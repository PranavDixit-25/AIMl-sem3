class NegativeNumberError(Exception):
    pass

def safe_sqrt(num):
    if num < 0:
        raise NegativeNumberError("Square root of negative number is not allowed!")
    return num ** 0.5

try:
    number = -9
    print("Square root:", safe_sqrt(number))
except NegativeNumberError as e:
    print("Error:", e)