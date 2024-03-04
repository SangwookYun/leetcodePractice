from TreeNode import TreeNode
class Solution:
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)





        
            
        
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
    print(solution.isSymmetric(root1))
    print("------")

    
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(1)
    root4 = TreeNode(2)

    root1.left = root2

    root3.right = root4
    
    #TestCase2
    print("TESTCASE2")
    print(solution.isSymmetric(root1))
    print("------")
