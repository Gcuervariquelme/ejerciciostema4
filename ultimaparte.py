class Node:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None

def insert(root, name, is_hero):
    if root is None:
        return Node(name, is_hero)
    if name < root.name:
        root.left = insert(root.left, name, is_hero)
    elif name > root.name:
        root.right = insert(root.right, name, is_hero)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        if not root.is_hero:
            print(root.name)
        in_order_traversal(root.right)

def starts_with_C(root):
    if root:
        starts_with_C(root.left)
        if root.name.startswith('C'):
            print(root.name)
        starts_with_C(root.right)

def count_superheroes(root):
    count = 0
    if root:
        count += count_superheroes(root.left)
        if root.is_hero:
            count += 1
        count += count_superheroes(root.right)
    return count

def find_and_modify(root, target_name, new_name):
    if root:
        if root.name == target_name:
            root.name = new_name
        find_and_modify(root.left, target_name, new_name)
        find_and_modify(root.right, target_name, new_name)

def reverse_order_traversal(root):
    if root:
        reverse_order_traversal(root.right)
        print(root.name)
        reverse_order_traversal(root.left)

# Create the tree
root = None
root = insert(root, "Iron Man", True)
root = insert(root, "Captain America", True)
root = insert(root, "Thor", True)
root = insert(root, "Hulk", True)
root = insert(root, "Black Widow", True)
root = insert(root, "Loki", False)
root = insert(root, "Thanos", False)
root = insert(root, "Ultron", False)
root = insert(root, "Doctor Strange", True)

# List villains alphabetically
print("Villains:")
in_order_traversal(root)

# List superheroes starting with C
print("Superheroes starting with C:")
starts_with_C(root)

# Count superheroes
superheroes_count = count_superheroes(root)
print("Number of superheroes:", superheroes_count)

# Find and modify Doctor Strange's name
find_and_modify(root, "Doctor Strange", "Dr. Strange")

# List superheroes in reverse order
print("Superheroes in reverse order:")
reverse_order_traversal(root)