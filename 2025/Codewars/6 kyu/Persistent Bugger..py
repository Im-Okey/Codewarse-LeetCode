"""Write a function, persistence, that takes
   in a positive parameter num and returns its multiplicative persistence,
   which is the number of times you must multiply the digits in num until
   you reach a single digit.

For example (Input --> Output):

 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit,
 there are 3 multiplications)
 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and
 finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)"""
import functools


def persistence(n: int, count: int = 0) -> int:
        return count if n < 9 else persistence(functools.reduce(lambda a, b: a * b, list(map(int, [i for i in str(n)]))), count + 1)


assert persistence(39) == 3
assert persistence(4) == 0
assert persistence(25) == 2
assert persistence(999) == 4