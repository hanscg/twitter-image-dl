import configparser
import os
import requests
import time

config = configparser.RawConfigParser()
config.read('config/config.properties')

target_user = config.get('Target', 'username')

def download():
    # Open input file
    parse_filename = 'data/' + target_user + '.txt'
    inputfile = open(parse_filename)

    # Read lines
    lines = inputfile.read().splitlines()

    # Create folder if not exist
    foldername = 'downloads/' + target_user
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    # Iterate lines
    for media_url in lines:    
        #Get file name from url
        filename = media_url.split('/')[-1]
        
        #Get file extension from file name
        extension = filename.rpartition('.')[2]

        #Set URL parameter to get original file
        url_param = '?format=' + extension + '&name=orig'

        #Remove extension from url then concat with parameter
        url = media_url.rpartition('.')[0] + url_param

        #Retrieve from url
        r = requests.get(url)

        #Write to file
        path = foldername + '/' + filename
        open(path, 'wb').write(r.content)
        print(url + ' downloaded')

        #Sleep to throttle down the requests
        #time.sleep(1)
