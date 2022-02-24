import string
import logging
import pdb
from collections import Counter

import web_api_local as web_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def is_valid_word(word: str):
    if Counter(word).most_common(1)[0][1] > 2:
        return False
    else:
        return True

def is_lewd_word(word: str):
    entries = web_api.define(word)

    if len(entries) < 3:
        return False

    cnt_neighbor = 0
    for elem in entries:
        if elem["word"].find(' ')==-1 and elem["word"].lower() != word:
            if not (word[-1] == 's' and elem["word"].lower()[0:4] == word[0:4]):
                cnt_neighbor += 1

    if float(cnt_neighbor) / float(len(entries)) > 0.5:
        return False
    else:
        return True

def output_lewd_words(filename: str):

    alphabet_list = list(string.ascii_lowercase)

    word_cnt = 0
    with open(filename, "w") as f:
        for letter1 in alphabet_list:
            for letter2 in alphabet_list:
                for letter3 in alphabet_list:
                    print(f"{letter1}{letter2}{letter3} {word_cnt}")
                    f.flush()
                    for letter4 in alphabet_list:
                        for letter5 in alphabet_list:
                            search_word = f"{letter1}{letter2}{letter3}{letter4}{letter5}"
                            if is_valid_word(search_word) and is_lewd_word(search_word):
                                f.write(f"{search_word}\n")
                                print(f"{search_word}")
                                word_cnt += 1

def main():
    output_lewd_words("lewd_words.txt")

if __name__ == "__main__":
    main()
