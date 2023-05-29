class priorityqueue:
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
            greatest = i 
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and self.array[left_child][1] > self.array[greatest][1]:
                greatest = left_child

            if right_child < n and self.array[right_child][1] > self.array[greatest][1]:
                greatest = right_child

            if greatest != i:
                self.array[i], self.array[greatest] = self.array[greatest], self.array[i]
                i = greatest
            else:
                break
    
    def heapify_up(self,i):
        while i > 0:
            parent = (i-1) // 2
            
            if self.array[parent][1] < self.array[i][1]:
                self.array[parent], self.array[i] = self.array[i], self.array[parent]
                i = parent
            else:
                break

    def insert(self,x,weight): 
        #insert x into the existing heap
        self.array.append((x,weight))
        #heapify to maintain the heap property
        self.heapify_up(len(self.array)-1)

    def remove(self):
        if len(self.array) == 0:
            return "Queue is empty, cannot remove"
        #remove the root and move the "final" element to the root position
        self.array[0] = self.array.pop()
        #heapify to maintain the heap property
        self.heapify_down(0, len(self.array))


my_queue = priorityqueue()
my_queue.insert('a',100)
my_queue.insert('b',10)
my_queue.insert('c',102)
my_queue.insert('d',90)
print(my_queue.array)
my_queue.remove()
print(my_queue.array)