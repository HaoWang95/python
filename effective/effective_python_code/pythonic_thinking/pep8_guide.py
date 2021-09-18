"""
What is PEP8 -> Python Enhancement Proposal #8, known as PEP8.
PEP8 is the style guide for how to format Python code.
Note: We can always write Python code any way we want, as long as there is no error in the code.
But PEP8 works as a consistent style enhancement that makes our code more consistent and approachable. And it also makes
sure all Python users share the format guideline to follow.
Homework: read pep8.

# 2nd class
Using a consistent style makes your code more approachable and easier to read, even if you are the only one who will
ever read your code, following the style code will make it easier for you to change things later and can help you avoid
many common errors.

Whitespace conventions
In Python, whitespace is syntactically significant. Python programmers are especially sensitive to the effects of
whitespace on code clarity. Follow the guidelines related to whitespace.
The PyCharm will prompt us immediately if we break the PEP-8 guideline.
1. Use spaces instead of tabs for indentation.
2. Use 4 spaces for each level of syntactically significant indenting.
3. Lines should be 79 characters in length or less. (Note that there's a vertical line in PyCharm editor!)
4. Continuations of long expressions onto additional lines should be indented by four extra spaces from their normal
indentation level.
5. In a file, functions and classes should be separated by two blank lines. (We've met this)
6. In a class, methods should be separated by one blank line.
7. In a dictionary, put no whitespace between each key and colon, and put a single space before the corresponding value
if it fits on the same line.
8. Put one and only one space before and after the = operator in a variable assignment.
9. For type annotations, ensure that there is no separation between the variable name and the colon, and use a space
before the type information.

Naming conventions
1. Functions, variables, and attributes should be in lowercase_underscore format.
2. Protected instance attributes should be in _leading_underscore format.
3. Private instance attributes should be in __double_leading_underscore format.
4. Classes (including exceptions) should be in CapitalizedWord format.
5. Module-level constants should be in ALL_CAPS format.
6. Instance methods in classes should use self, which refers to the object, as the name of the first parameter.
7. Class methods should use cls, which refers to the class, as the name of the first parameter.
"""
# There are many guidelines in PEP8

if __name__ == '__main':
    print("I'm not sure whether this is following pep8")
