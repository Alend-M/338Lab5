class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1
        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        element = self.queue[self.front]
        print(f"peek {element}")
        return element

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")
            return
        new_node = Node(element)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.size += 1
        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        element = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        element = self.front.data
        print(f"peek {element}")
        return element

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return self.size == self.capacity

# List of operations with expected outputs for testing
operations = [
    ("enqueue", 1),   # enqueue 1
    ("enqueue", 2),   # enqueue 2
    ("enqueue", 3),   # enqueue 3
    ("peek", 1),      # peek 1
    ("dequeue", 1),   # dequeue 1
    ("dequeue", 2),   # dequeue 2
    ("enqueue", 4),   # enqueue 4
    ("enqueue", 5),   # enqueue 5
    ("peek", 3),      # peek 3
    ("enqueue", 6),   # enqueue 6
    ("enqueue", 7),   # enqueue 7
    ("enqueue", 8),   # enqueue 8
    ("enqueue", 9),   # enqueue 9
    ("enqueue", 10),  # enqueue 10
    ("enqueue", 11),  # enqueue None (queue is full)
    ("dequeue", 3),   # dequeue 3
    ("dequeue", 4),   # dequeue 4
    ("dequeue", 5),   # dequeue 5
    ("dequeue", 6),   # dequeue 6
    ("dequeue", 7),   # dequeue 7
    ("dequeue", 8),   # dequeue 8
    ("dequeue", 9),   # dequeue 9
    ("dequeue", 10),  # dequeue 10
    ("dequeue", None),# dequeue None (queue is empty)
    ("peek", None),   # peek None (queue is empty)
    ("enqueue", 11),  # enqueue 11
    ("peek", 11),     # peek 11
    ("dequeue", 11),  # dequeue 11
    ("enqueue", 12),  # enqueue 12
    ("enqueue", 13),  # enqueue 13
    ("enqueue", 14),  # enqueue 14
    ("enqueue", 15),  # enqueue 15
    ("enqueue", 16),  # enqueue 16
    ("enqueue", 17),  # enqueue 17
    ("enqueue", 18),  # enqueue 18
    ("enqueue", 19),  # enqueue 19
    ("enqueue", 20),  # enqueue 20
    ("enqueue", 21),  # enqueue None (queue is full)
    ("enqueue", 22),  # enqueue None (queue is full)
]

MyListArray = CircularQueueArray(10)
MyListLinkedList = CircularQueueLinkedList(10)

for operation, value in operations:
    if operation == "enqueue":
        MyListArray.enqueue(value)
        MyListLinkedList.enqueue(value)
    elif operation == "dequeue":
        MyListArray.dequeue()
        MyListLinkedList.dequeue()
    elif operation == "peek":
        MyListArray.peek()
        MyListLinkedList.peek()
