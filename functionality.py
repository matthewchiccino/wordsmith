import random
import bisect
import numpy as np
from vector_utils import *


guesses_info = []

print("loading words...")
with open('word_vecs.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    word_vecs = {}
    for line in f:
        tokens = line.rstrip().split(' ')
        word_vecs[tokens[0]] = np.array(list(map(float, tokens[1:])))

print("for now we wont pick a random word, well just use computer")
"""
print("picking random word...")
with open('nouns.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    words = []
    for line in f:
        words.append(line.strip())
word = random.choice(words)
"""
word = "computer"
similarities = most_similar_words(word_vecs, word)


top_ten = most_similar_words(word_vecs, word)
print("The most similar word has similarity: " + str(top_ten[0][1]))
print("The 10th most similar word has similarity: " + str(top_ten[9][1]))


def guess(guess):
    if guess in word_vecs.keys():
        guess_float_score = similarity(word_vecs, guess, word)
        guesses_info.append({"guess": guess, "similarity": find_word_index(guess, guess_float_score, similarities)})
        guesses_info.sort(key=lambda x: x['similarity'])

        int_score = find_word_index(guess, guess_float_score, similarities)
        print("SCORE:", int_score)

        if guess == word:
            return "You got it!"
            

        print(similarity(word_vecs, guess, word))
        return "decent guess"
    else:
        return "I'm not sure thats a word"

