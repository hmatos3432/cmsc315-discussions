from collections import deque


class Stack:
    def __init__(self):
        # A list stores the values in the stack.
        self.items = []

    def push(self, value):
        # Adding to the end supports LIFO because the newest
        # value becomes the first value removed.
        self.items.append(value)

    def pop(self):
        # Check for an empty stack before attempting removal.
        if self.is_empty():
            return "Stack is empty. Nothing to pop."

        return self.items.pop()

    def peek(self):
        # Peek returns the top value without removing it.
        if self.is_empty():
            return "Stack is empty. Nothing to peek at."

        return self.items[-1]

    def is_empty(self):
        # An empty list means the stack contains no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # deque provides efficient operations from both ends.
        self.items = deque()

    def enqueue(self, value):
        # New values are added to the back so older values
        # remain at the front, supporting FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # Check for an empty queue before attempting removal.
        if self.is_empty():
            return "Queue is empty. Nothing to dequeue."

        return self.items.popleft()

    def front(self):
        # Front returns the first value without removing it.
        if self.is_empty():
            return "Queue is empty. Nothing at the front."

        return self.items[0]

    def is_empty(self):
        # An empty deque means the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four values to the stack:")
    stack.push("Book 1")
    stack.push("Book 2")
    stack.push("Book 3")
    stack.push("Book 4")

    print("Current stack:", stack.items)
    print("Top value using peek():", stack.peek())

    print("\nRemoving values demonstrates LIFO:")
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())

    print("Is the stack empty?", stack.is_empty())

    # Edge case: pop from empty stack.
    print("\nAttempting to pop from an empty stack:")
    print(stack.pop())

    # Edge case: peek at empty stack.
    print("\nAttempting to peek at an empty stack:")
    print(stack.peek())

    # Edge case: single-item stack.
    print("\nTesting a stack containing one item:")

    single_stack = Stack()
    single_stack.push("Only Item")

    print("Item added:", single_stack.peek())
    print("Item removed:", single_stack.pop())
    print("Is the single-item stack empty?", single_stack.is_empty())

    # ===============================
    # QUEUE DEMO
    # ===============================

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four customers to the queue:")
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Current queue:", list(queue.items))
    print("Front of queue:", queue.front())

    print("\nRemoving values demonstrates FIFO:")
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())

    print("Is the queue empty?", queue.is_empty())

    # Edge case: dequeue from empty queue.
    print("\nAttempting to dequeue from an empty queue:")
    print(queue.dequeue())

    # Edge case: view front of empty queue.
    print("\nAttempting to view the front of an empty queue:")
    print(queue.front())

    # Edge case: single-item queue.
    print("\nTesting a queue containing one item:")

    single_queue = Queue()
    single_queue.enqueue("Only Customer")

    print("Customer added:", single_queue.front())
    print("Customer served:", single_queue.dequeue())
    print("Is the single-item queue empty?", single_queue.is_empty())

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


if __name__ == "__main__":
    main()