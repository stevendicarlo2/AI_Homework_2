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
    

make_original_tree(["A B C D", "E F G H", "I J", "Kl"])