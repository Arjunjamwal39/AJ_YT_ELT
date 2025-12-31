import requests 
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path = "./.env")
API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLER = "MrBeast"

def get_playlist_id(): #fucntion to fetch playlist id from YT channel
    try:               #prevents program from crashing

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLER}&key={API_KEY}"
        #calls YT API 

        response = requests.get(url) #This line sends an HTTP 
        #GET request to the given URL and stores the server’s 
        #response in the variable response.
        
        #print(response)
        response.raise_for_status()

        data = response.json() #This line parses the HTTP 
        #response body from JSON format into a Python 
        #dictionary  or list.

        #print(json.dumps(data, indent = 4)) #This line converts 
        #a Python object into a pretty-printed JSON string 
        #with 4-space indentation.

        channel_items = data["items"][0]

        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]['uploads']
        print(channel_playlist_id)

        return channel_playlist_id
    except request.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()