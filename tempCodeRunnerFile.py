class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            return "enqueue None"
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1
        return f"enqueue {element}"

    def dequeue(self):
        if self.is_empty():
            return "dequeue None"
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return f"dequeue {element}"

    def peek(self):
        if self.is_empty():
            return "peek None"
        element = self.queue[self.front]
        return f"peek {element}"

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
            return "enqueue None"
        new_node = Node(element)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.size += 1
        return f"enqueue {element}"

    def dequeue(self):
        if self.is_empty():
            return "dequeue None"
        element = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return f"dequeue {element}"

    def peek(self):
        if self.is_empty():
            return "peek None"
        element = self.front.data
        return f"peek {element}"

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return self.size == self.capacity

operations = [
    ("enqueue", 1, "enqueue 1"),   # enqueue 1
    ("enqueue", 2, "enqueue 2"),   # enqueue 2
    ("enqueue", 3, "enqueue 3"),   # enqueue 3
    ("peek", None, "peek 1"),      # peek 1
    ("dequeue", None, "dequeue 1"),   # dequeue 1
    ("dequeue", None, "dequeue 2"),   # dequeue 2
    ("enqueue", 4, "enqueue 4"),   # enqueue 4
    ("enqueue", 5, "enqueue 5"),   # enqueue 5
    ("peek", None, "peek 3"),      # peek 3
    ("enqueue", 6, "enqueue 6"),   # enqueue 6
    ("enqueue", 7, "enqueue 7"),   # enqueue 7
    ("enqueue", 8, "enqueue 8"),   # enqueue 8
    ("enqueue", 9, "enqueue 9"),   # enqueue 9
    ("enqueue", 10, "enqueue 10"),  # enqueue 10
    ("enqueue", 11, "enqueue None"),  # enqueue None (queue is full)
    ("dequeue", None, "dequeue 3"),   # dequeue 3
    ("dequeue", None, "dequeue 4"),   # dequeue 4
    ("dequeue", None, "dequeue 5"),   # dequeue 5
    ("dequeue", None, "dequeue 6"),   # dequeue 6
    ("dequeue", None, "dequeue 7"),   # dequeue 7
    ("dequeue", None, "dequeue 8"),   # dequeue 8
    ("dequeue", None, "dequeue 9"),   # dequeue 9
    ("dequeue", None, "dequeue 10"),  # dequeue 10
    ("dequeue", None, "dequeue None"),# dequeue None (queue is empty)
    ("peek", None, "peek None"),   # peek None (queue is empty)
    ("enqueue", 11, "enqueue 11"),  # enqueue 11
    ("peek", None, "peek 11"),     # peek 11
    ("dequeue", None, "dequeue 11"),  # dequeue 11
    ("enqueue", 12, "enqueue 12"),  # enqueue 12
    ("enqueue", 13, "enqueue 13"),  # enqueue 13
    ("enqueue", 14, "enqueue 14"),  # enqueue 14
    ("enqueue", 15, "enqueue 15"),  # enqueue 15
    ("enqueue", 16, "enqueue 16"),  # enqueue 16
    ("enqueue", 17, "enqueue 17"),  # enqueue 17
    ("enqueue", 18, "enqueue 18"),  # enqueue 18
    ("enqueue", 19, "enqueue 19"),  # enqueue 19
    ("enqueue", 20, "enqueue 20"),  # enqueue 20
    ("enqueue", 21, "enqueue None"),  # enqueue None (queue is full)
    ("enqueue", 22, "enqueue None"),  # enqueue None (queue is full)
]


MyListArray = CircularQueueArray(10)
MyListLinkedList = CircularQueueLinkedList(10)

for operation, value, expected_output in operations:
    if operation == "enqueue":
        result_array = MyListArray.enqueue(value)
        result_linked_list = MyListLinkedList.enqueue(value)
    elif operation == "dequeue":
        result_array = MyListArray.dequeue()
        result_linked_list = MyListLinkedList.dequeue()
    elif operation == "peek":
        result_array = MyListArray.peek()
        result_linked_list = MyListLinkedList.peek()
    
    # Check if the result matches the expected output
    if result_array == expected_output and result_linked_list == expected_output:
        print("Test: Success")
        #print(f"    |Array: {result_array}\n    |linked List: {result_linked_list}")
    else:
        print("Test: Fail")
        print(" ", expected_output)
        print(f"    |Array: {result_array}\n    |linked List: {result_linked_list}")