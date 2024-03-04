from TreeNode import TreeNode
class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        cur = []
        output = []
        def checkCur(nums):
            odd_set = set()
            
            for num in nums:
                if num in odd_set:
                    odd_set.remove(num)
                else:
                    odd_set.add(num)
            
            if len(odd_set) > 1:
                return False

            return True
        def dfs(node):
            nonlocal cur
            if node is None:
                return
            
            cur.append(node.val)
            if node.left is None and node.right is None:
                output.append(checkCur(cur))
            elif node.left or node.right:
                dfs(node.left)
            
                dfs(node.right)
                
            cur.pop()
        
        dfs(root)
        print(output)

        return output.count(True)
    
if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(2)
    root2 = TreeNode(3)
    root3 = TreeNode(1)
    root4 = TreeNode(3)
    root5 = TreeNode(1)
    root6 = TreeNode(1)

    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    root3.right= root6
    
    #TestCase1
    print("TESTCASE1")
    print("PASS" if solution.pseudoPalindromicPaths(root1) == 2 else "FAILED")
    # print(solution.pseudoPalindromicPaths(root1))
    print("------")
    
    
    root1 = TreeNode(2)
    root2 = TreeNode(1)
    root3 = TreeNode(1)
    root4 = TreeNode(1)
    root5 = TreeNode(3)
    root6 = TreeNode(1)
    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    root5.right = root6
    
    # #TestCase2
    # print("TESTCASE2")
    # print("PASS" if solution.pseudoPalindromicPaths(root1) == 1 else "FAILED")
    # print(solution.pseudoPalindromicPaths(root1))
    # print("------")
    
    # root1 = TreeNode(9)
    # #TestCase3
    # print("TESTCASE3")
    # print("PASS" if solution.pseudoPalindromicPaths(root1) == 1 else "FAILED")
    # print(solution.pseudoPalindromicPaths(root1))
    # print("------")
