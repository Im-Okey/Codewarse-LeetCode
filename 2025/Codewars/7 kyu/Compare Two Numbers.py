"""Your function takes two integers, x and y.
 Return the character ">" if x > y, "<" if x < y, or "=" if x == y.

Code limit: < 32 characters."""


f=lambda x,y:'=><'[(x>y)-(x<y)]

assert f(3, 2) == ">"
assert f(2, 3) == "<"
assert f(2, 2) == "="