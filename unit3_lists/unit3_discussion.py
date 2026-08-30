"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert() changes the original list in place.
    # Every element at the insertion index and to the right shifts one
    # position, so inserting near the beginning usually costs more work
    # than inserting at the end.
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # The index is validated before pop() is called so the program does not
    # crash with an IndexError when the list is empty or the index is outside
    # the list's valid range.
    if index < 0 or index >= len(lst):
        return None

    # pop(index) removes the item and returns the removed value.
    # Items to the right of the deleted value shift left to close the gap.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because each item is checked in order.
    # The search stops early if a match is found, but in the worst case
    # it must scan the entire list.
    for index, item in enumerate(lst):
        if item == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Created a course roster to make the list operations easier to interpret.
    course_roster = ["Ava", "Ben", "Cara", "Dion"]
    print("Original course roster:", course_roster)

    # Inserted at index 0. Existing names shifted one position to the right.
    insert_at(course_roster, 0, "Zara")
    print("After inserting Zara at the beginning:", course_roster)

    # Inserted near the middle. Items from the middle through the end shifted.
    middle_index = len(course_roster) // 2
    insert_at(course_roster, middle_index, "Maya")
    print(
        f"After inserting Maya in the middle at index {middle_index}:",
        course_roster
    )

    # Inserted at the end. This behaves like appending and requires the fewest
    # shifts because no existing student needs to move.
    insert_at(course_roster, len(course_roster), "Eli")
    print("After inserting Eli at the end:", course_roster)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Deleted from the beginning. The remaining names shifted left.
    removed_value = delete_at(course_roster, 0)
    print("Removed from the beginning:", removed_value)
    print("Roster after beginning deletion:", course_roster)

    # Deleted from the middle. The item returned by delete_at() shows which
    # value was removed before the list closed the gap.
    middle_index = len(course_roster) // 2
    removed_value = delete_at(course_roster, middle_index)
    print("Removed from the middle:", removed_value)
    print("Roster after middle deletion:", course_roster)

    # Deleted from the end. This removal does not require shifting later items
    # because there are no elements after the final index.
    removed_value = delete_at(course_roster, len(course_roster) - 1)
    print("Removed from the end:", removed_value)
    print("Roster after end deletion:", course_roster)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Searched for a value that exists in the current roster.
    existing_name = "Maya"
    found_index = search_value(course_roster, existing_name)
    print(
        existing_name,
        "was found at index",
        found_index,
        "using linear search."
    )

    # Searched for a value that does not exist. The function returns -1 so the
    # caller can handle the missing value without an exception.
    missing_name = "Zoe"
    missing_index = search_value(course_roster, missing_name)
    print(
        f"{missing_name} was not found. The search function returned "
        f"{missing_index}."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Tried to delete using an index that does not exist.
    invalid_delete = delete_at(course_roster, 25)
    print("Deleting index 25 returned:", invalid_delete)
    print("Roster stayed unchanged after invalid deletion:", course_roster)

    # Edge case 2: Tried to delete from an empty list.
    empty_roster = []
    empty_delete = delete_at(empty_roster, 0)
    print("Deleting from an empty list returned:", empty_delete)

    # Edge case 3: Inserted into an empty list to show that a list can grow
    # from no values to one value without special setup.
    insert_at(empty_roster, 0, "Kai")
    print("Empty roster after inserting Kai:", empty_roster)

    # Edge case 4: Searched an empty list and received -1 because there were
    # no values to scan.
    empty_search = search_value([], "Kai")
    print("Searching an empty list returned:", empty_search)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")
    print(
        "A course registration roster can use list insertion when a student "
        "is added, deletion when a student drops the course, and search when "
        "staff need to find whether a student is enrolled."
    )

    print(
        "Beginning and middle changes may shift several entries, while a "
        "linear search checks names one at a time until it finds a match or "
        "reaches the end."
    )



if __name__ == "__main__":
    main()
