from collections import Counter

import click


def find_combinations(file, length) -> Counter:
    combinations = Counter()
    for word in file:
        word = word.strip().strip(".-")
        for i in range(len(word) - length + 1):
            combinations[word[i : i + length]] += 1
    return combinations


def find_combinations_from_beginning(file, length) -> Counter:
    combinations = Counter()
    for word in file:
        word = word.strip().strip(".-")
        combinations[word[:length]] += 1
    return combinations


@click.command()
@click.argument("dictionary", type=click.File())
@click.option("--length", "-l", default=2, help="length of the combinations")
@click.option("--top", "-t", default=5, help="number of the most common combinations")
@click.option(
    "--beginning",
    "-b",
    is_flag=True,
    default=False,
    help="show only combinations from the beginning of the word",
)
def report_combinations(dictionary, length, top, beginning):
    if beginning:
        combinations = find_combinations_from_beginning(dictionary, length)
    else:
        combinations = find_combinations(dictionary, length)
    for combination, count in combinations.most_common(top):
        print(f"{combination}: {count}")


if __name__ == "__main__":
    report_combinations()
