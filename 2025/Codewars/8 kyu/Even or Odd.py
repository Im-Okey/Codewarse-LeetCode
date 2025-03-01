"""Create a function that takes an integer as an argument and returns
"Even" for even numbers or "Odd" for odd numbers."""



def even_or_odd(number: int) -> str:
    return 'Even' if number % 2 == 0 else 'Odd'


assert even_or_odd(2) == 'Even'
assert even_or_odd(-1) == 'Odd'
assert even_or_odd(1) == 'Odd'
assert even_or_odd(-2) == 'Even'
assert even_or_odd(0) == 'Even'
