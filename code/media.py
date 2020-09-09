#-*- coding: utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
from datetime import datetime as dt
from datetime import date, timedelta

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)


# tweet
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

today = dt.strftime(dt.today(), '%Y-%m-%d')
image = 'media'+ today +'.png'

# media
files = {"media" : open(image, 'rb')}
req_media = twitter.post(url_media, files = files)

# configure response
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# get Media ID 
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# tweet with Media ID 
params = {'status': '1週間の睡眠記録', "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# configure response again
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
