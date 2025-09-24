# Week-5-E.C.---Stephan-Bluitt
# Small repository to explain a new concept

Text Counter with Collections.Counter
=====================================

This demo shows how to use ``collections.Counter`` for advanced text analysis, going beyond simple counting loops.

What is collections.Counter?
----------------------------
``Counter`` is a dictionary subclass in Python's standard library designed for counting hashable objects. It's optimized for counting and provides useful methods like ``most_common()``.

Installation
------------
No installation required! ``collections.Counter`` is part of Python's standard library.

Demo Files
----------

1. ``basic_counter.py``
   * Basic letter and word counting
   * Comparing Counter to manual approaches

2. ``advanced_counter.py``
   * Mathematical operations with counters
   * Finding most common elements
   * Working with large text files

Example Usage
-------------

.. code-block:: python

    from collections import Counter
    
    # Count letters in a word
    word = "mississippi"
    letter_count = Counter(word)
    print(letter_count)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
    
    # Get most common letters
    print(letter_count.most_common(2))  # [('i', 4), ('s', 4)]
