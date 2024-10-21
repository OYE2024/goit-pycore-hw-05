from re import findall
from typing import Generator, Callable

text = """
Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""


def generator_numbers(string: str) -> Generator:
    """
    Функція generator_numbers аналізує текст, ідентифікує всі дійсні числа,
    що вважаються частинами доходів, і повертає їх як генератор.
    """
    patern = r"\b\d*\.?\d+\b"
    numbers = findall(patern, string)
    for num in numbers:
        yield float(num)


def sum_profit(string: str, func: Callable):
    """
    Функція sum_profit використовує generator_numbers для підсумовування
    цих чисел і обчислення загального прибутку.
    """
    return sum(func(string))


print(sum_profit(text, generator_numbers))
