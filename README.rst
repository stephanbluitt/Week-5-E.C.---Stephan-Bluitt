Simple Letter Counter
=====================

A very simple Python program that counts letters in text using Python's built-in ``len()`` function.

What is len()?
--------------
``len()`` is one of Python's most useful built-in functions. It returns the **length** (number of items) of any object.

What ``len()`` works with:
- **Strings**: ``len("hello")`` returns ``5`` (5 characters)
- **Lists**: ``len([1, 2, 3])`` returns ``3`` (3 items)  
- **Dictionaries**: ``len({"a": 1, "b": 2})`` returns ``2`` (2 key-value pairs)
- **Sets**: ``len({1, 2, 2, 3})`` returns ``3`` (unique items only)

In our program, we use ``len()`` to count how many letters are in a list

What It Does
------------
- Asks you to type some text
- Counts only letters (A-Z, a-z)
- Ignores spaces, numbers, and punctuation
- Shows the total number of letters

How to Run
----------
1. Make sure you have Python installed
2. Download ``letter_counter.py``
3. Open terminal/command prompt
4. Type::

    python letter_counter.py

5. Enter your text when asked!

Example
-------
::

    === LETTER COUNTER ===
    Enter your text: Hello World! 123
    
    Your text: 'Hello World! 123'
    Total letters: 10

How It Works
------------
The program uses:

- ``input()`` - to get text from user
- ``.isalpha()`` - to check if character is a letter
- ``len()`` - to count the letters

Code Explanation
----------------
::

    letters = [char for char in text if char.isalpha()]

This line creates a list of only letter characters.

::

    total_letters = len(letters)

This line counts how many letters are in the list.
