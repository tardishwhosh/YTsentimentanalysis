#cleaning text steps
#1 create a text file and take text from it
#2 convert the letter into lowercase
#3 remove punctuations
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
text = open('Read.txt', encoding= 'utf-8').read()
lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation)) #lower case to a string without punctuations


tokenized_words = word_tokenize(cleaned_text,"english") #.split takes a lot of time when read.txt gets big, this works optimally.


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# NLP Emotion Algorithm
#1 check if the word is in the final word list is also in emotions
#open emotion file
#loop through each line
#extract the word and emotion using split

#2 if word is present add the emotion to emotion_list

#3 count each emotion in the emotion list
emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace("'",'').strip()

        word, emotion = clear_line.split(':')


        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg= score['neg']
    pos= score['pos']
    if neg>pos:
        print("Negative Sentiment")

    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("The vibe is neutral")


sentiment_analyse(cleaned_text)



fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('plot.png')
plt.show()





