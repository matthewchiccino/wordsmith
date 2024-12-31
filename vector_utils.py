import numpy as np
import bisect

def similarity(word_vecs, w1, w2):
    # Determines the similarity of two words
    # The cosine similarity of the vectors in `word_vecs` representing
    # the words `w1` and `w2`

    v1 = word_vecs[w1]
    v2 = word_vecs[w2]

    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    cosine_sim = np.dot(v1/norm_v1, v2/norm_v2)

    return cosine_sim

#Determines the closest words to a given word
def most_similar_words(word_vecs, word):

    similarities = []

    # Loop over all words in word_vecs
    for w in word_vecs:
        sim = round(similarity(word_vecs, word, w), 5)
        similarities.append((w, sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    print(similarities[:35])
    
    return similarities


def find_word_index(word, float_score, similarities):
    # Extract the list of just the similarity scores
    just_sims = [score for _, score in similarities]
    
    # Use bisect_left to find the correct index where float_score would fit
    rounded_score = round(float_score, 9)
    print("float score:", rounded_score)
    print(just_sims[:10])
    just_sims = just_sims[::-1]
    index = bisect.bisect_left(just_sims, rounded_score)
    print("index of ", index)
    return 400000 - index - 1