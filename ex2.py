import random
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)
        self.queue = merge_sort(self.queue)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

class SortedPriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        # Find the index where the new element should be inserted
        index = 0
        while index < len(self.queue) and self.queue[index] < data:
            index += 1
        self.queue.insert(index, data)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)  

#Function to generate a list of random 1000 tasks, 
# 1 = enqueue (probability 0.7), 0 = dequeue (probability 0.3)
def generate_tasks(n):
    instances = random.choices([0, 1], weights=[0.3, 0.7], k=n)
    return instances

# Function to measure the performance of priority queue implementations
def measure_performance(pq_class):
    pq = pq_class()
    instances = generate_tasks(1000)
    for i in instances:
        if instances[i] == 1:
            pq.enqueue(random.randint(0,100))
        #elif instances[i] == 0:
            #pq.dequeue()
    return pq


if __name__ == '__main__':

    print("Performance of Regular Priority Queue Enqueue:")
    time_regular = timeit.timeit(lambda: measure_performance(PriorityQueue), number=100)
    print("Time taken:", time_regular)
    #print(measure_performance(PriorityQueue))

    print("\nPerformance of Sorted Priority Enqueue:")
    time_sorted = timeit.timeit(lambda: measure_performance(SortedPriorityQueue), number=100)
    print("Time taken:", time_sorted)
    #print(measure_performance(SortedPriorityQueue))




'''The second implementation (SortedPriotiyQueue) is faster. Its time complexity to enqueue is O(n) 
in the worst case while the first implementation's time complexity to enqueue is O(nlogn). 
The time complexity of merge sort with recurssion is O(nlogn), PriorityQueue's complexity
is the same since it uses merge sort. SortedPriorityQueue just finds the index where the 
new element should be placed. In it's worse case, it iterates though the whole queue n times.'''