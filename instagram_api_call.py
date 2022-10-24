import pandas as pd
import numpy as np
import time
import json
from instagrapi import Client

#Initialize the instagrapi client
cl = Client()

#Define the relevant keys from the dictionary resulting from the API call
relevant_keys = ['pk','username','is_private','media_count','follower_count','following_count']

#Define the empty dictionary to hold the results 
all_calls_dict = {}

#Itearate over all usernames in users to get a dictionary with only the relevant keys
for u in users:
    time.sleep(15)
    try:
        complete_user_info = cl.user_info_by_username(u).dict() #Use instagrapi public method to get all the available info for the user "u"
    except:
        all_calls_dict[u] = {'status': '0', 'timestamp': time.time()}
        continue
    relevant_user_info = { your_key: complete_user_info[your_key] for your_key in relevant_keys } #Select only the relevant keys from the dictionary
    relevant_user_info['status'] = '1',
    relevant_user_info['timestamp'] = time.time()
    all_calls_dict[u] = relevant_user_info
    
#Serialize json
json_object = json.dumps(all_calls_dict, indent = 4)

#Define the json filename
json_filename = time.ctime().replace(" ","_") + '_api_call.json'

#Write to file
with open(json_filename, "w") as outfile:
    outfile.write(json_object)
