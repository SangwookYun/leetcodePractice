from TreeNode import TreeNode
class Solution:
    def hasPathSum(self, root, targetSum):
        
        def dfs(node, cur_sum):
            if not node:
                return False
        
            cur_sum +=node.val

            if not node.left and not node.right:
                return targetSum == cur_sum
            
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)  
         
        return dfs(root,0)

if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)

    root1.left = root2
    # root1.right = root3
    
    #TestCase1
    print("TESTCASE1")
    print(solution.hasPathSum(root1, 1))
    print("------")

    
    # root1 = TreeNode(1)
    # root2 = TreeNode(2)
    # root3 = TreeNode(1)
    # root4 = TreeNode(2)

    # root1.left = root2

    # root3.right = root4
    
    # #TestCase2
    # print("TESTCASE2")
    # print(solution.maxDepth(root1))
    # print("------")
