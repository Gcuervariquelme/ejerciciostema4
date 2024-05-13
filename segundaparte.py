class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            node = Node(char)
            stack.append(node)
        else:
            right_node = stack.pop()
            left_node = stack.pop()
            node = Node(char)
            node.left = left_node
            node.right = right_node
            stack.append(node)
    return stack.pop()

expression = "3+4*2/(1-5)"
expression_tree = build_expression_tree(expression)