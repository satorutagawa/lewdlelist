import string

import web_api

def output_lewd_words(filename: str):
    alphabet_list = list(string.ascii_lowercase)

    with open(filename, "w") as f:
        for letter1 in alphabet_list:
            for letter2 in alphabet_list:
                for letter3 in alphabet_list:
                    for letter4 in alphabet_list:
                        for letter5 in alphabet_list:
                            search_word = f"{letter1}{letter2}{letter3}{letter4}{letter5}"
                            if web_api.is_lewd_word(search_word):
                                f.write(f"{search_word}\n")

def main():
    output_lewd_words("lewd_words.txt")

if __name__ == "__main__":
    main()
