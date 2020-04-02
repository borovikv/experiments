import json
import time
import urllib.request
from collections import namedtuple

from bs4 import BeautifulSoup

Video = namedtuple("Video", "video_id title duration views")


def parse_video_div(div):
    video_id = div.get("data-context-item-id", "")
    title = div.find("a", "yt-uix-tile-link").text
    duration = div.find("span", "video-time").contents[0].text
    views = int(div.find("ul", "yt-lockup-meta-info").contents[0].text.rstrip(" views").replace(",", ""))
    return Video(video_id, title, duration, views)


def parse_videos_page(page):
    video_divs = page.find_all("div", "yt-lockup-video")
    return [parse_video_div(div) for div in video_divs]


def find_load_more_url(page):
    for button in page.find_all("button"):
        url = button.get("data-uix-load-more-href")
        if url:
            return "http://www.youtube.com" + url


def download_page(url):
    return urllib.request.urlopen(url).read()


PARSER = "html.parser"


def get_videos(username):
    page_url = "http://www.youtube.com/user/{0}/videos".format(username)
    page = BeautifulSoup(download_page(page_url), PARSER)
    videos = parse_videos_page(page)
    page_url = find_load_more_url(page)
    while page_url:
        json_data = json.loads(download_page(page_url))
        page = BeautifulSoup(json_data.get("content_html", ""), PARSER)
        videos.extend(parse_videos_page(page))
        load_more_widget_html = json_data.get("load_more_widget_html", "")
        soup = BeautifulSoup(load_more_widget_html, PARSER)
        page_url = find_load_more_url(soup)
    return videos


if __name__ == "__main__":
    start = time.time()
    videos = get_videos("jimmydiresta")
    duration = time.time() - start
    for video in videos:
        print(video)
    print("duration {0} for {1} videos, {2}s per video".format(duration, len(videos), (duration)/len(videos)))
    # duration 4.682564973831177 for 30 videos, 0.1560854991277059s per video
    # ~ 2 day for 1e6 videos
