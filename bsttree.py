class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 

def create_bst(root,v):
    if root is None:
        return TreeNode(v)
    if root.val>v:
        root.left=create_bst(root.left,v)
    else:
        root.right=create_bst(root.right,v)
    return root 

def incsertarr(arr):
    root=None 
    for i in arr:
        root=create_bst(root,i)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

arr = [10, 5, 15, 3, 7, 12, 18]
bst_root = incsertarr(arr)
inorder(bst_root)
        