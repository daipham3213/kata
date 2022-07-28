path = "wordlist.txt"
anagrams_path = "result.txt"


def load_words() -> list[str]:
    with open(path, "r") as file:
        return list(file.readlines())


def build_anagrams_list(word_list: list[str], case_sensitive=False) -> list[list[str]]:
    wdict = {}
    for word in word_list:
        word = word.replace("\n", "").strip()
        if not case_sensitive:
            word = word.lower()
        if len(word) < 2:
            continue
        chars = "".join(sorted([c for c in word]))
        if not wdict.get(chars, None):
            wdict[chars] = []
        wdict[chars].append(word)
    result = []
    for arr in wdict.values():
        arr = list(set(arr))
        if len(arr) > 1:
            result.append(arr)
    return result


def anagrams(case_sensitive=False) -> list[list[str]]:
    word_list = load_words()
    return build_anagrams_list(word_list, case_sensitive)
