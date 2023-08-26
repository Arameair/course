# Introduction to Python Programming

## Overview
This module serves as an introduction to Python programming, covering the fundamental concepts and hands-on exercises, including building a simple calculator.

## Table of Contents
1. [Basics of Python Programming](#basics-of-python-programming)
   - Introduction to Programming and Python
   - Understanding Python Syntax, Variables, Data Types, and Operators
2. [Hands-On Exercise: Simple Calculator](#hands-on-exercise-simple-calculator)
   - Building a Basic Calculator
3. [Preparing for Collaborative Development (GitHub Teaser)](#preparing-for-collaborative-development-github-teaser)
   - Introduction to Version Control and Collaboration
   - Teaser for GitHub Project
4. [Conclusion and Transition](#conclusion-and-transition)
   - Summary
   - Next Steps and Resources

### Basics of Python Programming

#### Introduction to Programming and Python
- **What is Programming?** Programming is the process of writing instructions that a computer can understand and execute.
- **Why Python?** Python is a popular high-level programming language known for its simplicity and readability.

#### Understanding Python Syntax, Variables, Data Types, and Operators
- **Python Syntax**: Python's syntax is designed to be clear and easy to read.
- **Variables**: Variables are used to store values in memory.
- **Data Types**: Python supports various data types, including integers, floats, strings, lists, tuples, and dictionaries.
- **Operators**: Operators perform actions on values and variables, including arithmetic, comparison, and logical operators.

### Hands-On Exercise: Simple Calculator

#### 1. Function Definitions
We'll define four functions to perform the basic arithmetic operations: addition, subtraction, multiplication, and division.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
```

#### 2. User Interface
We'll present the user with options to select the desired operation and input the numbers.

```python
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

#### 3. Conditional Logic
Based on the user's choice, the appropriate function will be called, and the result will be printed.

```python
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
```

#### Full Code
Here's the complete code for the simple calculator:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
```

### Preparing for Collaborative Development (GitHub Teaser)

#### Introduction to Version Control and Collaboration
In the world of software development, collaboration and version control are key components. They enable developers to work together on projects, keep track of changes, and manage different versions of the code. One popular platform for version control and collaboration is GitHub.

#### Teaser for GitHub Project in Module 4
As we progress through this course, we'll be building a project that integrates the concepts and skills learned in each module. In Module 4, we'll take an exciting step by adding our project to GitHub. This will allow us to:
- **Collaborate**: Work with other developers and contributors on the project.
- **Track Changes**: Keep a detailed history of code changes and revisions.
- **Share**: Make the project accessible to others, fostering community engagement and open-source development.

### Conclusion and Transition
This module provides a solid foundation in Python programming. As we move on to the next module, we'll continue to build on these skills, paving the way for more advanced topics and real-world applications. The journey toward collaborative development and open-source contribution has just begun, and there's much more to explore and learn!

Stay tuned, and get ready to dive into the next exciting phase of this course!

