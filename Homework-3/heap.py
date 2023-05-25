class heap:
    def __init__(self):
        self.array = []
        
    def heapify(self):
        n = len(self.array)
        start = (n // 2) - 1  # Start from the last parent node
        for i in range(start, -1, -1): #Loop through each other parent node
            self.heapify_down(i, n)

    def heapify_down(self, i, n):
        #O(logn)
        while True: 
            smallest = i 
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and self.array[left_child] < self.array[smallest]:
                smallest = left_child

            if right_child < n and self.array[right_child] < self.array[smallest]:
                smallest = right_child

            if smallest != i:
                self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
                i = smallest
            else:
                break
    
    def heapify_up(self,i):
        while i > 0:
            parent = (i-1) // 2
            
            if self.array[parent] > self.array[i]:
                self.array[parent], self.array[i] = self.array[i], self.array[parent]
                i = parent
            else:
                break

    def insert(self,x): 
        #insert x into the existing heap
        self.array.append(x)
        #heapify to maintain the heap property
        self.heapify_up(len(self.array)-1)

    def remove(self):
        if len(self.array) == 0:
            return "Queue is empty, cannot remove"
        #remove the root and move the "final" element to the root position
        self.array[0] = self.array.pop()
        #heapify to maintain the heap property
        self.heapify_down(0, len(self.array))


my_heap = heap()
my_heap.array = [17,3,2,100,19,7,25,1,36]
my_heap.heapify()
print(my_heap.array)
my_heap.remove()
print(my_heap.array)
my_heap.insert(1)
print(my_heap.array)
