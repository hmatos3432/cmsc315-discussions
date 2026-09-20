"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Book titles are immutable string keys; values count available copies.
    # dict hashes each key to locate an entry instead of scanning every title.
    # CPython resolves collisions internally with open addressing (probing
    # other slots and checking key equality); this application uses that code.
    inventory = {}
    inventory["Python Basics"] = 3
    inventory["Data Structures"] = 2
    inventory["Algorithms"] = 4
    inventory["Database Design"] = 1
    inventory["Computer Networks"] = 0
    print("Library inventory (title: available copies):", inventory)
    assert len(inventory) == 5


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Existing keys can be indexed directly. A count of zero is a valid
    # result, so it must not be treated as a missing title.
    for title in ("Python Basics", "Computer Networks"):
        print(f"Lookup {title!r}: {inventory[title]} available copies")
    assert inventory["Python Basics"] == 3
    assert inventory["Computer Networks"] == 0


    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before checkout:", inventory)
    # Reassigning an equal key replaces its value, without adding a new entry.
    inventory["Python Basics"] = 2
    print("After checking out one copy of Python Basics:", inventory)
    assert inventory["Python Basics"] == 2 and len(inventory) == 5


    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Before removing a retired title:", inventory)
    # pop removes both the key and its value and returns the former value.
    removed = inventory.pop("Database Design")
    print(f"Removed 'Database Design' (previously {removed} available copy).")
    print("After removal:", inventory)
    assert "Database Design" not in inventory and len(inventory) == 4


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # None is an unambiguous missing marker because inventory values are ints.
    missing = inventory.get("Artificial Intelligence")
    print("Missing lookup:", missing, "(None means the title was not found.)")
    assert missing is None

    before = inventory.copy()
    removed = inventory.pop("Unknown Book", None)
    print("Missing deletion:", removed, "(No entry was removed; no KeyError.)")
    assert removed is None and inventory == before

    # Assignment to a missing key inserts it; it is not an update-only API.
    inventory["Cybersecurity"] = 2
    print("Assignment to a missing key inserted 'Cybersecurity':", inventory)
    assert inventory["Cybersecurity"] == 2 and len(inventory) == 5

    empty_inventory = {}
    print("Empty inventory lookup:", empty_inventory.get("Python Basics"))
    print("Empty inventory deletion:", empty_inventory.pop("Python Basics", None))
    assert empty_inventory == {}

    # Lists are mutable and unhashable, so they cannot serve as dictionary keys.
    try:
        inventory[["Invalid Title"]] = 1
    except TypeError:
        print("Invalid list key rejected: dictionary keys must be hashable.")
    else:
        raise AssertionError("A list key should have raised TypeError.")
    assert len(inventory) == 5

    print("\n=== COLLISION DEMONSTRATION ===")
    # Python's numeric hash modulus lets us construct unequal integer keys
    # with equal hashes, without relying on randomized string hash values.
    import sys

    first_id = 1
    second_id = first_id + sys.hash_info.modulus
    assert first_id != second_id and hash(first_id) == hash(second_id)
    books_by_id = {first_id: "Python Basics", second_id: "Algorithms"}
    print(f"Different book IDs: {first_id} and {second_id}")
    print(f"Equal hashes: {hash(first_id)} and {hash(second_id)}")
    print("Both books remained retrievable:", books_by_id)
    assert len(books_by_id) == 2
    assert books_by_id[first_id] == "Python Basics"
    assert books_by_id[second_id] == "Algorithms"
    # A collision does not make unequal keys identical. Updating/deleting one
    # entry must preserve the other, even when their hashes are the same.
    books_by_id[first_id] = "Python Basics, Second Edition"
    assert books_by_id[second_id] == "Algorithms"
    del books_by_id[first_id]
    assert books_by_id[second_id] == "Algorithms"
    print("After updating and deleting the first ID:", books_by_id)
    print("All demonstration checks passed.")




if __name__ == "__main__":
    main()