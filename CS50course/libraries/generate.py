# Here you are specifying that you are gonna import only the choice method from the full random library
from random import random

#You have to give a list to random.choice() in braclets
coin = random.choice(["heads", "tails"])
print(coin)
