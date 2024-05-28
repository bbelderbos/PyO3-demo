import time

from sum_squares import sum_of_squares


def sum_of_squares_py(n):
    return sum(x * x for x in range(1, n + 1))


if __name__ == "__main__":
    n = 10**6

    start_time = time.time()
    result = sum_of_squares_py(n)
    end_time = time.time()
    print(f"Python result: {result}")
    print(f"Python execution time: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    result = sum_of_squares(n)
    end_time = time.time()
    print(f"Rust result: {result}")
    print(f"Rust execution time: {end_time - start_time:.6f} seconds")

