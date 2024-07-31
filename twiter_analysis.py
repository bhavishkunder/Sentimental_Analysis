



import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got

def gettweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2020-08-03") \
        .setUntil("2021-09-30") \
        .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets=[[tweets.text] for tweet in tweets]
    return text_tweets
text=""
text_tweets= gettweets()
length=len(text_tweets)
print(length)
for i in range(0,length+1):
    text=text_tweets[i][0]+" "+text
# reading text file
#text=open('read.txt',encoding='utf-8').read()
# converting to lowercase
lower_case=text.lower()
# Removing punctuations
cleaned_text=lower_case.translate(str.maketrans(' ', ' ', string.punctuation))
# splitting text into words
tokenization_word=cleaned_text.split()
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
final_word=[]
emotion_list =[]
for word in tokenization_word:
    if word not in stop_words:
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

fig , ax1= plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()