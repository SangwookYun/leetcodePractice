from TreeNode import TreeNode

class Solution:
    def isSymmetric(self, root):
        if not root:
            return

        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val is not root2.val:
            return False
        
        if not self.isMirror(root1.left, root2.right):
            return False
        if not self.isMirror(root1.right, root2.left):
            return False



if __name__ == "__main__":
    # root6 = TreeNode(100)
    # root5 = TreeNode(7, root6)
    # root4 = TreeNode(15)
    # root3 = TreeNode(20, root4, root5)
    # root2 = TreeNode(9)
    # root1 = TreeNode(3, root2, root3)
    # sol = Solution()

    root5 = TreeNode(3)
    root4 = TreeNode(3)
    root3 = TreeNode(2, root4)
    root2 = TreeNode(2, None, root5)
    root1 = TreeNode(1, root2, root3)
    sol = Solution()

    print(sol.isSymmetric(root1))
    
