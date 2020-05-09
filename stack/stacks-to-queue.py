
'''
ILLUSTRATION
[2]       []            # E
[2, 3]    []            # E
[2,3, 4]  []            # E
[]        [4, 3, 2]     # D
[3]       [4, 3, 2]     # E
[3]       [4, 3]        # D
[3]       [4]           # D
[3]       []            # D
[]        [3]           # D
[]        []            # D
'''

from stack import Stack


class QueueFromTwoStacks:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)
    
    def dequeue(self):
        if len(self.out_stack) == 0:
            # Move items from instack to outstack in reverse
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # If outstack is still empty, raise exception
            if not len(self.out_stack):
                raise IndexError("Can't dequeue from empty queue")

        return self.out_stack.pop()



# SOLUTION 1
class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def is_empty(self):
        return self.inbox.is_empty() and self.outbox.is_empty()

    def enqueue(self, data):
        self.inbox.push(data)

    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()


# SOLUTION 2
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []

    def shift(self):
        """
        Shift all the elements of inbox to outbox
        """
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbox.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outbox:
            return self.outbox.pop()

        self.shift()
        return self.outbox.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outbox:
            self.shift()
        return self.outbox[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inbox and not self.outbox