import random
import numpy as np
from vector_utils import *


guesses_info = []

print("loading words...")
with open('word_vecs.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    word_vecs = {}
    for line in f:
        tokens = line.rstrip().split(' ')
        word_vecs[tokens[0]] = np.array(list(map(float, tokens[1:])))

print("for now we wont pick a random word, well just use hammer")
"""
print("picking random word...")
with open('nouns.txt', encoding='utf-8', newline='\n', errors='ignore') as f:
    words = []
    for line in f:
        words.append(line.strip())
word = random.choice(words)
"""
word = "hammer"


top_ten = most_similar_words(word_vecs, 10, word)
print("The most similar word has similarity: " + str(top_ten[0][1]))
print("The 10th most similar word has similarity: " + str(top_ten[9][1]))
print("")
"""
while True:
    guess = input("> ").strip()
    if guess in word_vecs.keys():
        if guess == word:
            print("You win!")
            exit()
        print(similarity(word_vecs, guess, word))
    elif guess == ":q":
        print("Giving up? It was " + word)
        exit()
    elif guess == ":h":
        print("The 10th closest word is: " + top_ten[9][0])
    else:
        print("I don't know that word")
"""

def guess(guess):
    if guess in word_vecs.keys():
        guesses_info.append({"guess": guess, "similarity": similarity(word_vecs, guess, word)})
        guesses_info.sort(key=lambda x: x['similarity'], reverse=True)

        if guess == word:
            return "You got it!"
            

        print(similarity(word_vecs, guess, word))
        return "decent guess"
    else:
        return "I'm not sure thats a word"

