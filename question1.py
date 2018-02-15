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

def check_goal_state(puzzle):
    goal = [[1,2,3],[8,0,4],[7,6,5]]
    return goal == puzzle

puzzle = generate_random()
correct = [[1,2,3],[8,0,4],[7,6,5]]
print(puzzle)
print(check_goal_state(puzzle))
print(correct)
print(check_goal_state(correct))


