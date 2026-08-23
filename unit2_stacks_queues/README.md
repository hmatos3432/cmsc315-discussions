Unit 2 Discussion: Stacks and Queues
Overview

This assignment explored two fundamental linear data structures in Python:

Stack, which followed Last In, First Out (LIFO)
Queue, which followed First In, First Out (FIFO)

The assignment required the implementation of stack and queue operations, demonstrations of their behavior, testing of edge cases, and examples of real-world applications.

Stack Implementation

I created a Stack class that used a Python list as its internal data structure.

The following stack operations were implemented:

push() added a new value to the top of the stack.
pop() removed and returned the most recently added value.
peek() returned the top value without removing it.
is_empty() checked whether the stack contained any values.

The stack demonstrated Last In, First Out (LIFO) behavior. Four books were added to the stack in the following order:

Book 1
Book 2
Book 3
Book 4

When the books were removed, Book 4 was removed first because it was the most recently added item. The remaining books were then removed in reverse order.

Queue Implementation

I created a Queue class that used collections.deque as its internal data structure.

The following queue operations were implemented:

enqueue() added a new value to the back of the queue.
dequeue() removed and returned the value at the front of the queue.
front() returned the first value without removing it.
is_empty() checked whether the queue contained any values.

The queue demonstrated First In, First Out (FIFO) behavior. Four customers were added to the queue in the following order:

Customer 1
Customer 2
Customer 3
Customer 4

When customers were served, Customer 1 was removed first because that customer had entered the queue first. The remaining customers were then served in the same order they entered.

Edge Cases Tested

Several edge cases were tested to verify that the program handled unusual conditions without crashing.

Stack Edge Cases

I tested the following situations:

Attempted to use pop() on an empty stack.
Attempted to use peek() on an empty stack.
Created a stack containing only one item.
Removed the single item.
Verified that the stack became empty afterward.

The program returned clear messages when invalid operations were attempted on an empty stack.

Queue Edge Cases

I tested the following situations:

Attempted to use dequeue() on an empty queue.
Attempted to use front() on an empty queue.
Created a queue containing only one item.
Removed the single item.
Verified that the queue became empty afterward.

The program returned clear messages when invalid operations were attempted on an empty queue.

Real-World Applications
Stack Example: Browser History

I used browser history as a real-world example of a stack.

When a user visits several webpages, the most recently visited page would be the first page returned to when the Back button was selected.

For example:

Page 1
Page 2
Page 3
Page 4

If Page 4 was the most recently visited page, it would be the first page removed from the history stack when moving backward.

This demonstrated LIFO behavior.

Queue Example: Customer Service Line

I used a customer service line as a real-world example of a queue.

Customers were served in the same order that they entered the line.

For example:

Customer 1
Customer 2
Customer 3
Customer 4

Customer 1 entered first and was therefore served first.

This demonstrated FIFO behavior.

Memory Usage

Both the stack and queue required additional memory as more items were added.

If n represented the number of stored items, both structures required approximately:

O(n) memory

This meant that memory usage grew linearly as additional items were stored.

For example, a structure containing four items required storage for four values, while a structure containing one hundred items required storage for one hundred values.

Removing items reduced the number of values that needed to be stored.

The Python list used by the stack could reserve some additional internal capacity as it grew, while deque managed its own internal blocks of memory. However, the overall theoretical memory requirement for both structures remained O(n).

Time Complexity

The primary operations used in this assignment were efficient.

Stack
push() - O(1) average time
pop() - O(1) time
peek() - O(1) time
is_empty() - O(1) time
Queue
enqueue() - O(1) time
dequeue() - O(1) time
front() - O(1) time
is_empty() - O(1) time

Using collections.deque allowed values to be efficiently removed from the front of the queue without shifting every remaining item.

Program Results

The completed program successfully demonstrated both data structures.

The stack removed values in the following order:

Book 4
Book 3
Book 2
Book 1

This confirmed LIFO behavior.

The queue removed values in the following order:

Customer 1
Customer 2
Customer 3
Customer 4

This confirmed FIFO behavior.

All required edge cases were also handled without causing the program to terminate unexpectedly.

Running the Program

The program was executed using Python through IntelliJ with the Python plugin.

The file used for the assignment was:

unit2_stacks_queues/unit2_discussion.py

The program completed successfully with:

Process finished with exit code 0
GitHub

The completed Unit 2 files were committed to the CMSC 315 discussion repository.

Repository:

https://github.com/hmatos3432/cmsc315-discussions

Unit 2 folder:

https://github.com/hmatos3432/cmsc315-discussions/tree/main/unit2_stacks_queues