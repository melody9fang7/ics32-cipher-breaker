#Melody Fang
#mkfang@uci.edu
#37001380
import nltk
from nltk.corpus import words

en_word_set = set(words.words())


def findpercentage(file1):
    total_words = 0
    valid_words = 0

    with open(file1, "r") as ofile:
        for line in ofile:
            words = line.split("_")
            for w in words:
                w_ = ''.join(a for a in w if a.isalpha())
                if w_.lower() in en_word_set:
                    valid_words += 1
                total_words += 1

    if total_words != 0:
        return valid_words / total_words