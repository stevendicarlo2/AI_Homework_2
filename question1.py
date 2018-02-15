# Steven DiCarlo
# Yaser Qazi


import random


def generate_random():
    numbers_to_pick = [0,1,2,3,4,5,6,7,8]
    returned_puzzle = [[],[],[]]
    for row in range(3):
        for col in range(3):
            index = random.randint(0,len(numbers_to_pick)-1)
            returned_puzzle[row].append(numbers_to_pick[index])
            del numbers_to_pick[index]
    return returned_puzzle

puzzle = generate_random()
print(puzzle)


