from flask import Flask, request, jsonify, render_template
from functionality import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# data structure to track guesses
# items are {}

past_guesses = {}

@app.route('/guess', methods=['POST'])
def guess_word():

    data = request.get_json()
    curr_guess = data.get('word')
    print("guess recieved:", curr_guess)
    if curr_guess in past_guesses:
        print("already guessed")
        message = "already guessed"
        curr_score = past_guesses[curr_guess]
    elif not is_valid_word(curr_guess):
        print("this word isnt counted")
        message = "im not sure that is a word"
        curr_score = "none"
    else:
        message, curr_score = guess(curr_guess)
        past_guesses[curr_guess] = curr_score

    return jsonify({
        "message": message,
        "score": curr_score,
        "data": guesses_info
        })

@app.route('/')
def home():
    return render_template('index.html')

# for local testing
"""
if __name__ == '__main__':
    app.run(debug=True, port=8080)
    """