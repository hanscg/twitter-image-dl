## twitter-images-dl
A tool to scrape images from a user's tweets.

## Requirements
 - [python-twitter](https://pypi.org/project/python-twitter/)
 - [Twitter application token](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

## How to use
Write down your Twitter application token at config/config.properties.

    [API]
    consumer_key =
    consumer_secret =
    access_token_key =
    access_token_secret =

Write down the user name of the user that you want to scrape the images from.
You can specify whether to include retweets or replies. The default is to exclude both.

    [Target]
    username = 
    include_rts = False
    exclude_replies = True
Run main.py. It will retrieve the tweets of the specified user (up to the limit of 3200 tweets, as it is limited by Twitter API) into a JSON file, parse it to get the URL for the images, and download the images. The downloaded images can be found at downloads/&lt;username&gt;

## To-do
 - Use other library to retrieve the tweets that doesn't require application token. 
 - Add support to download videos.
 - Add support to retrieve tweets from a search query.
 - Check existing JSON file before retrieving tweets so as to only retrieve the tweets that has not been retrieved.
