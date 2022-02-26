import pdb

from collections import Counter
from collections import defaultdict

def read_words(fname: str="lewd_words.txt") -> list:
    words = []

    with open(fname, 'r') as fp:
        for line in fp:
            if line[0] != '"':
                continue

            word = line.split('"')[1].lower()
            words.append(word)

    return words

def find_most_common_letter(words: list):
    letter_counter = Counter()

    for word in words:
        letter_counter.update(word)

    print("5 most common letters")
    for letter, count in letter_counter.most_common(5):
        print(letter, count)
    
    print("")
    print("Vowels count")
    for vowel in ["a","e","i","o","u"]:
        print(vowel, letter_counter[vowel])
    print("")

def find_word_with_most_vowels(words: list):

    words_by_unique_vowel_cnt = defaultdict(list)
    max_vowels = 0

    for word in words:
        letter_counter = Counter()
        letter_counter.update(word)

        unique_vowels_cnt = 0
        for vowel in ["a","e","i","o","u"]:
            if vowel in letter_counter:
                unique_vowels_cnt += 1

        words_by_unique_vowel_cnt[unique_vowels_cnt].append(word)
        if max_vowels < unique_vowels_cnt:
            max_vowels = unique_vowels_cnt

    for i in range(max_vowels,1,-1):
        print(f"Word(s) with {i} unique vowels:")
        print(words_by_unique_vowel_cnt[i])
        print("")

def main():
    words = read_words()

    find_most_common_letter(words)

    find_word_with_most_vowels(words)

if __name__ == "__main__":
    main()
