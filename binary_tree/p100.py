from TreeNode import TreeNode
class Solution:
    def isSameTree(self, p,q):
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        else:
            if p.val != q.val:
                return False
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
            
        
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
    print("PASS" if solution.isSameTree(root1, root4) == True else "FAILED")
    # print(solution.pseudoPalindromicPaths(root1))
    print("------")

    
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(1)
    root4 = TreeNode(2)

    root1.left = root2

    root3.right = root4
    
    #TestCase1
    print("TESTCASE1")
    print("PASS" if solution.isSameTree(root1, root3) == False else "FAILED")
    # print(solution.pseudoPalindromicPaths(root1))
    print("------")
