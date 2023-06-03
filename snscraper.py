from snscrape.modules.twitter import TwitterUserScraper, TwitterProfileScraper
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import openai
import re


openai.api_key = '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'

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
    limit = int(input("Enter the number of tweets to dump (default is 100): ") or "100")
    return username, limit

def scrape_tweets_by_hashtag(hashtag, num_tweets=100):

    # Calculate the date 30 days ago
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # Format dates in the YYYY-MM-DD format that TwitterSearchScraper requires
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # Creating list to append tweet data to
    tweets = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{hashtag} lang:en since:{start_date_str} until:{end_date_str}').get_items()):
        if i > num_tweets:
            break
        tweets.append(tweet)

    # Printing out tweets
    for tweet in tweets:
        print(tweet.content)


def user_info(username, limit=100):
    
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
        if count >= limit:
            break
        tweets.append(tweet.rawContent)

    # Interact with OpenAI GPT API
    # response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #                {"role": "user", "content": f"Please generate profile using theses following  data that I will give you  (tweets) : {user_infos}, {tweets}. evaluate the content of their posts, tweets, retweets, shared content, the people they interact with, the hashtags they use, their professional background, skills, endorsements, and interests listed on LinkedIn. Taking these into account, provide a comprehensive profile of this individual. This profile should ideally include their professional background, possible career aspirations, personal interests, social circles, political inclinations, favored topics, general sentiment of their posts, and potential future behavior. Remember to respect ethical guidelines and privacy considerations during this evaluation."},
    #         ],
    #     )
    
    # print("ChatGPT Response: ", response.choices[0].message['content'])

    # Create a DataFrame and print it
    print("---------------------debug--------------------")
    print(tweets)
    df = pd.DataFrame(tweets)
    print(df)
 
def main (): 
    hashtag, num_tweets = get_user_input()
    if check_hashtag(hashtag) == True : 
        scrape_tweets_by_hashtag(hashtag,num_tweets) 
    else : 
       user_info (hashtag,num_tweets)

if __name__ == '__main__':
    main()
    text = "C’est pour moi un honneur d’appartenir à la 50è promotion de science politique mention : communication politique et institutionnelle de la @SorbonneParis1.Merci à toutes et à tous !RDV AU SOMMET ! ♥️ https://t.co/IhAc9IWvZR', 'RT @fortius0: Mon édito cette semaine revient sur la mort lente du journalisme 🇹🇩ien à travers le conflit agriculteurs éleveurs.@gouwala…', '@KaatyDiallo @KeessoBlvck on parle de vous ici 😂', 'À l’instant 🤩 https://t.co/8Zn2tqs2AQ', 'Pourquoi certains chefs d’Etats africains prennent pour luxe le fait que le peuple leur demande de s’exprimer clairement à la fin de leur dernier mandat ?nEn principe, on ne devrait même pas attendre d’eux qu’ils s’expriment là-dessus, cela devrait être automatique 🤦🏾', 'Ok… la suite nous édifiera donc après la défense des forces de l’ordre 🤦🏾', '@miisbaou a découvert message vocal sur Twitter maintenant c’est 3 minutes de vocal il m’envoie.Il va finir les vocaux de la Guinée 😂😂', 'Quels sont les bons pictogrammes pour le facile à lire et à comprendre (FALC)#Communication #accessible\nhttps://t.co/EwoByK01Iy', 'Mais déjà ?Mince !nMerci pour tout en tout cas !', 'En clair, Ibrahima Diallo et cie ont été libérés d’une petite prison pour une grande prison.', 'RT @FacelyKonate1: Retour à la maison et en classe après les #GGTour2023 . #TeamFK https://t.co/nqPTK1dm7e', 'Joyeux anniversaire au polémiste le plus sous côté de la TL224', 'RT @diallo_moud: Les ethnocentriques sont pour moi, dans leur essence, des gens profondément injuste. \nAutrement, je ne peux comprendre, co…', 'Ibrahima Diallo du FNDC empêché de voyager à l’aéroport de Conakry sans aucune raison.🤦🏾', 'Autogoal 🤔', 'En boucle par des africains qui traiteraient leurs propres frères de sauvages 🙈🤦🏾😂', '🔴OPPORTUNITÉ EN #GUINÉE🔴Vous avez le goût du challenge, vous êtes passionné de #communication et du secteur agricole, ce poste est peut-être pour vous.Postulez ! https://t.co/4JidWcL9g5'RT @AlphaBalde91: @blemoul https://t.co/PUqE8ovmF6  parles de ça c'est la meilleure sonorité à écouter pour le football en Guinée. OUI je sRT @Nogent94130: #weekend 100% vélo, la municipalité, @MDBIDF et les vélos du viaduc ont mis en place 2 jours d'activités dédiés au #vélo l…, 'RT @LemediaAfrique: Football : Chancel remporte le prix Marc-Vivien Foé\https://t.co/n7uBY7bZTS"
 
    #generate_wordcloud(text)