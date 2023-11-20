"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
# Author: ChatGPT


def greeting():
    """
    This function prints 'Hello World' on one line and returns the docstring.
    Example:
    greeting()  # Output: Hello World!
    """
    print("Hello World!")
    return greeting.__doc__


greeting()


# Test Cases
# Test Case 1: Call the function and verify the output is 'Hello World!'
greeting()  # Output: Hello World!


# Test Case 2: Call the function again to demonstrate the reusability of the greeting function
greeting()  # Output: Hello World!


# Test Case 3: Assign the docstring to a variable and print it separately
docstring_var = greeting.__doc__
print(docstring_var)  # Output: This function prints 'Hello World' on one line and returns the docstring.


# Test Case 4: Call the function without printing to observe the behavior of not using the returned docstring
greeting()

