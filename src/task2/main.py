from re import split
from typing import Iterator, Callable

def generator_numbers(text: str) -> Iterator[float]:
    """
    Returns generator of all real numbers found in `text`

    :param text: input text to parse
    :return: generator of real numbers in the input
    """

    # split text into word by whitespace sequences
    for word in split(r'\s+', text):
        try:
            # try parsing word into float
            result = float(word)

            yield result
        except ValueError:
            # if we couldn't parse the word, we skip it
            pass

def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """
    Sums up real numbers generated from `text` by `func`.

    :param text: input text to parse
    :param func: parser function to generate real numbers from `text`
    :return: sum of all generated numbers
    """
    return sum(func(text))
