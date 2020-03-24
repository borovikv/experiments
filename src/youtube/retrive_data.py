# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from youtube.utils import get_client_secrets_file

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = get_client_secrets_file()

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()

a = {'kind': 'youtube#videoListResponse', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/rLvdEZu4aBFUMtl8niHcqkPANKg"',
 'nextPageToken': 'CAUQAA', 'pageInfo': {'totalResults': 200, 'resultsPerPage': 5}, 'items': [
    {'kind': 'youtube#video', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/QpzjPq3_myCrDoipXlZFrc2Nzvk"', 'id': 'dqRZDebPIGs',
     'snippet': {'publishedAt': '2020-03-23T16:00:10.000Z', 'channelId': 'UCF_fDSgPpBQuh1MsUTgIARQ',
                 'title': 'The Weeknd - In Your Eyes (Official Video)',
                 'description': 'Official music video by The Weeknd performing "In Your Eyes"– \'After Hours" available everywhere now: http://theweeknd.co/afterhoursYD\n\n►Subscribe to The Weeknd on YouTube: http://theweeknd.co/subscribeYD \n\n►Get tickets: https://www.theweeknd.com/tour\n\n►Get exclusive merch: https://shop.theweeknd.com/\n\n►Follow The Weeknd:\nhttps://twitter.com/theweeknd \nhttps://www.facebook.com/theweeknd \nhttps://www.instagram.com/theweeknd \nhttps://www.theweeknd.com \n\nDirector: Anton Tammi\n\nStarring: Zaina Miuccia\n\nProduction Company: Somesuch\nExecutive Producer: Saskia Whinney\n\nProducer: Sarah Park\n\nDirector of Photography: Oliver Millar\n2nd Unit DP: Devin "Daddy" Karringten\nSteadicam Op: Nick Mueller\n\nProduction Designer: Miranda Lorenz\nCostume Designer: Alana Morshead\nSFX Makeup: Koji Ohmura\n\nMake up Artist: Fatma Bendris\nMake up Artist: Christine Nelli\n\n1st AD: Kenneth Taylor\n\nEditor: Andreas Arvidsson\nAssistant Editor: Janne Vartia\n2nd Assistant Editor: Tim Montana\nPost Production Supervisor: Alec Ernest\n\nColorist: Nicke Jacobsson\nAssistant Colorist: Sander van Wijk\nEditorial/Color Talent Mgmt: Sofia Misgena & Helene\nMisgena @ The Talent Group\n\nSound Design: Anton Ahlberg @ Red Pipe Studios\n\nVFX: Mathematic\nTitle Design: Aleksi Tammi\n\nLyrics:\n\nI just pretend that I’m in the dark\nI don’t regret cause my heart can’t take a loss\nI’d rather be so oblivious\nI’d rather be with you\nWhen it’s said, when it’s done yeah\nI don’t ever wanna know\nI can tell what you done yeah\nWhen I look at you\nin your eyes\nI see there’s something burning inside you\nOh inside you\nIn your eyes, I know it hurts to smile\nBut you try to, oh you try to\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes, you lie but I don’t let it define you\nOh define you\nI tried to find love in someone else too many times\nBut I hope you know I mean it\nWhen I tell you you’re the one that was on my mind oh\nWhen it’s said, when it’s done\nI would never let you know\nI’m ashamed of what I done\nWhen I look at you\nIn your eyes\nI see there’s something burning inside you\nOh inside you\nIn your eyes I know it hurts to smile\nBut you try to, oh you try to\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes you lie but I don’t let it define you\nOh define you\nIn your eyes\nI see there’s something burning inside you\nOh inside you\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes you lie but I don’t let it define you\nOh define you\n\n#TheWeeknd #InYourEyes #AfterHours\n\n\nMusic video by The Weeknd performing In Your Eyes. © 2020 The Weeknd XO, Inc., manufactured and marketed by Republic Records, a division of UMG Recordings, Inc.',
                 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/dqRZDebPIGs/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/dqRZDebPIGs/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/dqRZDebPIGs/hqdefault.jpg', 'width': 480, 'height': 360},
                     'standard': {'url': 'https://i.ytimg.com/vi/dqRZDebPIGs/sddefault.jpg', 'width': 640,
                                  'height': 480},
                     'maxres': {'url': 'https://i.ytimg.com/vi/dqRZDebPIGs/maxresdefault.jpg', 'width': 1280,
                                'height': 720}}, 'channelTitle': 'TheWeekndVEVO',
                 'tags': ['The', 'Weeknd', 'Your', 'Eyes', 'Republic', 'Records', 'the weeknd in your eyes',
                          'in your eyes the weeknd', 'the weeknd your eyes', 'your eyes the weeknd',
                          'in your eyes official music video', 'in your eyes premiere',
                          'the weeknd in your eyes music video', 'your eyes official music video', 'the weekend',
                          'weekend', 'the weekend in your eyes', 'in your eyes the weekend', 'in your eyes lyrics',
                          'the weeknd', 'the weeknd new song', 'after hours', 'the weeknd after hours', 'after',
                          'hours', 'the'], 'categoryId': '10', 'liveBroadcastContent': 'none',
                 'localized': {'title': 'The Weeknd - In Your Eyes (Official Video)',
                               'description': 'Official music video by The Weeknd performing "In Your Eyes"– \'After Hours" available everywhere now: http://theweeknd.co/afterhoursYD\n\n►Subscribe to The Weeknd on YouTube: http://theweeknd.co/subscribeYD \n\n►Get tickets: https://www.theweeknd.com/tour\n\n►Get exclusive merch: https://shop.theweeknd.com/\n\n►Follow The Weeknd:\nhttps://twitter.com/theweeknd \nhttps://www.facebook.com/theweeknd \nhttps://www.instagram.com/theweeknd \nhttps://www.theweeknd.com \n\nDirector: Anton Tammi\n\nStarring: Zaina Miuccia\n\nProduction Company: Somesuch\nExecutive Producer: Saskia Whinney\n\nProducer: Sarah Park\n\nDirector of Photography: Oliver Millar\n2nd Unit DP: Devin "Daddy" Karringten\nSteadicam Op: Nick Mueller\n\nProduction Designer: Miranda Lorenz\nCostume Designer: Alana Morshead\nSFX Makeup: Koji Ohmura\n\nMake up Artist: Fatma Bendris\nMake up Artist: Christine Nelli\n\n1st AD: Kenneth Taylor\n\nEditor: Andreas Arvidsson\nAssistant Editor: Janne Vartia\n2nd Assistant Editor: Tim Montana\nPost Production Supervisor: Alec Ernest\n\nColorist: Nicke Jacobsson\nAssistant Colorist: Sander van Wijk\nEditorial/Color Talent Mgmt: Sofia Misgena & Helene\nMisgena @ The Talent Group\n\nSound Design: Anton Ahlberg @ Red Pipe Studios\n\nVFX: Mathematic\nTitle Design: Aleksi Tammi\n\nLyrics:\n\nI just pretend that I’m in the dark\nI don’t regret cause my heart can’t take a loss\nI’d rather be so oblivious\nI’d rather be with you\nWhen it’s said, when it’s done yeah\nI don’t ever wanna know\nI can tell what you done yeah\nWhen I look at you\nin your eyes\nI see there’s something burning inside you\nOh inside you\nIn your eyes, I know it hurts to smile\nBut you try to, oh you try to\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes, you lie but I don’t let it define you\nOh define you\nI tried to find love in someone else too many times\nBut I hope you know I mean it\nWhen I tell you you’re the one that was on my mind oh\nWhen it’s said, when it’s done\nI would never let you know\nI’m ashamed of what I done\nWhen I look at you\nIn your eyes\nI see there’s something burning inside you\nOh inside you\nIn your eyes I know it hurts to smile\nBut you try to, oh you try to\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes you lie but I don’t let it define you\nOh define you\nIn your eyes\nI see there’s something burning inside you\nOh inside you\nYou always try to hide the pain\nYou always know just what to say\nI always look the other way\nI’m blind, I’m blind\nIn your eyes you lie but I don’t let it define you\nOh define you\n\n#TheWeeknd #InYourEyes #AfterHours\n\n\nMusic video by The Weeknd performing In Your Eyes. © 2020 The Weeknd XO, Inc., manufactured and marketed by Republic Records, a division of UMG Recordings, Inc.'}},
     'contentDetails': {'duration': 'PT5M42S', 'dimension': '2d', 'definition': 'hd', 'caption': 'true',
                        'licensedContent': True, 'regionRestriction': {
             'allowed': ['SG', 'SE', 'SD', 'SC', 'SB', 'SA', 'SO', 'SN', 'SM', 'SL', 'SK', 'SJ', 'SI', 'SH', 'SV', 'ST',
                         'SR', 'SZ', 'SY', 'SX', 'CW', 'CV', 'CU', 'CR', 'KI', 'KH', 'KG', 'KE', 'CZ', 'CY', 'CX', 'CG',
                         'CF', 'CD', 'CC', 'KZ', 'CA', 'CO', 'CN', 'CM', 'CL', 'CK', 'KR', 'CI', 'CH', 'LY', 'LR', 'LS',
                         'LV', 'LT', 'LU', 'LK', 'LI', 'LB', 'LC', 'LA', 'DE', 'DJ', 'DK', 'DO', 'DM', 'DZ', 'MY', 'MX',
                         'MZ', 'ZA', 'MQ', 'MP', 'MS', 'MR', 'MU', 'MT', 'MW', 'MV', 'MH', 'MK', 'YT', 'MM', 'ML', 'MO',
                         'MN', 'MA', 'MC', 'ME', 'MD', 'MG', 'MF', 'TR', 'EC', 'EE', 'TW', 'EG', 'TZ', 'EH', 'TC', 'ES',
                         'ER', 'TF', 'TG', 'TD', 'TJ', 'TK', 'TH', 'TN', 'TO', 'TL', 'TM', 'NZ', 'KN', 'NU', 'NP', 'KM',
                         'NR', 'NL', 'NO', 'NI', 'NE', 'NF', 'NG', 'NA', 'NC', 'US', 'UY', 'FM', 'FO', 'FI', 'FJ', 'FK',
                         'UA', 'FR', 'VG', 'UM', 'WF', 'ZM', 'JP', 'WS', 'ZW', 'OM', 'VU', 'GY', 'GS', 'GR', 'GQ', 'GP',
                         'GW', 'GU', 'GT', 'VE', 'GI', 'GH', 'VA', 'GM', 'GL', 'GB', 'GA', 'GG', 'GF', 'GE', 'GN', 'PN',
                         'UG', 'HT', 'HU', 'HR', 'KY', 'PH', 'PF', 'PG', 'PE', 'PA', 'KW', 'PY', 'HN', 'PW', 'PT', 'HM',
                         'PR', 'HK', 'JO', 'VI', 'VC', 'PS', 'GD', 'IT', 'UZ', 'IQ', 'IS', 'IR', 'TT', 'QA', 'PL', 'IE',
                         'ID', 'PM', 'IM', 'IL', 'IN', 'PK', 'AX', 'AZ', 'AU', 'AT', 'AW', 'AQ', 'AS', 'AR', 'AM', 'AL',
                         'AO', 'AI', 'AE', 'AD', 'AG', 'AF', 'RE', 'VN', 'RO', 'ET', 'RS', 'RU', 'RW', 'TV', 'YE', 'BQ',
                         'BR', 'BS', 'BT', 'JM', 'BV', 'BW', 'BY', 'BZ', 'JE', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH',
                         'BI', 'BJ', 'BL', 'BM', 'BN', 'BO']}, 'projection': 'rectangular'},
     'statistics': {'viewCount': '2875207', 'likeCount': '287591', 'dislikeCount': '4048', 'favoriteCount': '0',
                    'commentCount': '19542'}},
    {'kind': 'youtube#video', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/HLNAyvi8PKStjpRrkY59HEuwGnQ"', 'id': 'd0uFNajqTZI',
     'snippet': {'publishedAt': '2020-03-22T21:45:01.000Z', 'channelId': 'UCnM1ay_QoQOpa1N2iejLA7A',
                 'title': "We broke up... we're not moving in together anymore",
                 'description': "We're sorry guys, we love you and appreciate all the support. Thanks for everything.\n\n20% off JATIE BEAUTY LINK: https://jatiebeauty.com/\n\nPROPOSAL VID: https://youtu.be/U7VEN2EZkI8\n\nNEW MERCH: http://fanjoy.co/jatie\n\nMakeup giveaway! \nFollow @jatiebeauty for a chance to win! \n\nSUBSCRIBE & FOLLOW ON THE IG FOR A CHANCE TO WIN SOME AIRPODS!\n@joshbrueckner\n@katiebetzing \n@jatiebeauty \n\nTiktok: @joshxkatie\n\n-PRANK WARS-\nYou can look but you CANT touch prank: https://youtu.be/WtVe0typDVI\nBeing PDA in front of our friends: https://youtu.be/-MP2E1IiHXg\nBeing mean to my fiancé: https://youtu.be/Yi6T9UCslx0\n\n\n•Follow Us On Social Media•\nInstagram: @katiebetzing @Joshbrueckner\nFitness Instagram @J80Fit\nTwitter: @ktbetzing @Joshbrueckner \nSnapchat: @k80betz @Joshbrueckner\n\nHow we met: https://youtu.be/Ed6MYkS1-eo\nKatie’s Main Channel: https://www.youtube.com/user/Beautygu...\n\nBusiness inquiries: j80vlogs@gmail.com",
                 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/d0uFNajqTZI/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/d0uFNajqTZI/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/d0uFNajqTZI/hqdefault.jpg', 'width': 480, 'height': 360},
                     'standard': {'url': 'https://i.ytimg.com/vi/d0uFNajqTZI/sddefault.jpg', 'width': 640,
                                  'height': 480},
                     'maxres': {'url': 'https://i.ytimg.com/vi/d0uFNajqTZI/maxresdefault.jpg', 'width': 1280,
                                'height': 720}}, 'channelTitle': 'Jatie Vlogs',
                 'tags': ['we broke up', 'break up', 'broke up', 'why we broke up',
                          'were not moving in together anymore', 'its over', 'jatie vlogs break up', 'jatie vlogs',
                          'jatie vlogs pranks', 'move in vlog', 'emtpy house tour', 'the break up',
                          'why we arent together anymore', 'boyfriend', 'girlfriend', 'calling off the engagement',
                          'prank', 'jatie house', 'josh and katie', 'jatie house tour', 'josh brueckner',
                          'katie betzing', 'house tour', 'opening up about our break up', 'im sorry',
                          'why we really broke up'], 'categoryId': '1', 'liveBroadcastContent': 'none',
                 'localized': {'title': "We broke up... we're not moving in together anymore",
                               'description': "We're sorry guys, we love you and appreciate all the support. Thanks for everything.\n\n20% off JATIE BEAUTY LINK: https://jatiebeauty.com/\n\nPROPOSAL VID: https://youtu.be/U7VEN2EZkI8\n\nNEW MERCH: http://fanjoy.co/jatie\n\nMakeup giveaway! \nFollow @jatiebeauty for a chance to win! \n\nSUBSCRIBE & FOLLOW ON THE IG FOR A CHANCE TO WIN SOME AIRPODS!\n@joshbrueckner\n@katiebetzing \n@jatiebeauty \n\nTiktok: @joshxkatie\n\n-PRANK WARS-\nYou can look but you CANT touch prank: https://youtu.be/WtVe0typDVI\nBeing PDA in front of our friends: https://youtu.be/-MP2E1IiHXg\nBeing mean to my fiancé: https://youtu.be/Yi6T9UCslx0\n\n\n•Follow Us On Social Media•\nInstagram: @katiebetzing @Joshbrueckner\nFitness Instagram @J80Fit\nTwitter: @ktbetzing @Joshbrueckner \nSnapchat: @k80betz @Joshbrueckner\n\nHow we met: https://youtu.be/Ed6MYkS1-eo\nKatie’s Main Channel: https://www.youtube.com/user/Beautygu...\n\nBusiness inquiries: j80vlogs@gmail.com"}},
     'contentDetails': {'duration': 'PT10M50S', 'dimension': '2d', 'definition': 'hd', 'caption': 'false',
                        'licensedContent': True, 'projection': 'rectangular'},
     'statistics': {'viewCount': '2204996', 'likeCount': '76135', 'dislikeCount': '35041', 'favoriteCount': '0',
                    'commentCount': '56472'}},
    {'kind': 'youtube#video', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/SdHYDp1yQ15jI96e3AkqyR4hawA"', 'id': 'iVfWEoerrTY',
     'snippet': {'publishedAt': '2020-03-22T23:00:10.000Z', 'channelId': 'UCwD4x63A9KC7Si2RuSfg-SA',
                 'title': 'Dobre Brothers - You Know You Lit ft. Lil Pump (Official Video)',
                 'description': "It's LIT Dobre Army!🔥 STREAM You Know You Lit here➡\n\nhttps://open.spotify.com/track/429k38tTAHEXrAYZRvvxYA?si=gA51TlZ7SbmDAZkRME5gdA\n\nhttps://music.apple.com/us/album/you-know-you-lit-feat-lil-pump/1503987313?i=1503987320\n\nDirected by Alex Hassan\nProduced by laviedeeric\nEngineered by Nakuu\nCover art by primo_estilo\nOriginal Beat by Young D of Trap Team Beats\n\nDOWNLOAD DOBRE DUNK! 🏀http://bit.ly/DownloadDOBREDUNK\nMERCH 🔥 http://bit.ly/NewDobreMerch\n\nWE POST TUESDAY,THURSDAY, & SUNDAY!\nTURN OUR POST NOTIFICATIONS ON FOR A SHOUTOUT!\n\nSUBSCRIBE TO THE DOBRE VLOG CHANNEL! https://www.youtube.com/channel/UCC3O...\n\nSUBSCRIBE TO THE LUCAS AND MARCUS CHANNEL!\nhttps://www.youtube.com/user/TwiNboTz... \n\nLucas's Social Media \n \nInstagram: https://www.instagram.com/lucas_dobre/\nTwitter: https://twitter.com/dobrelucas\nFacebook: https://www.facebook.com/dobrelucas/\nSnapchat: lucas_dobre\nTik Tok: DobreTwins\n \nMarcus's Social Media \n \nInstagram: https://www.instagram.com/marcusdobre\nTwitter: https://twitter.com/dobremarcus\nFacebook: https://www.facebook.com/marcusdobre/\nSnapchat: marcusdobre1\nTik Tok: Dobretwins\n\nFollow the Dobre Brothers: \nInstagram: https://www.instagram.com/dobrebrothers/\n\nBIZ - dobrebrothersmgmt@gmail.com\n \nTHANKS FOR WATCHING!\n\nDobre Brothers - You Know You Lit ft. Lil Pump (Official Video)\nhttps://www.youtube.com/user/TwiNboTzVids\n\n#DobreBrothers #LilPump #YouKnowYouLit #LucasandMarcus",
                 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/iVfWEoerrTY/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/iVfWEoerrTY/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/iVfWEoerrTY/hqdefault.jpg', 'width': 480, 'height': 360},
                     'standard': {'url': 'https://i.ytimg.com/vi/iVfWEoerrTY/sddefault.jpg', 'width': 640,
                                  'height': 480},
                     'maxres': {'url': 'https://i.ytimg.com/vi/iVfWEoerrTY/maxresdefault.jpg', 'width': 1280,
                                'height': 720}}, 'channelTitle': 'Lucas and Marcus',
                 'tags': ['lucas and marcus', 'dobre twins', 'dobre brothers', '24 hours', 'challenge',
                          'family friendly', 'handcuffed', 'girlfriend', 'twins', 'twin brother', 'challenges',
                          'gymnastics', 'dance', 'marcus and lucas', 'music', 'rap', 'pranks', 'grocery store', 'cars',
                          'reactions', 'games', 'family', 'animals', 'new', 'ivanita lomeli', 'cyrus and christina',
                          'relationship', 'crush', 'boyfriend', 'lil pump'], 'categoryId': '10',
                 'liveBroadcastContent': 'none',
                 'localized': {'title': 'Dobre Brothers - You Know You Lit ft. Lil Pump (Official Video)',
                               'description': "It's LIT Dobre Army!🔥 STREAM You Know You Lit here➡\n\nhttps://open.spotify.com/track/429k38tTAHEXrAYZRvvxYA?si=gA51TlZ7SbmDAZkRME5gdA\n\nhttps://music.apple.com/us/album/you-know-you-lit-feat-lil-pump/1503987313?i=1503987320\n\nDirected by Alex Hassan\nProduced by laviedeeric\nEngineered by Nakuu\nCover art by primo_estilo\nOriginal Beat by Young D of Trap Team Beats\n\nDOWNLOAD DOBRE DUNK! 🏀http://bit.ly/DownloadDOBREDUNK\nMERCH 🔥 http://bit.ly/NewDobreMerch\n\nWE POST TUESDAY,THURSDAY, & SUNDAY!\nTURN OUR POST NOTIFICATIONS ON FOR A SHOUTOUT!\n\nSUBSCRIBE TO THE DOBRE VLOG CHANNEL! https://www.youtube.com/channel/UCC3O...\n\nSUBSCRIBE TO THE LUCAS AND MARCUS CHANNEL!\nhttps://www.youtube.com/user/TwiNboTz... \n\nLucas's Social Media \n \nInstagram: https://www.instagram.com/lucas_dobre/\nTwitter: https://twitter.com/dobrelucas\nFacebook: https://www.facebook.com/dobrelucas/\nSnapchat: lucas_dobre\nTik Tok: DobreTwins\n \nMarcus's Social Media \n \nInstagram: https://www.instagram.com/marcusdobre\nTwitter: https://twitter.com/dobremarcus\nFacebook: https://www.facebook.com/marcusdobre/\nSnapchat: marcusdobre1\nTik Tok: Dobretwins\n\nFollow the Dobre Brothers: \nInstagram: https://www.instagram.com/dobrebrothers/\n\nBIZ - dobrebrothersmgmt@gmail.com\n \nTHANKS FOR WATCHING!\n\nDobre Brothers - You Know You Lit ft. Lil Pump (Official Video)\nhttps://www.youtube.com/user/TwiNboTzVids\n\n#DobreBrothers #LilPump #YouKnowYouLit #LucasandMarcus"}},
     'contentDetails': {'duration': 'PT2M33S', 'dimension': '2d', 'definition': 'hd', 'caption': 'false',
                        'licensedContent': True, 'projection': 'rectangular'},
     'statistics': {'viewCount': '1987945', 'likeCount': '116545', 'dislikeCount': '43815', 'favoriteCount': '0',
                    'commentCount': '31867'}},
    {'kind': 'youtube#video', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/Nwev3WhHjEp85l7d5gut0AgbbPQ"', 'id': 'pPn-Bay_ANU',
     'snippet': {'publishedAt': '2020-03-23T20:47:42.000Z', 'channelId': 'UCY1kMZp36IQSyNx_9h4mpCg',
                 'title': 'SCIENCE CLASS- WHY Does Helium Make Your Voice Higher?',
                 'description': 'Live stream with demos your brain will enjoy where we answer a basic question every time.\n\nDoes farting make you weigh more or less?!?!  Place your guess and give me feedback too- https://forms.gle/gqNw9Ht83Vzo2va4A',
                 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/pPn-Bay_ANU/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/pPn-Bay_ANU/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/pPn-Bay_ANU/hqdefault.jpg', 'width': 480, 'height': 360},
                     'standard': {'url': 'https://i.ytimg.com/vi/pPn-Bay_ANU/sddefault.jpg', 'width': 640,
                                  'height': 480},
                     'maxres': {'url': 'https://i.ytimg.com/vi/pPn-Bay_ANU/maxresdefault.jpg', 'width': 1280,
                                'height': 720}}, 'channelTitle': 'Mark Rober', 'categoryId': '28',
                 'liveBroadcastContent': 'none',
                 'localized': {'title': 'SCIENCE CLASS- WHY Does Helium Make Your Voice Higher?',
                               'description': 'Live stream with demos your brain will enjoy where we answer a basic question every time.\n\nDoes farting make you weigh more or less?!?!  Place your guess and give me feedback too- https://forms.gle/gqNw9Ht83Vzo2va4A'}},
     'contentDetails': {'duration': 'PT35M27S', 'dimension': '2d', 'definition': 'hd', 'caption': 'false',
                        'licensedContent': True, 'projection': 'rectangular'},
     'statistics': {'viewCount': '1031709', 'likeCount': '85186', 'dislikeCount': '875', 'favoriteCount': '0',
                    'commentCount': '4968'}},
    {'kind': 'youtube#video', 'etag': '"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/XS67y_rb3kVXQk7x3nha5heOCzw"', 'id': '9Suu5DPnntw',
     'snippet': {'publishedAt': '2020-03-23T15:00:02.000Z', 'channelId': 'UCpi8TJfiA4lKGkaXs__YdBA',
                 'title': 'The Try Guys Work From Home For 168 Hours',
                 'description': "We've been working from home all week and this is how it's going so far! What have you been doing to stay busy during your stay at home? #StayHome #WithMe #StayHomeSaveLives\n\nAre you a business looking to work with The Try Guys? Reach out to us at 2ndtrybusiness@gmail.com for all business inquiries! \n\n🎧THE TRYPOD 🎧: watch our new podcast at https://youtube.com/trypod or listen at https://tryguys.com/podcast\n\n📘THE HIDDEN POWER OF F*CKING UP 📘: check out our new book at https://tryguys.com/book\n\nGet your official Try Guys color hoodies and phone cases at https://tryguys.com/collections/color-line 💙❤️💚💜\n\nSupport us! http://www.patreon.com/tryguys. Join our Patreon to get videos a day early, plus, live streams, chatrooms, BTS footage, exclusive merchandise, and more!\n\nSUBSCRIBE TO AND FOLLOW THE TRY GUYS \nhttp://www.youtube.com/c/tryguys\nhttp://www.facebook.com/tryguys  \nhttp://www.twitter.com/tryguys\nhttps://www.instagram.com/tryguys\n\nFOLLOW THE GUYS\nhttp://www.Instagram.com/keithhabs\nhttp://www.Instagram.com/nedfulmer\nhttp://www.Instagram.com/korndiddy\nhttp://www.instagram.com/eugeneleeyang\n \nhttp://www.twitter.com/keithhabs\nhttp://www.twitter.com/nedfulmer \nhttp://www.twitter.com/korndiddy\nhttp://www.twitter.com/eugeneleeyang \n\nTHE TRY GUYS\nThe #TryGuys is the flagship channel of 2ND TRY, LLC. Tune in twice a week for shows from Keith, Ned, Zach and Eugene, the creators and stars of The Try Guys.\n\nEDITED BY\nYB Chang @xoybox\n\nMUSIC\nLicensed from AudioNetwork\n\nSFX\nLicensed from Audioblocks\n\nVIDEO\nLicensed from Videoblocks\n\nOfficial Try Guys Photos \nBy Mandee Johnson Photography | @mandeephoto\n\n2nd Try, LLC STAFF\nExecutive Producer - Keith Habersberger\nExecutive Producer - Ned Fulmer\nExecutive Producer - Zach Kornfeld\nExecutive Producer - Eugene Lee Yang\nProducer - Rachel Ann Cole\nProducer - Nick Rufca\nProduction Manager - Alexandria Herring\nEditor - Devlin McCluskey\nEditor - YB Chang\nEditor - Elliot Dickerhoof\nAssistant Editor - Will Witwer\nCamera Operator - Miles Bonsignore\nSound Operator - Jonathan Kirk\nAssistant Production Coordinator - Sam Johnson\nContent Strategist - Kaylin Burke\n\nSpecial Thanks To! \n\nThanks to all of our Gold Level Patrons! AJ S., Amy Fleming, Ana Camba, Cat Hicks, Elisa Proust, Emma Godfrey, Erica Rao, Jared Aarons, Kelsey Bock, Kourtney Wong, Loretta Wen, Matthew Tadros, Miha, Paulus, Sarah Waxman, Traci Lew, Wendy Tran, Lily",
                 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/9Suu5DPnntw/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/9Suu5DPnntw/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/9Suu5DPnntw/hqdefault.jpg', 'width': 480, 'height': 360},
                     'standard': {'url': 'https://i.ytimg.com/vi/9Suu5DPnntw/sddefault.jpg', 'width': 640,
                                  'height': 480},
                     'maxres': {'url': 'https://i.ytimg.com/vi/9Suu5DPnntw/maxresdefault.jpg', 'width': 1280,
                                'height': 720}}, 'channelTitle': 'The Try Guys',
                 'tags': ['try guys', 'keith', 'ned', 'zach', 'eugene', 'habersberger', 'fulmer', 'kornfeld', 'yang',
                          'buzzfeedvideo', 'buzzfeed', 'ariel', 'ned & ariel', 'comedy', 'education', 'funny', 'try',
                          'learn', 'fail', 'experiment', 'test', 'tryceratops', 'work from home',
                          'work from home challenge', 'stay at home', 'vlog', 'vlogging', 'family vlog',
                          'make money online', 'work from home 2020', 'work from home jobs', 'today trending',
                          'bullet journal', 'online job', 'morning routine', 'make money', 'rank king', 'hide and seek',
                          'board games', 'games to play', 'play games', 'news'], 'categoryId': '23',
                 'liveBroadcastContent': 'none', 'defaultLanguage': 'en',
                 'localized': {'title': 'The Try Guys Work From Home For 168 Hours',
                               'description': "We've been working from home all week and this is how it's going so far! What have you been doing to stay busy during your stay at home? #StayHome #WithMe #StayHomeSaveLives\n\nAre you a business looking to work with The Try Guys? Reach out to us at 2ndtrybusiness@gmail.com for all business inquiries! \n\n🎧THE TRYPOD 🎧: watch our new podcast at https://youtube.com/trypod or listen at https://tryguys.com/podcast\n\n📘THE HIDDEN POWER OF F*CKING UP 📘: check out our new book at https://tryguys.com/book\n\nGet your official Try Guys color hoodies and phone cases at https://tryguys.com/collections/color-line 💙❤️💚💜\n\nSupport us! http://www.patreon.com/tryguys. Join our Patreon to get videos a day early, plus, live streams, chatrooms, BTS footage, exclusive merchandise, and more!\n\nSUBSCRIBE TO AND FOLLOW THE TRY GUYS \nhttp://www.youtube.com/c/tryguys\nhttp://www.facebook.com/tryguys  \nhttp://www.twitter.com/tryguys\nhttps://www.instagram.com/tryguys\n\nFOLLOW THE GUYS\nhttp://www.Instagram.com/keithhabs\nhttp://www.Instagram.com/nedfulmer\nhttp://www.Instagram.com/korndiddy\nhttp://www.instagram.com/eugeneleeyang\n \nhttp://www.twitter.com/keithhabs\nhttp://www.twitter.com/nedfulmer \nhttp://www.twitter.com/korndiddy\nhttp://www.twitter.com/eugeneleeyang \n\nTHE TRY GUYS\nThe #TryGuys is the flagship channel of 2ND TRY, LLC. Tune in twice a week for shows from Keith, Ned, Zach and Eugene, the creators and stars of The Try Guys.\n\nEDITED BY\nYB Chang @xoybox\n\nMUSIC\nLicensed from AudioNetwork\n\nSFX\nLicensed from Audioblocks\n\nVIDEO\nLicensed from Videoblocks\n\nOfficial Try Guys Photos \nBy Mandee Johnson Photography | @mandeephoto\n\n2nd Try, LLC STAFF\nExecutive Producer - Keith Habersberger\nExecutive Producer - Ned Fulmer\nExecutive Producer - Zach Kornfeld\nExecutive Producer - Eugene Lee Yang\nProducer - Rachel Ann Cole\nProducer - Nick Rufca\nProduction Manager - Alexandria Herring\nEditor - Devlin McCluskey\nEditor - YB Chang\nEditor - Elliot Dickerhoof\nAssistant Editor - Will Witwer\nCamera Operator - Miles Bonsignore\nSound Operator - Jonathan Kirk\nAssistant Production Coordinator - Sam Johnson\nContent Strategist - Kaylin Burke\n\nSpecial Thanks To! \n\nThanks to all of our Gold Level Patrons! AJ S., Amy Fleming, Ana Camba, Cat Hicks, Elisa Proust, Emma Godfrey, Erica Rao, Jared Aarons, Kelsey Bock, Kourtney Wong, Loretta Wen, Matthew Tadros, Miha, Paulus, Sarah Waxman, Traci Lew, Wendy Tran, Lily"},
                 'defaultAudioLanguage': 'en'},
     'contentDetails': {'duration': 'PT25M45S', 'dimension': '2d', 'definition': 'hd', 'caption': 'false',
                        'licensedContent': True, 'projection': 'rectangular'},
     'statistics': {'viewCount': '1498728', 'likeCount': '93562', 'dislikeCount': '631', 'favoriteCount': '0',
                    'commentCount': '8642'}}]}


# print(len(a['items']))
