import random
import numpy as np
from vector_utils import *

print("loading words...")
# Load word vectors (once, not on every request)
with open('final_word_vecs_100d.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    word_vecs = {}
    for line in f:
        tokens = line.rstrip().split(' ')
        word_vecs[tokens[0]] = np.array(list(map(float, tokens[1:])))

# Function to initialize game state for a new session
def initialize_game():

    # Load words (short custom answer list)
    with open('words.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
        words = []
        for line in f:
            words.append(line.strip())
        
    # Pick a random word for the current session
    word = random.choice(words)
    # for testing
    #word = "computer"

    # Get the top similar words
    similarities = most_similar_words(word_vecs, word)
    # Print the top 10 most similar words
    #for i, (similar_word, similarity) in enumerate(similarities[:25]):
        #print(f"{i + 1}. {similar_word} with similarity: {similarity}")

    return word, similarities  # Return initial game state

def is_valid_word(w, word_vecs):
    return w in word_vecs

def get_hint(similarities, guesses_info):
    if not guesses_info:
        return similarities[201]
    
    highest_guess = guesses_info[0]['similarity']

    if highest_guess == 1:
        length = len(guesses_info)
        # edge case if the hint needs to be the worst guess yet
        if guesses_info[-1]['similarity'] == length:
            return similarities[length+1]
        
        # else find the highest index that hasnt been guessed yet
        p1 = 1
        p2 = 1
        while p2 == p1:
            p2+=1
            p2 = guesses_info[p2-1]['similarity']
            p1+=1
            
        return similarities[p1]

    else:
        return similarities[highest_guess // 2]


def guess(guess_word, word, similarities, guesses_info, word_vecs):
    # Calculate the similarity score
    guess_float_score = similarity(word_vecs, guess_word, word)
    int_score = find_word_index(guess_word, guess_float_score, similarities)

    # Store guess info and sort by similarity
    guesses_info.append({"guess": guess_word, "similarity": int_score})
    guesses_info.sort(key=lambda x: x['similarity'])

    print("SCORE:", int_score)
    
    # Corrected the order of the conditions for more accurate result handling
    if guess_word == word:
        return "You got it!", int_score, guesses_info
    elif int_score <= 15:
        return "almost there!", int_score, guesses_info
    elif int_score <= 20:
        return "good guess!", int_score, guesses_info
    elif int_score <= 100:
        return "getting close...", int_score, guesses_info
    elif int_score >= 10000:
        return "not so close", int_score, guesses_info
    else:
        return "Decent guess", int_score, guesses_info
