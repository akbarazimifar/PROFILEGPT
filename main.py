import os
import re
from dotenv import load_dotenv
import argparse
import logging
from datetime import datetime, timedelta
from snscrape.modules.twitter import TwitterUserScraper, TwitterProfileScraper
import snscrape.modules.twitter as sntwitter
import pandas as pd
import openai
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import snscraper as sn

# Fetch the API Key from environment variable
load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Constants
DAYS_TO_LOOK_BACK = 30

def check_hashtag(user_input):
    """
    Check if the user input is a hashtag.
    """
    return bool(re.match(r'^#\w+', user_input))

def generate_wordcloud(text):
    """
    Generate and display a word cloud from the given text.
    """
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the generated image with matplotlib 
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main (): 
    parser = argparse.ArgumentParser(description='Scrape tweets and generate user profiles.')
    parser.add_argument('username', type=str, help='The username or hashtag to scrape')

    args = parser.parse_args()
    username = args.username


    if check_hashtag(username):
        sn.scrape_tweets_by_hashtag(username)
    else:
        sn.user_info(username)

if __name__ == '__main__':
    main()
