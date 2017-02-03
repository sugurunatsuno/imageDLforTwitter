from requests_oauthlib import OAuth1Session
import json
from urllib import request
import argparse
import random

parser = argparse.ArgumentParser(description='image download from twitter account')
parser.add_argument("--followers", type=bool, default=False)
parser.add_argument("--user", type=str, default=None)
parser.add_argument("--path", type=str, default=None)

args = parser.parse_args()

path = args.path

key0 = {
            "CK":'',
            "CS":'',
            "AT":'',
            "AS":'',

        }


key1 = {
            "CK":'',
            "CS":'',
            "AT":'',
            "AS":'',
        }

key_list = [key0, key1]

def get_media_url_from_tweet(tweet):
    """
    ツイートのメディアurlを取得する
    """
    ls = []
    try:
        for i in tweet["extended_entities"]["media"]:
            if (i["media_url"].split(".")[-1] == "jpg" or i["media_url"].split(".")[-1] == "png"):
                ls.append(i["media_url"])
        return ls
    except:
        return ls

def downloadImageFromInternet(source, path):

    response = request.urlopen(source+":orig")

    if response.code != 200:
        return -1

    with open(path + "/" + source.split("/")[-1], "wb") as fout:
        fout.write(response.read())
    return 1


def tweet_to_image(tweet, path):
    urls = get_media_url_from_tweet(tweet)
    for i in urls:
        try:
            downloadImageFromInternet(i, path)
        except:
            pass

def get_session(key_list):
    keys = random.choice(key_list)
    for key in key_list:
        if key == keys:
            num = key_list.index(key)


    sess = OAuth1Session(keys["CK"], keys["CS"], keys["AT"], keys["AS"])
    return sess

if not args.followers:

    sess = get_session(key_list)

    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    params = {"count":50,
              "include_entities" : 1,
              }

    req = sess.get(url, params=params)
    timeline = json.loads(req.text)

    for tweet in timeline:
        tweet_to_image(tweet, path)

else:

    sess = get_session(key_list)

    url = "https://api.twitter.com/1.1/friends/list.json"
    params = {"count":200,}

    if args.user is not None:
        params["screen_name"] = args.user

    req = sess.get(url, params=params)
    users = json.loads(req.text)
    for user in users["users"]:

        screen_name = user["screen_name"]
        print(screen_name)


        max_id = 0
        for i in range(16):

            sess = get_session(key_list)

            url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

            params = {"count":200,
                      "include_entities" : 1,
                      "screen_name" : screen_name,
                     }


            if max_id != 0:
                params["max_id"] = max_id

            req = sess.get(url, params=params)
            timeline = json.loads(req.text)

            for tweet in timeline:
                tweet_to_image(tweet, path)

            max_id = timeline[-1]["id"]
