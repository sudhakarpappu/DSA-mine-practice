class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def create_binary_tree_from_list(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        current = queue.pop(0)

        if i < len(arr):
            current.left = TreeNode(arr[i])
            queue.append(current.left)
            i += 1

        if i < len(arr):
            current.right = TreeNode(arr[i])
            queue.append(current.right)
            i += 1

    return root

# Inorder Traversal for printing
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Example usage
arr = [1, 2, 3, 4, 5, 6]
tree_root = create_binary_tree_from_list(arr)
inorder(tree_root)
