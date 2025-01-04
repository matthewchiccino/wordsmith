from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from functionality import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files (use Redis for production)
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

@app.route('/')
def home():
    # Initialize new game state for this session
    session['word'], session['similarities'] = initialize_game()
    session['guesses_info'] = []  # Initialize an empty guesses_info list for the session
    print("this is session['guesses_info']:")
    print(session['guesses_info'])
    return render_template('index.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/help.html')
def help():
    return render_template('help.html')

@app.route('/guess', methods=['POST'])
def guess_word():
    print("as soon as i got the request this is session['guesses_info']")
    print(session['guesses_info'])
    data = request.get_json()
    curr_guess = data.get('word')
    print(f"Guess received: {curr_guess}")

    # Retrieve session data
    word = session.get('word')
    similarities = session.get('similarities')
    guesses_info = session.get('guesses_info', [])

    # Check if the guess is valid and process it
    if curr_guess in [g["guess"] for g in guesses_info]:
        print("Already guessed")
        message = "Already guessed"
        curr_score = next(g["similarity"] for g in guesses_info if g["guess"] == curr_guess)
    elif not is_valid_word(curr_guess, word_vecs):
        print("This word isn't valid")
        message = "I'm not sure that's a word"
        curr_score = "none"
    else:
        # Process the guess
        message, curr_score, guesses_info = guess(curr_guess, word, similarities, guesses_info, word_vecs)
        session['guesses_info'] = guesses_info  # Update session with the new guesses info

@app.route('/hint', methods=['GET'])
def hint():
    # Retrieve session data
    word = session.get('word')
    similarities = session.get('similarities')
    guesses_info = session.get('guesses_info', [])\
    
    # (word, index tuple)
    hinted_word = get_hint(similarities, guesses_info)
    print("we got a hinted word of", hinted_word)

    # Process the guess
    message, curr_score, guesses_info = guess(hinted_word[0], word, similarities, guesses_info, word_vecs)
    session['guesses_info'] = guesses_info  # Update session with the new guesses info
    
    return jsonify({
        "message": f"your hint is: {hinted_word[0]}",
        "score": curr_score,
        "data": guesses_info
    })

    return jsonify({
        "message": message,
        "score": curr_score,
        "data": guesses_info
    })

# for local testing
"""
if __name__ == '__main__':
    app.run(debug=True, port=8080)
"""
