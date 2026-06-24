
# This is a placeholder for AI experiments
print("Hello AI! This is my first AI script.")

### Description

# In several Python examples within the project, loops can manually track indexes using counters.
# However, Python provides a built-in function `enumerate()` that simplifies this pattern and improves readability.

### Current pattern

items = ["apple", "banana", "cherry"]

### Improved pattern using enumerate()

# Using enumerate() to get both index and value in a loop
# The enumerate() function returns an enumerate object, which is an iterator that produces tuples containing a count (from start which defaults to 0) and the values obtained from iterating over the sequence.
for index, item in enumerate(items, start=1):  # default start is 0, but we're making it explicit for clarity
    print(f"Index: {index}, Value: {item}")
