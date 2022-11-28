import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = list()
        for key, val in kwargs.items():
            for index in range(val):
                self.contents.append(key)
    
    def draw(self, number):
        try:
            colors = random.sample(self.contents, number)
        except:
            colors = copy.deepcopy(self.contents)

        for color in colors:
            self.contents.remove(color)
        
        return colors



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for num in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_colors = hat_copy.draw(num_balls_drawn)
        xpected_balls_list = list()
        for key, val in expected_balls.items():
            xpected_balls_list.append(val)
        
        if ContainBalls(xpected_balls_list, draw_colors):
            count += 1
    
    return count / num_experiments

def ContainBalls(expected_balls, actual_balls):
    for each_b in expected_balls:
        if each_b in actual_balls:
            actual_balls.remove(each_b)
        else:
            return False
        return True
    