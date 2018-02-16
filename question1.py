# Steven DiCarlo
# Yaser Qazi


import random
import queue

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

def get_heuristic(puzzle):
    goal = [[1,2,3],[8,0,4],[7,6,5]]
    incorrect_squares = 0
    for row in range(3):
        for col in range(3):
            if puzzle[row][col] != goal[row][col]:
                incorrect_squares += 1
    return incorrect_squares

def convert_puzzle_to_list(puzzle):
    ret_list = []
    for row in range(3):
        for col in range(3):
            ret_list.append(puzzle[row][col])
    return ret_list

def get_all_successors(puzzle):
    if puzzle[0][0] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[0][0] = new_puzzle_1[0][1]
        new_puzzle_1[0][1] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[0][0] = new_puzzle_2[1][0]
        new_puzzle_2[1][0] = 0
        return [new_puzzle_1, new_puzzle_2]
    elif puzzle[0][1] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[0][1] = new_puzzle_1[0][0]
        new_puzzle_1[0][0] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[0][1] = new_puzzle_2[0][2]
        new_puzzle_2[0][2] = 0
        new_puzzle_3 = deep_copy(puzzle)
        new_puzzle_3[0][1] = new_puzzle_3[1][1]
        new_puzzle_3[1][1] = 0
        return [new_puzzle_1, new_puzzle_2, new_puzzle_3]
    elif puzzle[0][2] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[0][2] = new_puzzle_1[0][1]
        new_puzzle_1[0][1] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[0][2] = new_puzzle_2[1][2]
        new_puzzle_2[1][2] = 0
        return [new_puzzle_1, new_puzzle_2]
    elif puzzle[1][0] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[1][0] = new_puzzle_1[0][0]
        new_puzzle_1[0][0] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[1][0] = new_puzzle_2[2][0]
        new_puzzle_2[2][0] = 0
        new_puzzle_3 = deep_copy(puzzle)
        new_puzzle_3[1][0] = new_puzzle_3[1][1]
        new_puzzle_3[1][1] = 0
        return [new_puzzle_1, new_puzzle_2, new_puzzle_3]
    elif puzzle[1][1] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[1][1] = new_puzzle_1[0][1]
        new_puzzle_1[0][1] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[1][1] = new_puzzle_2[1][0]
        new_puzzle_2[1][0] = 0
        new_puzzle_3 = deep_copy(puzzle)
        new_puzzle_3[1][1] = new_puzzle_3[1][2]
        new_puzzle_3[1][2] = 0
        new_puzzle_4 = deep_copy(puzzle)
        new_puzzle_4[1][1] = new_puzzle_4[2][1]
        new_puzzle_4[2][1] = 0
        return [new_puzzle_1, new_puzzle_2, new_puzzle_3, new_puzzle_4]
    elif puzzle[1][2] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[1][2] = new_puzzle_1[2][2]
        new_puzzle_1[2][2] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[1][2] = new_puzzle_2[0][2]
        new_puzzle_2[0][2] = 0
        new_puzzle_3 = deep_copy(puzzle)
        new_puzzle_3[1][2] = new_puzzle_3[1][1]
        new_puzzle_3[1][1] = 0
        return [new_puzzle_1, new_puzzle_2, new_puzzle_3]
    elif puzzle[2][0] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[2][0] = new_puzzle_1[1][0]
        new_puzzle_1[1][0] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[2][0] = new_puzzle_2[2][1]
        new_puzzle_2[2][1] = 0
        return [new_puzzle_1, new_puzzle_2]
    elif puzzle[2][1] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[2][1] = new_puzzle_1[2][2]
        new_puzzle_1[2][2] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[2][1] = new_puzzle_2[2][0]
        new_puzzle_2[2][0] = 0
        new_puzzle_3 = deep_copy(puzzle)
        new_puzzle_3[2][1] = new_puzzle_3[1][1]
        new_puzzle_3[1][1] = 0
        return [new_puzzle_1, new_puzzle_2, new_puzzle_3]
    elif puzzle[2][2] == 0:
        new_puzzle_1 = deep_copy(puzzle)
        new_puzzle_1[2][2] = new_puzzle_1[2][1]
        new_puzzle_1[2][1] = 0
        new_puzzle_2 = deep_copy(puzzle)
        new_puzzle_2[2][2] = new_puzzle_2[1][2]
        new_puzzle_2[1][2] = 0
        return [new_puzzle_1, new_puzzle_2]

def deep_copy(puzzle):
    new_copy = [[],[],[]]
    for row in range(3):
        for col in range(3):
            new_copy[row].append(puzzle[row][col])
    return new_copy

def solve(a,b,c,d,e,f,g,h,i):
    puzzle = [[a,b,c],[d,e,f],[g,h,i]]
    if not check_if_solvable(puzzle):
        return False
    pq = queue.PriorityQueue()
    priority = get_heuristic(puzzle)
    pq.put((priority, [puzzle]))
    solution = our_solve(pq)
    if solution[0]:
        print_string = convert_chain_to_string(solution[1])
        print(print_string)
        print("This solution took " + str(len(solution[1])-1) + " steps")
    else:
        return False

def deep_copy_puzzle_chain(chain):
    new_chain = []
    for puzzle in chain:
        puzzle_copy = deep_copy(puzzle)
        new_chain.append(puzzle_copy)
    return new_chain

def our_solve(pq):
    if pq.empty():
        return (False, [])
    puzzle_tuple = pq.get()
    priority = puzzle_tuple[0]
    puzzle_chain = puzzle_tuple[1]
    puzzle = puzzle_chain[-1]
    if check_goal_state(puzzle):
        return (True, puzzle_chain)
    successors = get_all_successors(puzzle)
    for successor in successors:
        puzzle_heuristic = get_heuristic(puzzle)
        depth = priority-puzzle_heuristic
        heuristic = get_heuristic(successor) + depth + 1
        chain_copy = deep_copy_puzzle_chain(puzzle_chain)
        chain_copy.append(successor)
        pq.put((heuristic, chain_copy))
    return our_solve(pq)


def convert_chain_to_string(chain):
    ret_string = ""
    for step in chain:
        ret_string = ret_string + convert_puzzle_to_string(step) + "\n"
    return ret_string


def convert_puzzle_to_string(puzzle):
    ret_string = ""
    ret_string = ret_string + str(puzzle[0]) + "\n" + str(puzzle[1]) + "\n" + str(puzzle[2]) + "\n"
    return ret_string
solve(8,1,2,0,4,3,7,6,5)


