# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations.

The completed program built a BST, inserted values recursively, searched recursively, and returned sorted values with an in-order traversal. The program also demonstrated edge cases and used product IDs as a real-world BST example.

## Learning Objectives

- Built a BST
- Inserted values recursively
- Searched recursively
- Performed in-order traversal
- Explained BST organization

## Implementation Documentation

### Node Class

I implemented the `Node` class by storing each node's value and initializing `left` and `right` child references to `None`.

This allowed each node to point to smaller values through the left child and larger values through the right child.

### BST Class

I implemented the `BST` class with a `root` reference that started as `None`.

The `insert()` method used the recursive helper method `_insert_recursive()`. If the current position was empty, the helper created a new `Node`. If the new value was smaller than the current node, it moved left. If the new value was larger, it moved right. Duplicate values were ignored so the tree kept one copy of each value.

The `search()` method used `_search_recursive()` to compare the target value with the current node. The search moved left for smaller targets and right for larger targets. This showed how a BST could reduce the search space at each step instead of scanning every value like a linear search.

The `inorder()` method used `_inorder_recursive()` to visit the left subtree, then the current node, then the right subtree. Since BST values were organized with smaller values on the left and larger values on the right, the traversal produced sorted output.

## Tests Performed

### Tree Construction

I created a BST and inserted these values:

- `50`
- `30`
- `70`
- `20`
- `40`
- `60`
- `80`
- `65`

The values created both left and right subtrees. The root value was `50`.

### In-Order Traversal

The program performed an in-order traversal and returned:

```text
[20, 30, 40, 50, 60, 65, 70, 80]
```

This verified that the traversal returned the BST values in sorted order.

### Search Tests

The program searched for `40` and `65`, which existed in the BST, and returned `True` for both.

The program also searched for `25` and `90`, which did not exist in the BST, and returned `False` for both.

## Edge Cases Tested

I tested an empty BST by running an in-order traversal and searching for `10`.

The empty traversal returned `[]`, and the empty-tree search returned `False`. This showed that the recursive methods handled missing nodes safely.

I also tested duplicate insertion by trying to insert `60` a second time. The traversal stayed the same before and after the duplicate insert, which showed that the BST kept only one copy of each value.

## Real-World Application

The program modeled a store inventory lookup using product IDs.

I inserted these product IDs into a separate BST:

- `1042`
- `1010`
- `1088`
- `1005`
- `1028`
- `1060`
- `1095`

The in-order traversal returned the product IDs in sorted order. The program searched for product `1060` and returned `True`, then searched for product `1100` and returned `False`.

This example showed how a BST-style ordering strategy could help organize searchable values such as inventory IDs, account numbers, or other ordered records.

## Program Results

The completed program successfully demonstrated:

- BST construction
- recursive insertion
- recursive searching
- sorted in-order traversal
- successful and unsuccessful search results
- empty-tree handling
- duplicate-value handling
- a real-world product ID scenario

The program completed successfully with exit code `0`.

## Running the Program

The file used for the assignment was:

`unit4_trees/unit4_discussion.py`

The program was run with:

```powershell
python .\unit4_trees\unit4_discussion.py
```

## GitHub

The completed Unit 4 files were committed to the CMSC 315 discussion repository.

Repository:

https://github.com/hmatos3432/cmsc315-discussions

Unit 4 folder:

https://github.com/hmatos3432/cmsc315-discussions/tree/main/unit4_trees

## Discussion Board Reflection

While completing this assignment, I learned how a Binary Search Tree organized data by comparison instead of by position. I implemented recursive insertion, recursive searching, and in-order traversal, which helped me understand how each node connected to left and right subtrees. The main challenge was making sure each recursive method returned the correct result when it reached an empty child reference. I overcame that by treating `None` as the base case for insertion, searching, and traversal. A BST kept smaller values on the left and larger values on the right, so each search step narrowed the possible location of a value. Compared to a list, this organization could be more efficient because the search did not always need to scan every item. If the tree was reasonably balanced, each comparison removed about half of the remaining tree from consideration. The assignment also showed that traversal order mattered because in-order traversal produced the values in sorted order.
