from re import split
from typing import Iterator, Callable

def generator_numbers(text: str) -> Iterator[float]:
    for word in split(r'\s+', text):
        try:
            result = float(word)

            yield result
        except ValueError:
            pass

def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    return sum(func(text))
