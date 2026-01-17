
print("Name: PRANAV DIXIT")
print("SAP ID: 590014418")
print("----------------------------------")

def basic_arithmetic():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

def type_conversion():
    x = 10
    print("Integer:", x, type(x))
    y = float(x)
    print("Float:", y, type(y))
    s = str(y)
    print("String:", s, type(s))
    z = int(float(s))
    print("Back to Integer:", z, type(z))
    b = bool(z)
    print("Boolean:", b, type(b))

def list_operations():
    numbers = [5, 2, 9, 1]
    numbers.append(7)
    print("Append:", numbers)
    numbers.insert(2, 10)
    print("Insert:", numbers)
    numbers.pop()
    print("Pop:", numbers)
    numbers.remove(2)
    print("Remove:", numbers)
    numbers.sort()
    print("Sort:", numbers)
    numbers.reverse()
    print("Reverse:", numbers)
    print("Index 0:", numbers[0])
    print("First 3 elements:", numbers[:3])

def tuple_demo():
    tup = (1, 2, 3, 4)
    print("Tuple:", tup)
    print("Element at index 2:", tup[2])
    try:
        tup[1] = 99
    except TypeError as e:
        print("Error (immutability):", e)

def dictionary_operations():
    student = {"name": "Ravi", "age": 20}
    student["age"] = 21
    student["course"] = "BSc Chemistry"
    for k, v in student.items():
        print(k, ":", v)

def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference:", set1 - set2)

def extras():
    text = input("Enter a string: ").lower()
    vowels = "aeiou"
    count = sum(1 for ch in text if ch in vowels)
    print("Vowel count:", count)

    n = int(input("Enter a number to check prime: "))
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
        print("Not prime")

    num = int(input("Enter number for factorial: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial (loop):", fact)

    def fact_rec(x):
        if x == 0:
            return 1
        return x * fact_rec(x - 1)

    print("Factorial (recursion):", fact_rec(num))

def greet_function():
    def greet(name, age):
        return "Hello " + name + ", you are " + str(age) + " years old."
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(greet(name, age))


while True:
    print("\n--- MENU ---")
    print("1. Basic Arithmetic")
    print("2. Type Conversion")
    print("3. List Operations")
    print("4. Tuple Demo")
    print("5. Dictionary Operations")
    print("6. Set Operations")
    print("7. Extras (Vowels, Prime, Factorial)")
    print("8. Greet Function")
    print("9. Exit")

    ch = input("Enter choice (1-9): ")

    if ch == "1":
        basic_arithmetic()
    elif ch == "2":
        type_conversion()
    elif ch == "3":
        list_operations()
    elif ch == "4":
        tuple_demo()
    elif ch == "5":
        dictionary_operations()
    elif ch == "6":
        set_operations()
    elif ch == "7":
        extras()
    elif ch == "8":
        greet_function()
    elif ch == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
