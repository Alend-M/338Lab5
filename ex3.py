import timeit
import random
import matplotlib.pyplot as plt

class ArrayStack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)
    
    def pop(self):
       if len(self.array) == 0:
           raise IndexError("Can't pop from an empty stack.")
       return self.array.pop()
    
    def peek(self):
        return self.array[-1]

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LLStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if (self.head != None):
            popped = self.head.data
            self.head = self.head.next
            return popped
        else:
            raise IndexError("Can't pop from an empty stack.")
    
    def peek(self):
        return self.head.data

def generate_tasks():
    tasks = []
    for i in range(10000):
        number = random.randint(1, 10)
        if (number <= 7):
            tasks.append("push")
        else:
            tasks.append("pop")
    return tasks

def measure_performance(type, tasks):
    test_stack = type()
    def run_tasks():
        for task in tasks:
            if (task == "push"):
                test_stack.push(random.randint(1, 100))
            elif (task == "pop"):
                try:
                    test_stack.pop()
                except IndexError:
                    pass
    time = timeit.timeit(lambda: run_tasks(), number = 1)
    return time

tasks_list = [generate_tasks() for i in range(100)]
array_timings = [measure_performance(ArrayStack, tasks) for tasks in tasks_list]
linked_list_timings = [measure_performance(LLStack, tasks) for tasks in tasks_list]

plt.hist(array_timings, bins = 20, label = "Stack Implementation Using Array")
plt.hist(linked_list_timings, bins = 20, label = "Stack Implementation Using Linked List")
plt.title("Distribution of Different Stack Implementation Timings")
plt.xlabel("Time in Seconds")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# The generated plot showcases how an array-based stack implementation tends to require less time
# to perform operations on than a linked list-based stack implementation. It also showcases how
# there is often a larger range in regards to the time taken for the linked list implementation to
# complete its operations, while the array-based implementation takes a more consistent amount of time.