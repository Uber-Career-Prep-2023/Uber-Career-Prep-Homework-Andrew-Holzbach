"""
Using: Save State
O(n) time complexity for each insertion, O(n) space complexity
Took 20 minutes

"""


class Running_Median:

    def __init__(self):
        self.list = []
    
    def insert(self, new_number):
        if len(self.list) == 0:
            self.list.append(new_number)
            return new_number
        else:
            ptr = 0
            while ptr < len(self.list) and self.list[ptr] < new_number:
                ptr += 1
            self.list.insert(ptr, new_number)
            if len(self.list)%2 == 0:
                num1 = self.list[len(self.list)//2 - 1]
                num2 = self.list[len(self.list)//2]
                return (num1 + num2)/2
            else:
                return self.list[len(self.list)//2]
            
tobject = Running_Median()
tests = [(1,1), (11,6), (4,4), (15,7.5), (12,11)]
for test in tests:
    num = test[0]
    res = test[1]
    if tobject.insert(num) == res:
        print("Sucess Inserted:", num, "Median:", res)
    else:
        print("Failure Inserted:", num, "Median:", res)