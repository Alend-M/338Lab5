import random
import timeit
import matplotlib.pyplot as plt


class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Insert element at the head (index 0)
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            # Remove element from the tail
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.head == self.tail:
            dequeued_item = self.head.data
            self.head = None
            self.tail = None
            return dequeued_item
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            dequeued_item = current.next.data
            current.next = None
            self.tail = current
            return dequeued_item

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count



#Function to generate a list of random 1000 tasks, 
# 1 = enqueue (probability 0.7), 0 = dequeue (probability 0.3)
def generate_tasks(n):
    instances = random.choices([0, 1], weights=[0.3, 0.7], k=n)
    return instances

# Function to measure the performance of queue implementations
def measure_performance(q_class):
    q = q_class()
    instances = generate_tasks(1000)
    for i in instances:
        if instances[i] == 1:
            q.enqueue(random.randint(0,100))
        elif instances[i] == 0:
            q.dequeue()
    #return q

def test_array():
    queue = ArrayQueue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # Print the queue
    print("Queue:", queue.items)
    # Dequeue elements
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())

    # Print the remaining queue
    print("Queue after dequeuing:", queue.items)

def test_list():
    queue = LinkedListQueue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Print the queue
    current = queue.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Dequeue elements
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())

    # Print the remaining queue
    current = queue.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == '__main__':

    print("Performance of Array Queue:")
    time_array = timeit.timeit(lambda: measure_performance(ArrayQueue), number=100)
    print("Time taken:", time_array)
    print(measure_performance(ArrayQueue))

    print("\nPerformance of Linked List Queue:")
    time_list = timeit.timeit(lambda: measure_performance(LinkedListQueue), number=100)
    print("Time taken:", time_list)
    print(measure_performance(LinkedListQueue))

    array_times = []
    list_times = []

    for _ in range (100):
        array_time = timeit.timeit(lambda: measure_performance(ArrayQueue), number=1)
        array_times.append(array_time)

        list_time = timeit.timeit(lambda: measure_performance(LinkedListQueue), number=1)
        list_times.append(list_time)
    
    # Plotting the distributions
    plt.hist(array_times, alpha=0.5, label='ArrayQueue')
    plt.hist(list_times, alpha=0.5, label='LinkedListQueue')
    plt.xlabel('Time taken')
    plt.ylabel('Frequency')
    plt.title('Distribution of Times for ArrayQueue and LinkedListQueue')
    plt.legend()
    plt.show()


#Discuss the result:
'''
ArrayQueue showed lower average times than LinkedListQueue'''


'''This is gpt's explanation:
ArrayQueue Performance:

The distribution of times for ArrayQueue implementation typically shows a relatively lower average time compared to LinkedListQueue, especially when considering enqueue operations.
ArrayQueue's enqueue operation inserts elements at the head of the array, which is relatively efficient in terms of time complexity. It doesn't require traversing the entire data structure to insert an element.
However, the dequeue operation in ArrayQueue is less efficient as it requires removing an element from the tail, which involves shifting all elements towards the end of the array, resulting in higher time complexity, especially for large arrays.
LinkedListQueue Performance:

The distribution of times for LinkedListQueue implementation generally exhibits a higher average time compared to ArrayQueue, particularly for both enqueue and dequeue operations.
LinkedListQueue's enqueue operation adds elements at the head of the linked list, which is efficient in terms of time complexity, similar to ArrayQueue.
However, the dequeue operation in LinkedListQueue, despite removing elements from the tail, involves traversing the linked list to find the second-to-last node, leading to relatively higher time complexity compared to ArrayQueue's dequeue operation.
Overall Comparison:

The choice between ArrayQueue and LinkedListQueue depends on the specific requirements of the application.
ArrayQueue may be preferable for applications where frequent insertions at the head are more common than removals from the tail, due to its more efficient enqueue operation.
LinkedListQueue may be more suitable for scenarios where frequent removals from the tail are required, as its dequeue operation may perform relatively better compared to ArrayQueue in such cases.
Moreover, LinkedListQueue can dynamically resize, which can be advantageous when the size of the queue is not known in advance and may grow or shrink dynamically.
Considerations:

It's important to note that these observations are based on the specific context of the given implementations and the nature of the operations performed. Actual performance may vary depending on factors such as the size of the data structure, hardware specifications, and implementation optimizations.
For critical applications where performance is a key concern, it's advisable to conduct thorough benchmarking and profiling to evaluate the performance characteristics under realistic workloads and scenarios.'''