def find_words(file_name, predicate):
    words = []
    with open(file_name) as f:
        for word in f:
            word = normalize(word)
            if predicate(word):
                words.append(word)
    return words


def accepted_words(letters: list, must_have: list, word: str):
    word = word.lower()
    word = word.strip().strip('.-')

    for l in word:
        if l not in letters:
            return False
    for m in must_have:
        if word.count(m) < 2:
            return False
    return True


def normalize(word):
    word = word.lower()
    word = word.strip().strip('.-')
    return word

