
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.remove(25)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Element at index 2:", numbers[2])
print("Slicing [1:4]:", numbers[1:4])
