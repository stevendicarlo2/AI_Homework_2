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

def check_if_solvable(puzzle):
    puzzle_list = convert_puzzle_to_list(puzzle)
    inversions = 0
    for i in range(len(puzzle_list)):
        for j in range(i+1, len(puzzle_list), 1):
            a = puzzle_list[i]
            b = puzzle_list[j]
            if a != 0 and b != 0 and a > b:
                inversions += 1
    return inversions%2 == 1

def convert_puzzle_to_list(puzzle):
    ret_list = []
    for row in range(3):
        for col in range(3):
            ret_list.append(puzzle[row][col])
    return ret_list

puzzle = generate_random()
correct = [[1,2,3],[8,0,4],[7,6,5]]
# print(puzzle)
# print(check_if_solvable(puzzle))
print(correct)
print(check_if_solvable(correct))


