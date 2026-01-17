
student = {"name": "Pranav", "age": 20, "course": "CSE"}
print("Original dictionary:", student)

# Update
student["age"] = 21
student["grade"] = "A"

print("Updated dictionary:", student)


print("Keys and Values:")
for key, value in student.items():
    print(key, ":", value)
