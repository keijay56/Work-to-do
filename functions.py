def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]
