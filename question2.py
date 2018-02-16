# Steven DiCarlo
# Yaser Qazi

class Node:
    statement = []
    parent = None
    left = None
    right = None

    def to_string(self, depth, decorator):
        ret_string = str(depth) + decorator + "\t" + str(self.statement) + "\n"
        if self.left is not None and self.right is None:
            ret_string = ret_string + self.left.to_string(depth+1, decorator)
        elif self.left is not None and self.right is not None:
            ret_string = ret_string + self.left.to_string(depth + 1, decorator + "L")
        if self.right is not None:
            ret_string = ret_string + self.right.to_string(depth+1, decorator + "R")
        return ret_string

def make_original_tree(list_of_statements):
    if len(list_of_statements) == 0:
        return
    root_node = Node()
    root_node.statement = list_of_statements[0].split(" ")
    temp_node = root_node
    for statement in list_of_statements[1:]:
        statement = statement.split(" ")
        new_node = Node()
        new_node.statement = statement
        new_node.parent = temp_node
        temp_node.left = new_node
        temp_node = new_node
    print(root_node.to_string(0, ""))

def and_rule(start_node):
    if "AND" not in start_node.statement:
        return
    index = start_node.statement.index("AND")
    first_part = start_node.statement[:index]
    second_part = start_node.statement[index+1:]
    new_node1 = Node()
    new_node1.statement = first_part
    new_node2 = Node()
    new_node2.statement = second_part
    propagate_in_order(start_node, new_node1, new_node2)


def deep_copy(node):
    new_node = Node()
    new_node.statement = node.statement
    new_node.left = node.left
    new_node.right = node.right
    new_node.parent = node.parent

def propagate_in_order(start_node, node1, node2):
    if start_node is None:
        return
    if start_node.left is None:
        node1.parent = start_node
        start_node.left = node1
        node2.parent = node1
        node1.left = node2
        return
    else:
        propagate_in_order(start_node.left, node1, node2)
        propagate_in_order(start_node.right, node1, node2)

def propagate_split(start_node, node1, node2):
    if start_node is None:
        return
    if start_node.left is None:
        node1.parent = start_node
        start_node.left = node1
        node2.parent = start_node
        start_node.right = node2
        return
    else:
        propagate_in_order(start_node.left, node1, node2)
        propagate_in_order(start_node.right, node1, node2)

def check_if_contradictory(statement1, statement2):
    if not ((len(statement1) == 1 and len(statement2) == 2) or (len(statement1) == 2 and len(statement2) == 1)):
        return False
    if len(statement1) == 1:
        ret_val = True
        ret_val = ret_val and statement2[0] == "NOT"
        ret_val = ret_val and statement1[0] == statement2[1]
        ret_val = ret_val and statement1[0][0].isupper() and statement1[0][1].islower()
        return ret_val
    else:
        ret_val = True
        ret_val = ret_val and statement1[0] == "NOT"
        ret_val = ret_val and statement2[0] == statement1[1]
        ret_val = ret_val and statement2[0][0].isupper() and statement2[0][1].islower()
        return ret_val

def check_if_contradictory_above(node):
    above_node = node.parent
    while above_node is not None:
        contradiction = check_if_contradictory(node.statement, above_node.statement)
        if contradiction:
            return True
        else:
            above_node = above_node.parent
    return False


print(check_if_contradictory(["NOT", "Pd"], ["Pd"]))