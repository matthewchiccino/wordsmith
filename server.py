from flask import Flask, request, jsonify, render_template
from functionality import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# data structure to track guesses
# items are {}

words_guessed = []

@app.route('/guess', methods=['POST'])
def guess_word():

    data = request.get_json()
    curr_guess = data.get('word')
    print("I GOT A WORD LFG, ITS", curr_guess)
    if curr_guess in words_guessed:
        message = "already guessed"
    else:
        words_guessed.append(curr_guess)
        message = guess(curr_guess)
    print("we made it past the new stuff i guess?")

    return jsonify({
        "message": message,
        "data": guesses_info
        })

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)