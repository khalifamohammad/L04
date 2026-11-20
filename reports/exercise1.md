# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks for odd numbers, but the docstring says "true for even numbers", which is incorrect.
Example: `is_even(4)` returns `False`, expected `True`.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns `width + height`, but the docstring says "area of a rectangle", which should be `width * height`.
Example: `rectangle_area(4, 5)` returns `9`, expected `20`.
Fix: return width * height

Line: 13
Problem: The function adds 2 to `n`, but the docstring says "twice the number n", which means `n * 2`.
Example: `double(3)` returns `5`, expected `6`.
Fix: return n * 2
