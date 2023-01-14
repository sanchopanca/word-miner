from functools import partial
from random import shuffle

from word_miner.words_for_typing import accepted_words, find_words


def main():
    words = find_words('russian.utf-8',
                       partial(accepted_words,
                               ['а', 'р', 'о', 'л', 'к', 'е', 'н', 'и', 'т'],
                               ['ке', 'ек'],
                               must_have_count=1))
    shuffle(words)
    print(' '.join(filter(lambda w: len(w) <= 15, words)))


if __name__ == '__main__':
    main()
