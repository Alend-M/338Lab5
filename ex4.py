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
    
    def peek(self):  
        if not self.is_empty():
            return self.elements[-1]
        else:
            return None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.head == self.tail:
            dequeued_item = self.head.data
            self.head = self.tail = None
            return dequeued_item
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            dequeued_item = self.tail.data
            self.tail = current
            self.tail.next = None
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
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tail.value



#Function to generate a list of random 1000 tasks, 
# 1 = enqueue (probability 0.7), 0 = dequeue (probability 0.3)
def generate_tasks(n):
    instances = random.choices([0, 1], weights=[0.3, 0.7], k=n)
    return instances

# Function to measure the performance of queue implementations
def measure_performance(q_class):
    q = q_class()
    instances = generate_tasks(10000)
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

# def test_list():
#     queue = LinkedListQueue()

#     # Enqueue elements
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)

#     # Print the queue
#     current = queue.head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

#     # Dequeue elements
#     print("Dequeued item:", queue.dequeue())
#     print("Dequeued item:", queue.dequeue())
#     print("Dequeued item:", queue.dequeue())
#     print("Dequeued item:", queue.dequeue())

#     # Print the remaining queue
#     current = queue.head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")


if __name__ == '__main__':

    print("Performance of Array Queue:")
    time_array = timeit.timeit(lambda: measure_performance(ArrayQueue), number=100)
    print("Time taken:", time_array)
    print(measure_performance(ArrayQueue))

    print("\nPerformance of Linked List Queue:")
    time_list = timeit.timeit(lambda: measure_performance(LinkedListQueue), number=100)
    print("Time taken:", time_list)
    print(measure_performance(LinkedListQueue)) #this stuff isnt related to the stuff below, its separate measurements

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
    plt.xlabel('Time taken (s)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Times for ArrayQueue and LinkedListQueue')
    plt.legend()
    plt.show()


#Discuss the result:
'''
ArrayQueue showed lower average times than LinkedListQueue, but Linked List Queue seems to perform better overall, as it 
had a higher frequency of taking shorter times.'''