"""
Took 36 minutes

Using, maintain 2 queues and pre-process
O(log(n)) initialization
O(1) adoption and addition of new animal
"""

class adopt_pet:
    def __init__(self,shelter_list):
        """
        I assume we are given a list of lists/tuples representing the pets in the shelter to initialize
        pet format:  (name, species, time at shelter)
        """
        self.dog_queue = []
        self.cat_queue = []
        for pet in shelter_list:
            if pet[1] == "dog":
                self.dog_queue.append([-pet[2],pet[0]])
            else:
                self.cat_queue.append([-pet[2],pet[0]])
        self.dog_queue.sort()
        self.cat_queue.sort()
        self.dog_ptr = 0
        self.cat_ptr = 0
    
    def new_animal(self, name, species):
        if species == "dog":
            self.dog_queue.append([0,name])
        else:
            self.cat_queue.append([0,name])

    def adoption(self,name, person, species):
        if len(self.dog_queue) == self.dog_ptr and len(self.cat_queue) == self.cat_ptr:
            return "No pets left"
        elif len(self.dog_queue) == self.dog_ptr:
            adopt_cat_name = self.cat_queue[self.cat_ptr][1]
            self.cat_ptr += 1
            return (adopt_cat_name, "cat")
        elif len(self.cat_queue) == self.cat_ptr:
            adopt_dog_name = self.dog_queue[self.dog_ptr][1]
            self.dog_ptr += 1
            return (adopt_dog_name, "dog")
        elif species == "dog":
            adopt_dog_name = self.dog_queue[self.dog_ptr][1]
            self.dog_ptr += 1
            return (adopt_dog_name, "dog")
        else:
            adopt_cat_name = self.cat_queue[self.cat_ptr][1]
            self.cat_ptr += 1
            return (adopt_cat_name, "cat")
        
test = adopt_pet([
("Sadie", "dog", 4),
("Woof", "cat", 7),
("Chirpy", "dog", 2),
("Lola", "dog", 1)]
)

print(test.adoption("Bob","Person","dog"))
print(test.new_animal("Floofy", "cat"))
print(test.adoption("Sally", "person", "cat"))
print(test.adoption("Ji", "person", "cat"))
print(test.adoption("Alli", "person", "cat"))