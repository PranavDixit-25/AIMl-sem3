
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in string if ch in vowels)
print("Number of vowels:", count)


n = int(input("Enter integer: "))

isprime = True

for i in range(2, n):
    if n % i == 0:
        isprime = False
        break

if isprime:
    print("Integer is prime")
else:
    print("Integer is not prime")


n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial using loop:", fact)

# Factorial using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print("Factorial using recursion:", factorial(n))
