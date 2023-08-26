# Functions and Modules in Python

## Overview
This module explores the essential concepts of defining and using functions, creating and importing custom modules, and working with data structures like lists, tuples, and dictionaries.

## Table of Contents
1. [Creating and Calling Functions](#creating-and-calling-functions)
   - Introduction to Functions
   - Defining and Calling Functions
   - Scope and Lifetime of Variables
2. [Importing Modules](#importing-modules)
   - Introduction to Modules
   - Creating a Custom Module
   - Importing Functions from a Module
3. [Working with Data: Lists, Tuples, and Dictionaries](#working-with-data-lists-tuples-and-dictionaries)
   - Understanding Lists, Tuples, and Dictionaries
   - Hands-on Exercise: Student Gradebook
4. [Conclusion and Transition](#conclusion-and-transition)
   - Summary
   - Next Steps and Resources

### Creating and Calling Functions

#### Introduction to Functions
- **Why Use Functions?** Functions allow code reusability and modularity, making programs more organized and manageable.
- **Defining and Calling Functions**: Functions encapsulate specific tasks and can be called by name.
- **Scope and Lifetime of Variables**: Understanding local and global variables.

**Example Code:**
```python
def greet(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")
message = greet(name)
print(message)

Importing Modules
Introduction to Modules
What Are Modules, and Why Use Them? Modules are files containing Python code, usually defining functions, variables, or classes.
Creating a Custom Module: Organizing related code into separate files.
Importing Functions from a Module: Using import to access code across files.
Example Code:

python
Copy code
# math_operations.py
def add(x, y): return x + y

# main.py
import math_operations
print("Addition:", math_operations.add(10, 5))
Working with Data: Lists, Tuples, and Dictionaries
Understanding Lists, Tuples, and Dictionaries
Lists: Ordered collections that can be indexed and modified.
Tuples: Immutable sequences.
Dictionaries: Collections of key-value pairs.
Hands-on Exercise: Student Gradebook

python
Copy code
students = [{"name": "Alice", "grade": 90}, {"name": "Bob", "grade": 85}]
Conclusion and Transition
Summary: This module provides foundational knowledge of functions, modules, and data structures in Python.
Next Steps and Resources: Continue to explore and apply these concepts in real-world scenarios.