import configparser
import json
import twitter

config = configparser.RawConfigParser()
config.read('config/config.properties')

target_user = config.get('Target', 'username')

def parse():
    # Read list of json
    json_filename = 'data/' + target_user + '.json'
    input = open(json_filename)

    # Create output file
    parse_filename = 'data/' + target_user + '.txt'
    with open(parse_filename, 'w+') as f:
        # For each line from input file
        for line in input:
            # Load json from string
            tweet = json.loads(line)
            
            # Get extended entities
            entities = tweet.get('extended_entities')
            if entities is not None:
                # Get media
                medias = entities.get('media')

                if medias is not None:
                    # Get url and output
                    for media in medias:
                        f.write(media['media_url'])
                        f.write('\n')