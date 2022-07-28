import sys

path = "wordlist.txt"


def load_words(case_sensitive=False, word_length_limit=6):
    words_to_split = {}
    words_to_compare = {}
    with open(path, "r") as file:
        for line in file:
            line = line.replace("\n", "").strip()
            length = len(line)
            if length < 2:
                continue
            if not case_sensitive:
                line = line.lower()
            if length == word_length_limit:
                words_to_split[line] = True
            elif length < word_length_limit:
                words_to_compare[line] = True
    return words_to_split, words_to_compare


def conflicting_objectives(case_sensitive=False, word_length_limit=6):
    word_list, dictionary = load_words(case_sensitive, word_length_limit)
    result = []
    for key in word_list.keys():
        for i in range(2, len(key) - 1):
            head = key[:i]
            tail = key[i:]
            if head in dictionary and tail in dictionary:
                result.append([key, head, tail])
    return result


def main():
    print(conflicting_objectives(True))


if __name__ == "__main__":
    sys.exit(main())
