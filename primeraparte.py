import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        self._balance(node)

    def _balance(self, node):
        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if self._get_balance_factor(node.left) < 0:
                self._rotate_left(node.left)
            self._rotate_right(node)
        elif balance_factor < -1:
            if self._get_balance_factor(node.right) > 0:
                self._rotate_right(node.right)
            self._rotate_left(node)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        if self.root == z:
            self.root = y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        if self.root == z:
            self.root = y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def pre_order_traversal(self):
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.data, end=" ")
            self._in_order_traversal(node.right)

    def post_order_traversal(self):
        self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        if node:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.data, end=" ")

    def level_order_traversal(self):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node or node.data == data:
            return node

        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def delete(self, data):
        if not self.root:
            return

        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._get_min_value_node(node.right)
                node.data = successor.data
                node.right = self._delete(node.right, successor.data)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        self._balance(node)
        return node

    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def get_subtree_height(self, side):
        if side == "left":
            return self._get_height(self.root.left)
        elif side == "right":
            return self._get_height(self.root.right)
        else:
            return None

    def count_occurrences(self, data):
        return self._count_occurrences(self.root, data)

    def _count_occurrences(self, node, data):
        if not node:
            return 0

        count = 0
        if node.data == data:
            count += 1

        count += self._count_occurrences(node.left, data)
        count += self._count_occurrences(node.right, data)
        return count

    def count_parity(self):
        even_count = self._count_parity(self.root, True)
        odd_count = self._count_parity(self.root, False)
        return even_count, odd_count

    def _count_parity(self, node, is_even):
        if not node:
            return 0

        count = 0
        if (node.data % 2 == 0 and is_even) or (node.data % 2 != 0 and not is_even):
            count += 1

        count += self._count_parity(node.left, is_even)
        count += self._count_parity(node.right, is_even)
        return count


# Generate 1000 random numbers
numbers = random.sample(range(1, 10001), 1000)

# Create an AVL tree
tree = AVLTree()

# Insert the numbers into the tree
for number in numbers:
    tree.insert(number)

# Perform pre-order traversal
print("Pre-order traversal:")
tree.pre_order_traversal()
print()

# Perform in-order traversal
print("In-order traversal:")
tree.in_order_traversal()
print()

# Perform post-order traversal
print("Post-order traversal:")
tree.post_order_traversal()
print()

# Perform level-order traversal
print("Level-order traversal:")
tree.level_order_traversal()
print()

# Search for a number in the tree
number_to_search = 42
if tree.search(number_to_search):
    print(f"{number_to_search} is present in the tree")
else:
    print(f"{number_to_search} is not present in the tree")

# Delete three values from the tree
values_to_delete = [42, 123, 789]
for value in values_to_delete:
    tree.delete(value)

# Get the height of the left and right subtrees
left_subtree_height = tree.get_subtree_height("left")
right_subtree_height = tree.get_subtree_height("right")
print(f"Height of the left subtree: {left_subtree_height}")
print(f"Height of the right subtree: {right_subtree_height}")

# Count the occurrences of a number in the tree
number_to_count = 999
occurrences = tree.count_occurrences(number_to_count)
print(f"Number of occurrences of {number_to_count}: {occurrences}")

# Count the number of even and odd numbers in the tree
even_count, odd_count = tree.count_parity()
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")