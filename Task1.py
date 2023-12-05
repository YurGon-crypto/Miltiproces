import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def check_prime_with_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return results


def check_prime_with_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return results


if __name__ == "__main__":
    print("Using ThreadPoolExecutor:")
    results_threadpool = check_prime_with_threadpool(NUMBERS)
    print(results_threadpool)

    print("\nUsing ProcessPoolExecutor:")
    results_processpool = check_prime_with_processpool(NUMBERS)
    print(results_processpool)
