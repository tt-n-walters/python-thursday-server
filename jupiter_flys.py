from random import seed, choice, randint
from string import ascii_letters, digits

def generate_seed(input: str) -> int:
    seed(input)
    numbers = []
    for _ in input:
        n = randint(0, 100)
        padded = "{:03}".format(n)
        numbers.append(padded)
    joined = "".join(numbers)
    return int(joined)

def jupiter_flys(_seed: int, input: str) -> str:
    seed(_seed)
    letters = []
    for _ in range(100):
        letters.append(choice(ascii_letters + digits))
    joined = "".join(letters)
    return joined
