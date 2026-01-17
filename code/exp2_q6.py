def read_numbers_from_file(filename):
    try:
        with open(filename, "r") as f:
            numbers = []
            for line in f:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
            return numbers
    except FileNotFoundError:
        print("Error: File not found.")
        return []

# Usage example (make sure numbers.txt exists in the same folder)
filename = "numbers.txt"
numbers = read_numbers_from_file(filename)
print("Numbers read from file:", numbers)