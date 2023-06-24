from snscrape.modules.twitter import TwitterUserScraper, TwitterProfileScraper
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import openai
import re


openai.api_key = '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'
max_tweets=50
def check_hashtag(user_input):
   return bool(re.match(r'^#\w+', user_input))

def generate_wordcloud(text):
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the generated image with matplotlib 
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def get_user_input():
    username = input("Enter the username of the Twitter profile or a hashtag: ")
    #limit = int(input("Enter the number of tweets to dump (default is 10): ") or "10")
    return username

def scrape_tweets_by_hashtag(hashtag):


    # Calculate the date 30 days ago
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # Creating list to append tweet data to
    tweets = []
    tweet_content = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{hashtag} lang:en since:{start_date_str} until:{end_date_str}').get_items()):
        if i > max_tweets:
            break
        tweets.append(tweet)

    # Printing out tweets
    for tweet in tweets:
        #print(tweet.content)
        tweet_content.append(tweet.rawContent)

    # Interact with OpenAI GPT API
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                     {"role": "user", "content": f"Act as a digital forensics expert with a specialization in Open Source Intelligence (OSINT). Given the following tweet, {tweet_content} please analyze its content, context. Consider elements like the language used, sentiment, possible hidden meanings, location, potential network of interactions based on replies, likes, and retweets. Based on your analysis, provide detailed insights about the hashtag, probable geographic location, social networks, possible intentions, and any potential security threats or vulnerabilities that might be revealed. Please, also offer suggestions for further data points or OSINT avenues that might be worth exploring."},
              ],
          )
    result =  response.choices[0].message['content']
    print("ChatGPT Response: ", result)
    #print(tweet_content) 
    df = pd.DataFrame(tweet_content)
    print(df)
    return result

def user_info(username):
    
    # Get user description
    user = next(TwitterUserScraper(username).get_items())
    print(f"User description: {user.user.renderedDescription}")
    print(f"Date created: {user.user.created}")
    print(f"Display name : {user.user.displayname}") 
    print(f"location : {user.user.location}")  
    print(f"Followers  : {user.user.followersCount}")  
    print(f"Friends  : {user.user.friendsCount}")  
    print(f"favourites  : {user.user.favouritesCount}")  

    print("---------------------------------------------------")

    user_infos = {
        "User description" :user.user.renderedDescription,
        "Date created" : user.user.created,
        "Display name ": user.user.displayname,
        "location ": user.user.location, 
        "Followers  ": user.user.followersCount,
        "Friends  ": user.user.friendsCount,
        "favourites ": user.user.favouritesCount 
    }

    # Get user tweets
    tweets = []
    for count, tweet in enumerate(TwitterProfileScraper(username).get_items()):
        if count >= max_tweets:
            break
        tweets.append(tweet.rawContent)

    # Interact with OpenAI GPT API
    response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=[
                    {"role": "user", "content": f"Please generate profile using theses following  data that I will give you  (tweets) : {user_infos}, {tweets}. evaluate the content of their posts, tweets, retweets, shared content, the people they interact with, the hashtags they use, their professional background, skills, endorsements, and interests listed on LinkedIn. Taking these into account, provide a comprehensive profile of this individual. This profile should ideally include their professional background, possible career aspirations, personal interests, social circles, political inclinations, favored topics, general sentiment of their posts, and potential future behavior. Remember to respect ethical guidelines and privacy considerations during this evaluation."},
             ],
         )
    
    result =  response.choices[0].message['content']
    print("ChatGPT Response: ", result)

    #Create a DataFrame and print it
    
    df = pd.DataFrame(tweets)
    print(df)
    return result
 
def main (): 
    user_input = get_user_input()
    if check_hashtag(user_input) == True : 
        scrape_tweets_by_hashtag(user_input) 
    else : 
       user_info (user_input)
       
if __name__ == '__main__':
    main()