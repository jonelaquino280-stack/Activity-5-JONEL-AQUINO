Analysis: Stacks and Queues Implementation Choices

1. *Why the linked-list stack pushes at the head instead of the tail:*
   Pushing and popping at the head of a singly linked list takes $O(1)$ time because we only need to update the top reference and the new node's next pointer. If we were to perform operations at the tail, removing an element would require traversing the entire list to find the second-to-last node, making pop an $O(n)$ operation. Operating strictly at the head maintains constant time complexity for all core stack operations.

2. *Why the array queue must be circular:*
   In a naive array-based queue, dequeuing from the front requires either shifting all remaining elements left or continuously advancing the front index, which either wastes physical memory space or results in an $O(n)$ time complexity for removal. Treating the array as a circular buffer using modulo arithmetic ((front + size) % capacity) allows unused slots at the beginning of the array to be reused seamlessly when the rear index wraps around, ensuring $O(1)$ efficiency for both enqueues and dequeues without allocating new memory.
