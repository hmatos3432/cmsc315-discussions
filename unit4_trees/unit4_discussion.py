"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # A BST keeps smaller values on the left and larger values on
        # the right, so each comparison tells the recursion which half
        # of the remaining tree could contain the correct insert point.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # When an empty position is reached, the new value belongs there.
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values are not inserted so the tree stores one
            # copy of each value and search results stay unambiguous.
            return node

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Unlike linear search, a BST search does not need to check every
        # value when the tree is balanced. Each comparison can discard the
        # entire left or right subtree from consideration.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # In a BST, every value in the left subtree is smaller than the
        # current node and every value in the right subtree is larger.
        # Visiting left, node, then right therefore produces sorted output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    tree_values = [50, 30, 70, 20, 40, 60, 80, 65]

    # Values below 50 move into the left subtree, while values above 50
    # move into the right subtree. Each recursive step repeats that same
    # smaller-or-larger decision and reduces the remaining search space.
    for value in tree_values:
        tree.insert(value)

    print("Values inserted into the BST:", tree_values)
    print("Root value:", tree.root.value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    traversal = tree.inorder()
    print("In-order traversal result:", traversal)
    print("The traversal is sorted because it visits left subtree, node, then right subtree.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    search_values = [40, 65, 25, 90]

    # The first two values exist in the tree, while the last two do not.
    # Missing values eventually reach an empty child reference and return False.
    for value in search_values:
        result = tree.search(value)
        print(f"Search for {value}: {result}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty_tree = BST()
    print("Empty tree traversal:", empty_tree.inorder())
    print("Search for 10 in an empty tree:", empty_tree.search(10))

    before_duplicate = tree.inorder()
    tree.insert(60)
    after_duplicate = tree.inorder()
    print("Traversal before duplicate insert:", before_duplicate)
    print("Traversal after trying to insert duplicate 60:", after_duplicate)
    print("The duplicate was ignored so the BST kept one copy of each value.")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")
    product_tree = BST()
    product_ids = [1042, 1010, 1088, 1005, 1028, 1060, 1095]

    # A store inventory system could use a BST-like ordering strategy for
    # product IDs so lookup decisions move lower or higher instead of
    # scanning every product one at a time.
    for product_id in product_ids:
        product_tree.insert(product_id)

    print("Product IDs inserted:", product_ids)
    print("Product IDs in sorted order:", product_tree.inorder())
    print("Search for product 1060:", product_tree.search(1060))
    print("Search for product 1100:", product_tree.search(1100))



if __name__ == "__main__":
    main()
