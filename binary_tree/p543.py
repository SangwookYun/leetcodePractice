from hash.TreeNode import TreeNode
class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0
        if root is None:
            return 0
        else:
            # return self.recursive(root.left, ) + self.recursive(root.right)
            self.recursive(root)
            return self.maxDiameter
    
    def recursive(self, root):
        if root is None:
            return 0
        else: 
            left_height = self.recursive(root.left)
            right_height = self.recursive(root.right)
            cur_diameter = left_height + right_height
            self.maxDiameter = max(self.maxDiameter, cur_diameter)
            
            return 1 + max(left_height, right_height)
        
        
        
            
        
if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)
    

    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    
    #TestCase1
    print("TESTCASE1")
    print("PASS" if solution.diameterOfBinaryTree(root1) == 3 else "FAILED")
    print(solution.diameterOfBinaryTree(root1))
    print("------")


    root1 = TreeNode(1)
    root2 = TreeNode(2)
    

    root1.left = root2
    #TestCase2
    print("TESTCASE2")
    print("PASS" if solution.diameterOfBinaryTree(root1) == 1 else "FAILED")
    print(solution.diameterOfBinaryTree(root1))
    print("------")

