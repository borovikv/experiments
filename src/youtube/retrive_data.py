# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from youtube.utils import get_client_secrets_file

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = get_client_secrets_file()

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    videos = youtube.videos()
    token = None
    while token is not False:
        response = most_popular(token, videos)
        token = response.get('nextPageToken', False)

        print(response)


def most_popular(token, videos):
    request = videos.list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        pageToken=token
    )
    return request.execute()


if __name__ == "__main__":
    main()
