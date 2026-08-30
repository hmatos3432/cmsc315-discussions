# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists.

The completed program used a course registration roster as the real-world scenario. The roster made it easier to show how values were inserted, removed, and searched while also explaining how Python lists shifted elements after certain operations.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Implementation Documentation

### Insert Function

I implemented `insert_at()` using Python's built-in `list.insert()` method.

The function inserted a value at the requested index and returned the updated list. I added comments explaining that values at the insertion index and to the right shifted one position. This showed why inserting near the beginning or middle of a list could require more work than inserting at the end.

### Delete Function

I implemented `delete_at()` by validating the index before calling `pop()`.

If the index was valid, the function removed and returned the value at that index. If the index was invalid, the function returned `None` instead of allowing the program to crash with an `IndexError`. This demonstrated safe deletion and showed why validation was important when working with user-provided indexes.

### Search Function

I implemented `search_value()` using a loop with `enumerate()`.

The function checked each list item in order and returned the matching index when the value was found. If the value was not found, it returned `-1`. This demonstrated linear search because the list was scanned sequentially from the beginning to the end.

## Tests Performed

### Insertion Tests

I created a course roster with four student names:

- Ava
- Ben
- Cara
- Dion

The program inserted `Zara` at the beginning, `Maya` in the middle, and `Eli` at the end. After each insertion, the updated roster was printed so the movement of list values could be observed.

### Deletion Tests

The program deleted values from the beginning, middle, and end of the roster.

Each deletion printed the removed value and the updated list. This showed that deleting from the beginning or middle caused later values to shift left, while deleting from the end did not require later values to move.

### Search Tests

The program searched for `Maya`, which existed in the roster, and returned that name's index.

The program also searched for `Zoe`, which did not exist in the roster, and returned `-1`. This showed how the function handled both successful and unsuccessful searches.

## Edge Cases Tested

I tested invalid deletion by trying to delete index `25` from the roster. The function returned `None`, and the roster stayed unchanged.

I also tested deletion from an empty list. The function returned `None` because there was no valid value to remove.

As an additional edge case, I inserted `Kai` into an empty list. The list grew from empty to one value successfully. I also searched an empty list and received `-1`, showing that the search function handled empty input safely.

## Real-World Application

This program modeled a course registration roster.

In a real registration system, inserting into a list could represent adding a student to a class roster. Deleting from a list could represent a student dropping the class. Searching could represent checking whether a specific student was already enrolled.

The assignment showed that list operations were useful but had performance tradeoffs. Beginning and middle insertions or deletions could require shifting several values, so those operations took O(n) time in the worst case. Searching also took O(n) time because each value might need to be checked. End insertion was more efficient in typical cases because it usually behaved like an append operation.

## Program Results

The completed program successfully demonstrated:

- insertion at the beginning, middle, and end
- deletion at the beginning, middle, and end
- searching for existing and missing values
- invalid index handling
- empty list handling
- a real-world course roster scenario

The program completed successfully with exit code `0`.

## Running the Program

The file used for the assignment was:

`unit3_lists/unit3_discussion.py`

The program was run with:

```powershell
python .\unit3_lists\unit3_discussion.py
```

## GitHub

The completed Unit 3 files were committed to the CMSC 315 discussion repository.

Repository:

https://github.com/hmatos3432/cmsc315-discussions

Unit 3 folder:

https://github.com/hmatos3432/cmsc315-discussions/tree/main/unit3_lists

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150-200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
