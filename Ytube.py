
import googleapiclient.discovery
import googleapiclient.errors


#cleaning text steps
#1 create a text file and take text from it
#2 convert the letter into lowercase
#3 remove punctuations
import string
from collections import Counter
import matplotlib.pyplot as plt

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "enter your developer key"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="enter your video ID",
    maxResults=25
)
response = request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])






