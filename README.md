# OSINTGPT
OSINTGPT is a tool for analyzing profiles and hashtags on Twitter. The application exploits various technologies and APIs to collect data and generate information for users.


## Features
- **Profile Analysis**: Users can enter a Twitter username to retrieve information about the user's profile, including description, creation date, display name, location, followers count, friends count, and favorites count. The app uses the Twitter API and scraping techniques to collect the data.
- **Hashtag Analysis**: Users can input a hashtag to scrape and analyze tweets related to that hashtag. The app retrieves a specified number of recent tweets, performs sentiment analysis, and provides insights into the content, context, language used, sentiment, possible hidden meanings, and potential network of interactions based on replies, likes, and retweets. OpenAI's GPT API is utilized for analyzing the tweets.

## Technologies Used
- Python
- Flask
- HTML/CSS
- Bootstrap
- snscrape
- OpenAI GPT API

## Getting Started
1. Clone the repository: `git clone `
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI GPT API credentials by signing up for an API key on the [OpenAI website](https://openai.com/).
5. replace your OPENAI API KEY in sncraper.py like : 

`OPENAI_API_KEY='sk-YOUR_API_KEY'`

6. Run the application: `python app.py`
7. Access the application in your web browser at `http://localhost:5000`

## Usage
1. Enter a Twitter username or hashtag in the provided input fields.
2. Click the "Search" button to retrieve and analyze the data.
3. View the generated insights and reports on the app's user interface.


## Acknowledgements
- [OpenAI](https://openai.com/) for providing the GPT API.
- [Bootstrap](https://getbootstrap.com/) for the responsive design and UI components.
- [snscrape](https://github.com/JustAnotherArchivist/snscrape) for the Twitter scraping library.