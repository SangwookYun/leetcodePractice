from TreeNode import TreeNode
class Solution:
    def maxDepth(self, root):
        self.max_level = 0
        if root is None:
            return 0
        
        self.traverse(root, 0)

        return self.max_level

        
    def traverse(self, root, cur_level):
        if root is None:
            return
        cur_level +=1

        self.max_level = max(self.max_level, cur_level)
        if root.left:            
            self.traverse(root.left, cur_level)
        if root.right:
            self.traverse(root.right, cur_level)



        
            
        
if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(1)
    root5 = TreeNode(2)
    root6 = TreeNode(3)

    root1.left = root2
    root1.right = root3
    root4.left = root5
    root4.right = root6
    
    #TestCase1
    print("TESTCASE1")
    print(solution.maxDepth(root1))
    print("------")

    
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(1)
    root4 = TreeNode(2)

    root1.left = root2

    root3.right = root4
    
    #TestCase2
    print("TESTCASE2")
    print(solution.maxDepth(root1))
    print("------")
