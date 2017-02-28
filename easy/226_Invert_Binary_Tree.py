"""
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
question : is it a balanced tree?
swap left node value with right until all nodes are visited. either BFS or DFS will work
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.swap(root)
        return root

    def swap(self,root):
        if root is None:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)


def test():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    sol = Solution()
    root = sol.invertTree(root)
    print_tree(root)

def print_tree(root):
    if root is None:
        return

    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

test()