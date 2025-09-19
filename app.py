from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Function to get sentiment of text
def get_sentiment(text):
    '''Return sentiment of the text using TextBlob'''
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    
    if request.method == "POST":
        text_input = request.form['text']
        sentiment_result = get_sentiment(text_input)
        
    return render_template('index.html', sentiment_result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)
