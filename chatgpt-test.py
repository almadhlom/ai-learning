# This is a placeholder for AI experiments
print("Hello AI! This is my first AI script.")

### Description

# In several Python examples within the project, loops manually track indexes using counters.  
# Python provides a built-in function `enumerate()` that simplifies this pattern and improves readability.

### Current pattern

items = ['apple', 'banana', 'cherry']

for i, item in enumerate(items):
    print(i, item)