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
    maxResults=100
)
response = request.execute()

# Initialize an empty list to store the comments
comments_list = []

# Iterate over the items in the response and extract the comments
for item in response['items']:
    comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments_list.append(comment_text)

# Now you have all the comments stored in the comments_list variable
# You can perform your text analysis on this list

# Example text analysis code (assuming you have already imported required libraries)
lower_case = ' '.join(comments_list).lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

# Print the emotion list and perform further analysis as needed
print(emotion_list)
w = Counter(emotion_list)
print(w)

# Plotting the emotions
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('plot.png')
plt.show()