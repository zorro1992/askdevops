import random

# randrange will give different output expect the last number mentioned
# that is 5 in the below example
print(random.randrange(5))

# randint will give different output including last number mentioned in
# the range . In the below example 6
print(random.randint(2, 6))

# Give a float point number in range
print(random.uniform(0, 6))

number = 10
data = int(random.uniform(0, (number - 1)))
print(data)
