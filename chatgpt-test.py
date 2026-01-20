"""
Python Tip: Using enumerate() for index and value in loops
"""

print("Hello AI! This is my first AI script.\n")

# Example list
items = ['apple', 'banana', 'cherry']

print("Without enumerate():")
for i in range(len(items)):
    print(i, items[i])

print("\n Using enumerate():")
for index, item in enumerate(items):
    print(index, item)

print("\n Using enumerate() starting from 1:")
for index, item in enumerate(items, start=1):
    print(index, item)

# enumerate() makes code cleaner and more readable
