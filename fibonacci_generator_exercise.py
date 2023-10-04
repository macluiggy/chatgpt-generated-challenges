
# Exercise: Generate Fibonacci Sequence Up To N
# Create a generator function that yields the Fibonacci sequence up to a given number N.
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

from typing import Generator

def fibonacci_up_to_n(N: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

def test_fibonacci_up_to_n():
    assert list(fibonacci_up_to_n(0)) == [0]
    assert list(fibonacci_up_to_n(1)) == [0, 1, 1]
    assert list(fibonacci_up_to_n(2)) == [0, 1, 1, 2]
    assert list(fibonacci_up_to_n(3)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_up_to_n(5)) == [0, 1, 1, 2, 3, 5]
    assert list(fibonacci_up_to_n(8)) == [0, 1, 1, 2, 3, 5, 8]
    
# Test the generator function
if __name__ == "__main__":
    # N = 50
    # print(f"Fibonacci numbers up to {N}:")
    # for num in fibonacci_up_to_n(N):
    #     print(num)
    test_fibonacci_up_to_n()
