"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

from time import perf_counter


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks one value at a time from left to right.
    # In the worst case, the target is missing or at the end, so every
    # element must be inspected. That makes the time complexity O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = lst[middle]

        if middle_value == target:
            return middle

        if middle_value < target:
            # The target can only be in the right half, so the left half
            # is removed from consideration.
            left = middle + 1
        else:
            # The target can only be in the left half, so the right half
            # is removed from consideration.
            right = middle - 1

    return -1


def count_linear_comparisons(lst, target):
    """Return how many equality checks linear search performed."""
    comparisons = 0

    for value in lst:
        comparisons += 1
        if value == target:
            break

    return comparisons


def count_binary_comparisons(lst, target):
    """Return how many midpoint checks binary search performed."""
    comparisons = 0
    left = 0
    right = len(lst) - 1

    while left <= right:
        comparisons += 1
        middle = (left + right) // 2
        middle_value = lst[middle]

        if middle_value == target:
            break

        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return comparisons


def describe_result(index):
    """Format the required index return value in a readable way."""
    if index == -1:
        return "not found (index -1)"

    return f"found at index {index}"


def run_search_case(label, dataset, target):
    """Run both algorithms and print their index, comparisons, and time."""
    print(f"\n{label}")
    print(f"Dataset size: {len(dataset):,} | Target: {target}")

    for name, search_function, count_function in (
        ("Linear search", linear_search, count_linear_comparisons),
        ("Binary search", binary_search, count_binary_comparisons),
    ):
        start_time = perf_counter()
        index = search_function(dataset, target)
        elapsed_time = perf_counter() - start_time
        comparisons = count_function(dataset, target)

        print(
            f"{name:<14} -> {describe_result(index):<24} | "
            f"comparisons: {comparisons:>7,} | "
            f"time: {elapsed_time:.8f} seconds"
        )


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_numbers = [3, 7, 12, 18, 24, 31, 45]

    # Both algorithms return the same index when the value exists.
    run_search_case("Existing value in a small sorted list", small_numbers, 24)

    # Both algorithms return -1 when the value is not present.
    run_search_case("Missing value in a small sorted list", small_numbers, 20)

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_numbers = list(range(0, 1_000_000, 2))

    # On a large sorted list, binary search uses far fewer comparisons because
    # each midpoint check eliminates about half of the remaining values.
    run_search_case("Existing value in a large sorted list", large_numbers, 998_000)
    run_search_case("Missing value in a large sorted list", large_numbers, 999_999)

    print(
        "\nPerformance note: binary search needed fewer checks on the large "
        "dataset because the data was sorted. Linear search still worked, "
        "but it had to scan values one at a time."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    edge_cases = [
        ("Empty list", [], 10, "No elements exist, so both searches return -1."),
        (
            "Single-element list, value exists",
            [42],
            42,
            "The only index is checked and returned immediately.",
        ),
        (
            "Value at first position",
            [5, 10, 15, 20],
            5,
            "Linear search succeeds on its first check.",
        ),
        (
            "Value at last position",
            [5, 10, 15, 20],
            20,
            "Linear search reaches the end, while binary search still halves the range.",
        ),
    ]

    for case_name, dataset, target, explanation in edge_cases:
        run_search_case(case_name, dataset, target)
        print(f"Explanation: {explanation}")


if __name__ == "__main__":
    main()
