def find_words(f, predicate):
    words = []
    for word in f:
        word = normalize(word)
        if predicate(word):
            words.append(word)
    return words


def accepted_words(
    letters: list, must_have: list, must_have_count: int, _or: bool, word: str
):
    for l in word:
        if l not in letters:
            return False
    result = not _or
    for m in must_have:
        if _or:
            result = result or word.count(m) >= must_have_count
        else:
            result = result and word.count(m) >= must_have_count
    return result


def normalize(word):
    word = word.lower()
    word = word.strip().strip(".-")
    return word
