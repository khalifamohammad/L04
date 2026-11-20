# Bug reports for exercise2.py

Line: 2
Problem: The docstring says "5 or more", which includes 5, but the code uses > 5, making it False for grade = 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring says "at least 8 characters", which means 8 or more, but the code uses > 8, making it False for passwords of length 8.
Example: is_valid_password("12345678") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The function is supposed to limit x to the range from low to high, but the code returns max(low, min(x, low)), which incorrectly uses low twice and will always return low if x is below or equal to low. It should use min and max properly to clamp between low and high.
Example: clamp(10, 5, 15) returns 10, which is correct, but clamp(3, 5, 10) returns 5, which is correct; however, clamp(2, 5, 10) returns 5, which is correct, but the logic is flawed because min(x, low) is min(x, low), and then max(low, ...) makes it always at least low, but if x < low, min(x, low) = x, then max(low, x) = low — that's correct. But if x > high, min(x, low) = low, then max(low, low) = low — wrong. It should be max(low, min(x, high)). The current code has a bug: it uses low instead of high in the min.
Example: clamp(100, 1, 10) returns 10, expected 10; but clamp(2, 1, 10) returns 1, correct; clamp(15, 1, 10) returns 10, correct; but clamp(5, 1, 10) returns 5, correct. The bug is in the logic: it says min(x, low), but should be min(x, high). So when x is greater than high, it should cap at high, not at low.
Example: clamp(15, 1, 10) returns 10, which is correct, but the code uses min(x, low) which is min(15,1)=1, then max(low,1)=1 — wrong. Should be max(low, min(x, high)).
Fix: return max(low, min(x, high))
