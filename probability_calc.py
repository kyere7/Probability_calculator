import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key, val in kwargs:
            for index in range(val):
                self.contents.append(key)
    
    def draw(self, number):
        all_balls_removed = []
        if (number > len(self.contents)):
            return self.contents
        for i in range(number):
            balls_removed= self.contents.pop(int(random.random()*len(self.contents)))
            all_balls_removed.append(balls_removed)
        return all_balls_removed



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
