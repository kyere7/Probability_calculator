import copy
import random


class Hat:
  def __init__(self, **kwargs):
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
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)

    exptd_ball_list = list()
    for key, value in expected_balls.items():
      for x in range(value):
        exptd_ball_list.append(key)

    if ContainsBall(exptd_ball_list, balls):
      count += 1

  probability = count / num_experiments
  return probability


def ContainsBall(expected_balls, actual_balls):
  for b in expected_balls:
    if b in actual_balls:
      actual_balls.remove(b)
    else:
      return False
  return True