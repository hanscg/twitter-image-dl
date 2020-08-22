import configparser
import json
import twitter

config = configparser.RawConfigParser()
config.read('config/config.properties')

target_user = config.get('Target', 'username')

api = twitter.Api(
        consumer_key = config.get('API', 'consumer_key'), 
        consumer_secret = config.get('API', 'consumer_secret'), 
        access_token_key = config.get('API', 'access_token_key'), 
        access_token_secret = config.get('API', 'access_token_secret')
    )

def scrape():
    timeline = api.GetUserTimeline(
        screen_name=target_user,
        count=200,
        include_rts=config.get('Target', 'include_rts'),
        exclude_replies=config.get('Target', 'exclude_replies')
    )

    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(            
            screen_name=target_user,
            count=200,
            max_id=earliest_tweet,
            include_rts=config.get('Target', 'include_rts'),
            exclude_replies=config.get('Target', 'exclude_replies')
        )

        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest        
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    # Dump tweets to json file
    json_filename = 'data/' + target_user + '.json'
    with open(json_filename, 'w+') as f:
        for tweet in timeline:
            f.write(json.dumps(tweet._json))
            f.write('\n')