from TreeNode import TreeNode
class Solution:
    def binaryTreePaths(self, root):
        cur = []
        output = []

        def dfs(node):
            nonlocal cur
            if node is None:
                return
            cur.append(str(node.val))
            if node.left is None and node.right is None:
                output.append("->".join(cur))
            else:                
                
                dfs(node.left)
                dfs(node.right)

            cur.pop()
        dfs(root)
        return output

if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(5)

    root1.left = root2
    root1.right = root3
    root2.right = root4
    #TestCase1
    print("TESTCASE1")
    # print("PASS" if solution.binaryTreePaths(root1) == 2 else "FAILED")
    print(solution.binaryTreePaths(root1))
    print("------")
    
    
    root1 = TreeNode(1)
    
    # # #TestCase2
    # print("TESTCASE2")
    # # print("PASS" if solution.binaryTreePaths(root1) == 1 else "FAILED")
    # print(solution.binaryTreePaths(root1))
    # # print("------")