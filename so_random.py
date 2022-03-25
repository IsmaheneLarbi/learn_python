import random

# to print the radom modules:
#print(dir(random))

# generating a number in interval [3, 7)
def my_random():
    # Random, scale, shift, return
    return 4*random.random() + 3

for i in range(10):
    print(my_random())

for i in range(10):
    print(random.uniform(3, 7))

# normal distribution : bell curve generation
# myu: mean | sigma: std
for i in range(10):
    print(random.normalvariate(4, 0.2))

# random number in an integer interval:
for i in range(20):
    print(random.randint(1, 6))

outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))
