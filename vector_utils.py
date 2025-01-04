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
        sim = similarity(word_vecs, word, w)
        similarities.append((w, sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities


def find_word_index(word, float_score, similarities):
    # Extract the list of similarity scores
    just_sims = [score for _, score in similarities]
    # Ensure the list is sorted in ascending order for bisect_left
    just_sims.sort()  # Sort in ascending order
    # Find the index using bisect_left
    index = bisect.bisect_left(just_sims, float_score)
    return len(just_sims) - index - 1