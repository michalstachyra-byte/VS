import re
import unicodedata
from collections import Counter


def is_palindrome(text: str) -> bool:
    cleaned = "".join(
        c.lower() for c in text if not c.isspace()
    )
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    if n in (0, 1):
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęóAEIOUYĄĘÓ"
    return sum(1 for c in text if c in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def word_frequencies(text: str) -> dict:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    return dict(Counter(words))


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
