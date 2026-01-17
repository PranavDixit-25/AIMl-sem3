
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Access elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Demonstrating immutability
try:
    my_tuple[0] = 10
except TypeError:
    print("Tuples are immutable. Cannot modify elements.")
