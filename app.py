from flask import Flask, request, render_template
import snscraper  # replace this with the name of your Python file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form.get('search-input')
    if snscraper.check_hashtag(user_input): 
        result = snscraper.scrape_tweets_by_hashtag(user_input) 
    else: 
        result = snscraper.user_info(user_input)
    return render_template('result.html', result=result)  

if __name__ == '__main__':
    app.run(debug=True)
