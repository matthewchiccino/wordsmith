import numpy as np

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
def most_similar_words(word_vecs, n, word):

    similarities = []

    # Loop over all words in word_vecs
    for w in word_vecs:
        sim = similarity(word_vecs, word, w)
        similarities.append((w, sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(10):
        print("#", str(i), ": ", similarities[i])


    return similarities[1:n+1]