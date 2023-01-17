from functools import partial
from random import shuffle

import click

from word_miner.words_for_typing import accepted_words, find_words


@click.command()
@click.argument("dictionary", type=click.File())
@click.option(
    "--allowed",
    help="a set of letters as one string. resulting words will only have letters from this set",
)
@click.option(
    "--must-have",
    multiple=True,
    help="a string representing which letter or combinations of letters must be present",
)
@click.option(
    "--must-have-count",
    default=1,
    help="controls how many times the pattern from --must-have must be present",
)
@click.option(
    "--max-length",
    default=10,
    help="controls the maximum length of the words",
)
@click.option(
    "--or",
    "_or",
    is_flag=True,
    default=False,
    help="if multiple --must-have are passed, this flag controls if all of them must be present in the result words or just one",
)
def typing(dictionary, allowed, must_have, must_have_count, max_length, _or):
    """DICTIONARY is a utf-8 file with words separated by new line"""
    words = find_words(
        dictionary,
        partial(accepted_words, allowed, must_have, must_have_count, _or),
    )
    shuffle(words)
    print(" ".join(filter(lambda w: len(w) <= max_length, words)))


if __name__ == "__main__":
    typing()
