# Sentimental Analysis 🧠💬

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![NLTK](https://img.shields.io/badge/NLTK-enabled-green?logo=nltk)](https://www.nltk.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-visualization-orange?logo=matplotlib)](https://matplotlib.org/)

A modern Python project for **sentiment and emotion analysis** on text data, featuring:
- Emotion extraction from text using a custom lexicon
- Sentiment scoring with VADER (NLTK)
- Visualizations: emotion frequency bar chart & word cloud
- Twitter scraping support (via GetOldTweets3)
- Logging and modular code structure

---

## 🚀 Features

- **Emotion Detection:** Maps words to emotions using [`emotions.txt`](emotions.txt)
- **Sentiment Analysis:** Uses VADER to classify text as positive, negative, or neutral
- **Visualization:** Generates bar charts and word clouds for insights
- **Twitter Integration:** (Optional) Analyze tweets with [`twiter_analysis.py`](twiter_analysis.py)
- **Logging:** Outputs analysis logs to `sentiment_analysis.log`

---

## 📦 Requirements

- Python 3.8+
- [NLTK](https://www.nltk.org/)
- [matplotlib](https://matplotlib.org/)
- [wordcloud](https://github.com/amueller/word_cloud)
- [GetOldTweets3](https://github.com/Mottl/GetOldTweets3) (for Twitter analysis)

Install dependencies:
```sh
pip install nltk matplotlib wordcloud GetOldTweets3

🛠️ Setup
Clone the repository:
git clone https://github.com/yourusername/Sentimental_Analysis.git
cd Sentimental_Analysis

Download NLTK data (first run only):
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

Prepare your input:

Place your text in read.txt
(Optional) Update emotions.txt for custom emotion mappings

Usage
1. Analyze Local Text
Run the main analyzer:
python [try.py](http://_vscodecontentref_/1)

Outputs sentiment, emotion frequencies, and saves a bar chart as graph.png
Displays a word cloud for the input text

. Analyze Tweets
Fetch and analyze tweets (edit query in twiter_analysis.py):
python [twiter_analysis.py](http://_vscodecontentref_/2)

📁 Project Structure
Sentimental_Analysis/
│
├── [emotions.txt](http://_vscodecontentref_/3)           # Emotion lexicon
├── [read.txt](http://_vscodecontentref_/4)               # Input text file
├── [try.py](http://_vscodecontentref_/5)                 # Main sentiment/emotion analyzer
├── [twiter_analysis.py](http://_vscodecontentref_/6)     # Twitter scraping & analysis
├── [mains.py](http://_vscodecontentref_/7)               # Simple/legacy analyzer
├── sentiment_analysis.log # Log file
├── [README.md](http://_vscodecontentref_/8)              # This file
└── .idea/                 # IDE/project settings

