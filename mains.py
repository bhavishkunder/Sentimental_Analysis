import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# reading text file
text=open('read.txt',encoding='utf-8').read()
# converting to lowercase
lower_case=text.lower()
# Removing punctuations
cleaned_text=lower_case.translate(str.maketrans(' ', ' ', string.punctuation))
# splitting text into words
tokenization_word=word_tokenize(cleaned_text,"english")

final_word=[]
emotion_list =[]
for word in tokenization_word:
    if word not in stopwords.words("english"):
        final_word.append(word)
with open("emotions.txt","r") as file:
    for line in file:
        clear_line=line.replace("\n","").replace(",","").replace("'","").strip()
        word, emotion=clear_line.split(":")

        if word in final_word:
            emotion_list.append(emotion)
print(emotion_list)
w=Counter(emotion_list)
print(w)

def sentiment_analyze(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg > pos:
        print('Negative sentiment')
    elif pos > neg:
        print('positive Sentiment')
    else:
        print("Neutral Sentiment")

   
sentiment_analyze(cleaned_text)


fig , ax1= plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()