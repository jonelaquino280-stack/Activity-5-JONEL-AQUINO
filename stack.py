class Node:
    """Node class for linked list implementations of Stack and Queue."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.value = value
        self.next = None

class ArrayStack:
    """Fixed-capacity stack implemented using a Python list."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear reference
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: No top element to peek.")
        return self.data[self.top]


class LinkedStack:
    """Dynamic stack implemented using a singly linked list (LIFO at head)."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: No top element to peek.")
        return self.top.value
