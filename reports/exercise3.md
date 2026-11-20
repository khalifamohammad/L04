# Bug reports for exercise3.py

Line: 3
Problem: the docstring says "An empty list has average 0", but the code divides by len(numbers), which crashes for an empty list.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: the docstring says "or "" if the text is empty", but text.split()[0] raises IndexError if the text is empty (split returns []).
Example: first_word("") raises IndexError, expected "".
Fix: return text.split()[0] if text.split() else ""

Line: 12
Problem: the docstring says "If total is 0, the result is 0", but the code divides by total, which crashes for total=0.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
