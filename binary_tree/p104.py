from TreeNode import TreeNode
class Solution:
    def maxDepth(self, root):
        self.maxDepth = 0

        def traverse(node, cur_level):
            if node is None:
                self.maxDepth = max(self.maxDepth, cur_level)
                return 
            traverse(node.left, cur_level +1)
            traverse(node.right, cur_level+1)

        traverse(root, 0)
        return self.maxDepth
            
        
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
