import random

#printing a random in range of 0 to 1 including 0 and excluding 1
for i in range(0,10):
    print(random.random())

#Generating random number in certain interval
for i in range(10):
    print(random.uniform(4,9))

#Generating a set of numbers whose mean and standard deviation is predefined
for i in range(10):
    print(random.normalvariate(19,4))

random.seed(123)
for i in range(0,10):
    print(random.randint(0,1000))

