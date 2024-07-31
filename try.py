import os
import string
import logging
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.emotion_file = 'emotions.txt'
        self.log_file = 'sentiment_analysis.log'
        self.text_file = 'read.txt'
        self.graph_file = 'graph.png'
        self.analyzer = SentimentIntensityAnalyzer()

    def read_text_file(self, file_path):
        """Read and return the content of a text file."""
        try:
            with open(file_path, encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"Error: Text file '{file_path}' not found.")
            exit()

    def preprocess_text(self, text):
        """Preprocess the text."""
        lower_case = text.lower()
        cleaned_text = ''.join([char for char in lower_case if char not in string.punctuation])
        tokenized_words = word_tokenize(cleaned_text, "english")
        final_words = [word for word in tokenized_words if word not in stopwords.words("english")]
        return final_words

    def extract_emotions(self, final_words):
        """Extract emotions from the provided file."""
        emotion_list = []
        final_word_set = set(final_words)
        try:
            with open(self.emotion_file, "r") as file:
                for line in file:
                    clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
                    word, emotion = clear_line.split(":")
                    if word in final_word_set:
                        emotion_list.append(emotion)
        except FileNotFoundError:
            logging.error(f"Error: Emotions file '{self.emotion_file}' not found.")
            exit()
        return emotion_list

    def sentiment_analyze(self, sentiment_text):
        """Perform sentiment analysis on the provided text."""
        score = self.analyzer.polarity_scores(sentiment_text)
        neg, pos = score['neg'], score['pos']
        if neg > pos:
            print('Negative sentiment')
        elif pos > neg:
            print('Positive sentiment')
        else:
            print("Neutral sentiment")

    def plot_emotion_frequencies(self, emotion_list):
        """Plot a bar graph of emotion frequencies with a modern style."""
        plt.style.use('seaborn-darkgrid')
        frequencies = Counter(emotion_list)
        fig, ax1 = plt.subplots()
        colors = ['#FF6F61', '#A8DADC', '#457B9D', '#1D3557']
        bars = ax1.bar(frequencies.keys(), frequencies.values(), color=colors)
        ax1.set_xlabel('Emotion', fontsize=14)
        ax1.set_ylabel('Frequency', fontsize=14)
        ax1.set_title('Emotion Frequencies in Text', fontsize=16, fontweight='bold')
        ax1.tick_params(axis='both', which='major', labelsize=12)
        ax1.grid(axis='y', linestyle='--', alpha=0.7)

        # Add data labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)

        fig.autofmt_xdate()
        plt.savefig(self.graph_file, bbox_inches='tight')
        plt.show()

    def generate_wordcloud(self, text):
        """Generate and display a word cloud."""
        from wordcloud import WordCloud
        plt.style.use('seaborn-white')
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def main(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

        # Read text file
        text = self.read_text_file(self.text_file)

        # Preprocess text
        final_words = self.preprocess_text(text)

        # Extract emotions
        emotion_list = self.extract_emotions(final_words)

        # Perform sentiment analysis
        self.sentiment_analyze(text)

        # Plot emotion frequencies
        self.plot_emotion_frequencies(emotion_list)

        # Generate and display word cloud
        self.generate_wordcloud(text)

if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    sentiment_analyzer.main()
