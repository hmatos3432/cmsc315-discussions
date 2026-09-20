# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Completed Implementation

I implemented a library inventory in `unit6_discussion.py`. I created an empty
dictionary and inserted five book titles with their available copy counts. I
looked up two titles, changed the count for "Python Basics" from three to two
after a checkout, and removed "Database Design" after it was retired. I printed
the inventory before and after each update and deletion.

I retained every starter TODO prompt and existing comment. I added comments
that explained hashing, lookup, replacement, deletion, and collision resolution.
The retained TODO messages served as assignment labels; the completed
demonstrations followed them.

### Hash Table Design and Performance

I used immutable string keys and integer values. I relied on Python's built-in
dictionary implementation for hashing and collision resolution. I explained
CPython's open addressing: a collision caused the dictionary to probe other
slots and compare keys. I contrasted this with separate chaining, which stored
colliding entries together in a bucket.

I described lookup, insertion, and deletion as O(1) on average, with insertion
amortized across occasional resizing, assuming bounded key costs and
well-distributed hashes. I identified O(n) worst-case behavior when collisions
forced many comparisons. I also distinguished full-inventory printing and
copying, which required O(n) work, from individual dictionary operations.
I noted that increasing table occupancy could increase probing work and that
CPython managed resizing internally. I did not implement a custom hash
function or manually control the load factor.

For a reliable collision demonstration, I used integer IDs `1` and
`1 + sys.hash_info.modulus`. I verified their equal hashes and unequal values.
Both books remained retrievable. Updating and then deleting the first entry
preserved the second entry. This checked correctness under a collision; it did
not measure lookup speed.

### Edge Cases and Validation

| Case tested | Observed result |
| --- | --- |
| Existing title with zero copies | Returned 0, rather than treating the title as missing. |
| Missing lookup | Returned None through get(), without raising KeyError. |
| Missing deletion | Returned None through pop(); the inventory remained unchanged. |
| Assignment to a missing key | Inserted Cybersecurity as a new entry. |
| Empty dictionary | Lookup and deletion returned None; the dictionary remained empty. |
| List used as a key | Raised TypeError, which was caught and explained. |
| Two unequal keys with equal hashes | Preserved independent lookup, update, and deletion behavior. |

I ran the original starter and observed only headings and TODO messages. I ran
the completed file with Python 3.13.2 and verified the assertions and the final
"All demonstration checks passed." message. The terminal command used was:

```text
python unit6_hash_tables/unit6_discussion.py
```

I kept the example as a scripted demonstration with fixed data. I did not add
interactive input, persistent storage, or general quantity validation. I used
book titles for readability; an expanded inventory would have benefited from
unique IDs or ISBNs to distinguish books with identical titles.

### Reflection

This assignment helped me connect dictionary operations with the hash table concepts behind them. I used book titles as keys and available copy counts as values, then demonstrated insertion, retrieval, updating, and deletion. I also distinguished an existing title with zero available copies from a title that was missing entirely.

One implementation challenge was handling unsuccessful operations without stopping the demonstration. I addressed this by using get() and pop() with defaults. I tested an empty dictionary and caught the TypeError raised by an unhashable list key. Another challenge was demonstrating collisions reliably because ordinary string keys did not guarantee a collision. I used Python's numeric hash modulus to create two different integer IDs with the same hash and verified that both entries remained accessible.

The collision example showed why equal hashes did not necessarily mean equal keys. CPython used open addressing to resolve collisions, while a separate-chaining implementation would have stored colliding entries in a shared bucket. Well-distributed hashes reduced unnecessary comparisons and supported efficient lookups. Frequent collisions increased probing work and could reduce the performance advantage over a linear search.

### Submission Checklist Review

I checked the implementation against the repository's
`submission_checklist.md`. I completed the five TODO blocks, added test cases
and explanatory output, handled edge cases, and documented the library use
case. I prepared the initial discussion draft with a repository link, design
explanation, collision analysis, and reflection. Discussion-board posting and
two replies to classmates remained separate submission steps.

### References Consulted

- [Python dictionary operations and numeric hashing](https://docs.python.org/3/library/stdtypes.html)
- [Python operation complexity](https://docs.python.org/3/builtins/time-complexity.html)
- [CPython dictionary implementation](https://github.com/python/cpython/blob/main/Objects/dictobject.c)
