```python
# This is a placeholder for AI experiments
print("Hello AI! This is my first AI script.")

### Description

# In several Python examples within the project, loops manually track indexes using counters.
# Python provides a built-in function `enumerate()` that simplifies this pattern and improves readability.

### Current pattern

items = ["apple", "banana", "cherry"]

### Improved pattern using enumerate()

# Using enumerate() to get both index and value in a loop
for index, item in enumerate(items):
    print(f"Index: {index}, Value: {item}")
```

I have improved the documentation by adding a header for the improved pattern and added a comment to explain the usage of `enumerate()`. I have also used an f-string to make the print statement more readable.