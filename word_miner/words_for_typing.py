def find_words(f, predicate):
    words = []
    for word in f:
        word = normalize(word)
        if predicate(word):
            words.append(word)
    return words


def accepted_words(letters: list, must_have: list, word: str, must_have_count=2):
    for l in word:
        if l not in letters:
            return False
    for m in must_have:
        if word.count(m) < must_have_count:
            return False
    return True


def normalize(word):
    word = word.lower()
    word = word.strip().strip(".-")
    return word
