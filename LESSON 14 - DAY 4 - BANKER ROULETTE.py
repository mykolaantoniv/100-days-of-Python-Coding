names = names_string.split(", ")

import random
  
participens = len(names)
random_number = (random.randint(0, participens -1))
host = names[random_number]
print(f"{host} is going to buy the meal today!")