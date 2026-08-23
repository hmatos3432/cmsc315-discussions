"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # A Python list was used to store the values in the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # The value is added to the end of the list.
        # Because new values are added and removed from the same end,
        # the most recently added value is removed first, supporting LIFO.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # The stack is checked before attempting to remove an item.
        # This prevents an IndexError when the stack is empty.
        if self.is_empty():
            return "Stack is empty. Nothing to pop."

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # peek() returns the newest item without changing the stack.
        if self.is_empty():
            return "Stack is empty. Nothing to peek at."

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # deque was used because it efficiently supports adding items
        # to the back and removing items from the front.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Values are added to the back of the queue.
        # Older values remain at the front and are removed first,
        # which supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # The queue is checked before attempting to remove an item.
        # This prevents an error when the queue is empty.
        if self.is_empty():
            return "Queue is empty. Nothing to dequeue."

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # front() returns the oldest value without removing it.
        if self.is_empty():
            return "Queue is empty. Nothing at the front."

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    # Created the Stack object.
    stack = Stack()

    # Added four values to demonstrate stack behavior.
    print("Adding four values to the stack:")

    stack.push("Book 1")
    stack.push("Book 2")
    stack.push("Book 3")
    stack.push("Book 4")

    print("Current stack:", stack.items)

    # peek() showed the top item without removing it.
    print("Top value using peek():", stack.peek())

    # Demonstrated LIFO behavior.
    # Book 4 was added last, so it was removed first.
    print("\nRemoving values demonstrates LIFO:")

    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())

    print("Is the stack empty?", stack.is_empty())

    # Tested pop() on an empty stack.
    print("\nAttempting to pop from an empty stack:")
    print(stack.pop())

    # Tested peek() on an empty stack.
    print("\nAttempting to peek at an empty stack:")
    print(stack.peek())

    # Tested a stack containing only one item.
    print("\nTesting a stack containing one item:")

    single_stack = Stack()
    single_stack.push("Only Item")

    print("Item added:", single_stack.peek())
    print("Item removed:", single_stack.pop())
    print(
        "Is the single-item stack empty?",
        single_stack.is_empty()
    )

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    # Created the Queue object.
    queue = Queue()

    # Added four customers to demonstrate queue behavior.
    print("Adding four customers to the queue:")

    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Current queue:", list(queue.items))

    # front() showed the first customer without removing the customer.
    print("Front of queue:", queue.front())

    # Demonstrated FIFO behavior.
    # Customer 1 entered first, so Customer 1 was served first.
    print("\nRemoving values demonstrates FIFO:")

    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())

    print("Is the queue empty?", queue.is_empty())

    # Tested dequeue() on an empty queue.
    print("\nAttempting to dequeue from an empty queue:")
    print(queue.dequeue())

    # Tested front() on an empty queue.
    print("\nAttempting to view the front of an empty queue:")
    print(queue.front())

    # Tested a queue containing only one item.
    print("\nTesting a queue containing one item:")

    single_queue = Queue()
    single_queue.enqueue("Only Customer")

    print("Customer added:", single_queue.front())
    print("Customer served:", single_queue.dequeue())
    print(
        "Is the single-item queue empty?",
        single_queue.is_empty()
    )

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")

    print(
        "A stack could represent browser history because the most recently "
        "visited page is the first page returned to when pressing Back."
    )

    print(
        "A queue could represent customers waiting for service because the "
        "first customer to arrive should be the first customer served."
    )

    # ===============================
    # MEMORY USAGE
    # ===============================

    print("\n=== MEMORY USAGE ===")

    print(
        "Both stacks and queues use more memory as more items are added. "
        "Their theoretical memory usage is O(n), where n is the number "
        "of stored items."
    )


if __name__ == "__main__":
    main()