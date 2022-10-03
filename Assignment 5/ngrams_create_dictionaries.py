# Tera Parish       txp200011
# Bridgette Bryant  bmb180001

import nltk
import pickle
from nltk import word_tokenize
from nltk import ngrams


def readIn(fileName):
    # open file and read in raw text, using encoding utf-8 to be Windows friendly
    with open(fileName, 'r', encoding="utf-8") as file:
        # remove new line
        raw = file.read().replace('\n', ' ')

    # tokenize into unigrams
    unigrams = word_tokenize(raw)   # Sets the unigrams list

    #print("Unigrams length:", len(unigrams))
    #print("Unigrams:")
    #print(unigrams[:50])

    # Create a bigrams list from the unigrams list using ngrams
    bigrams = list(ngrams(unigrams, 2))

    #print("Bigrams:")
    #print(bigrams[:50])

    # dictionary {word: count} for the unigram and bigram dictionaries
    uni_dict = {u: unigrams.count(u) for u in set(unigrams)}
    bi_dict = {b: bigrams.count(b) for b in set(bigrams)}

    #print("unidict: ", uni_dict)
    #print("bidict: ", bi_dict)


    return uni_dict, bi_dict


if __name__ == '__main__':

    # The files needed to read in
    files = ['LangId.train.English', 'LangId.train.French', 'LangId.train.Italian']
    # The unigram pickles we will create
    uni_pickle = ['uni_English.pickle', 'uni_French.pickle', 'uni_Italian.pickle']
    # The bigram pickles we will create
    bi_pickle = ['bi_English.pickle', 'bi_French.pickle', 'bi_Italian.pickle']

    # counter for pickling
    i = 0

    for name in files:
        #print("i: ", i)
        # read in files
        uni, bi = readIn(name)

        # pickle the dictionaries
        #print("Pickling")
        pickle.dump(uni, open(uni_pickle[i], 'wb'))
        pickle.dump(bi, open(bi_pickle[i], 'wb'))
        # Increment the counter
        i += 1
