import random
import numpy as np
from vector_utils import *

guesses_info = []

print("loading words...")
# Load word vectors (lots)

with open('final_word_vecs_100d.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    word_vecs = {}
    for line in f:
        tokens = line.rstrip().split(' ')
        word_vecs[tokens[0]] = np.array(list(map(float, tokens[1:])))

print("picking random word...")
# Load words (short custom answer list)
with open('words.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    words = []
    for line in f:
        words.append(line.strip())
word = random.choice(words)

similarities = most_similar_words(word_vecs, word)


# Get the top similar words
similarities = most_similar_words(word_vecs, word)
top_ten = similarities[:10]

print(f"The most similar word has similarity: {top_ten[0][1]}")
print(f"The 10th most similar word has similarity: {top_ten[9][1]}")

def is_valid_word(w):
    return w in word_vecs

def guess(guess_word):
    
    # Calculate the similarity score
    guess_float_score = similarity(word_vecs, guess_word, word)
    int_score = find_word_index(guess_word, guess_float_score, similarities)

    # Store guess info and sort by similarity
    guesses_info.append({"guess": guess_word, "similarity": int_score})
    guesses_info.sort(key=lambda x: x['similarity'])

    print("SCORE:", int_score)
        
    if guess_word == word:
        return "You got it!", int_score
        
    print(similarity(word_vecs, guess_word, word))
    return "Decent guess", int_score

