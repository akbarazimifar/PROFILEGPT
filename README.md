# OSINTGPT
OSINTGPT is a tool for analyzing profiles and hashtags on Twitter. The application exploits various technologies and APIs to collect data and generate information for users.

# [Your App Name]

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Introduction
[Your App Name] is a web application designed to provide users with powerful features for analyzing social media profiles and hashtags. The app leverages various technologies and APIs to gather data and generate valuable insights for users.

## Features
- **Profile Analysis**: Users can enter a Twitter username to retrieve information about the user's profile, including description, creation date, display name, location, followers count, friends count, and favorites count. The app uses the Twitter API and scraping techniques to collect the data.
- **Hashtag Analysis**: Users can input a hashtag to scrape and analyze tweets related to that hashtag. The app retrieves a specified number of recent tweets, performs sentiment analysis, generates word clouds, and provides insights into the content, context, language used, sentiment, possible hidden meanings, and potential network of interactions based on replies, likes, and retweets. OpenAI's GPT API is utilized for analyzing the tweets.
- **Open Source Intelligence (OSINT)**: The app acts as a digital forensics expert with a specialization in OSINT. It offers detailed insights about hashtags, probable geographic locations, social networks, possible intentions, and any potential security threats or vulnerabilities that might be revealed. It suggests further data points and OSINT avenues worth exploring.

## Technologies Used
- Python
- Flask
- HTML/CSS
- Bootstrap
- Twitter API
- snscrape
- WordCloud
- OpenAI GPT API

## Getting Started
1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your Twitter API credentials by following the instructions in the [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
4. Set up your OpenAI GPT API credentials by signing up for an API key on the [OpenAI website](https://openai.com/).
5. Create a `.env` file in the root directory and add your API credentials in the following format:



6. Run the application: `python app.py`
7. Access the application in your web browser at `http://localhost:5000`

## Usage
1. Enter a Twitter username or hashtag in the provided input fields.
2. Click the "Search" button to retrieve and analyze the data.
3. View the generated insights and reports on the app's user interface.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [OpenAI](https://openai.com/) for providing the GPT API.
- [Bootstrap](https://getbootstrap.com/) for the responsive design and UI components.
- [snscrape](https://github.com/JustAnotherArchivist/snscrape) for the Twitter scraping library.
- [WordCloud](https://github.com/amueller/word_cloud) for generating word clouds.

## Contributing
Contributions to [Your App Name] are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) for more information.
