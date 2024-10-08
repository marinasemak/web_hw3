import time
from multiprocessing import Pool, cpu_count, current_process
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorized_list(number):
    logger.debug(f"pid={current_process().pid}, number={number}")
    return [i for i in range(1, number + 1, 1) if number % i == 0]


def factorize(*number):
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(factorized_list, number)
    return result


if __name__ == "__main__":
    start = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end = time.time()
    print(end - start)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
