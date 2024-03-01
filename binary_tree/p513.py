from hash.TreeNode import TreeNode
class Solution:
    def findBottomLeftValue(self, root):
        self.ans = []
        self.maxDept = 0
        if root is None:
            return 0
        else:
            self.recursive(root, 0)
        
        print(self.ans)
        return self.ans[-1]

    def recursive(self, node, dept):
        if node is None:
            return
        else:
            print(node.val, dept, self.maxDept)
            self.recursive(node.left, dept +1)
            self.recursive(node.right,dept +1)
            if (dept>=self.maxDept and len(self.ans) ==0) or (dept > self.maxDept):
                self.ans.append(node.val)
                self.maxDept = max(self.maxDept, dept)
            return           
        
if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(2)
    root2 = TreeNode(1)
    root3 = TreeNode(3)
    

    root1.left = root2
    root1.right = root3
    
    #TestCase1
    print("TESTCASE1")
    print("PASS" if solution.findBottomLeftValue(root1) == 1 else "FAILED")
    print("------")


    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)
    root6 = TreeNode(6)
    root7 = TreeNode(7)
    

    root1.left = root2
    root1.right = root3
    root2.left = root4
    root3.left = root5
    root3.right = root6
    root5.left = root7


    #TestCase2
    print("TESTCASE2")
    print("PASS" if solution.findBottomLeftValue(root1) == 7 else "FAILED")
    print(solution.findBottomLeftValue(root1))
    print("------")


    root1 = TreeNode(0)


    #TestCase3
    print("TESTCASE2")
    print("PASS" if solution.findBottomLeftValue(root1) == 0 else "FAILED")
    print(solution.findBottomLeftValue(root1))
    print("------")


