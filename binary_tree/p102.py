from TreeNode import TreeNode
class Solution:
    def levelOrder(self, root):
        ans = []
        stack = [root]
        temp_stack = []
                
        while stack:
            temp_ans = []
            while stack:
                cur = stack.pop(0)
                if cur:
                    print("cur?", cur.val)
                    if cur.left:
                        temp_stack.append(cur.left)
                    if cur.right:
                        temp_stack.append(cur.right)
                    temp_ans.append(cur.val)
            if len(temp_ans)>0:
                ans.append(temp_ans)
            stack = temp_stack[:]
            temp_stack = []

        return ans
            
               
            
            






if __name__ == "__main__":
    # Test Case1

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)

    root1.right = root2
    root2.left = root3

    # Test Case2
    root4 = TreeNode(None)

    # Test Case3
    root5 = TreeNode(3)
    root6 = TreeNode(9)
    root7 = TreeNode(20)
    root8 = TreeNode(15)
    root9 = TreeNode(7)
    root5.left = root6
    root5.right = root7
    root7.left = root8
    root7.right = root9

    solution = Solution()
    # solution1 = solution.levelOrder(root1)
    # print(solution1)
    solution2 = solution.levelOrder(root4)
    print(solution2)
    solution3 = solution.levelOrder(root5)
    print(solution3)

    # solution4 = solution.levelOrder(root1)
    # print(solution4)
    # solution5 = solution.levelOrder(root4)
    # print(solution5)
    # solution6 = solution.levelOrder(root5)
    # print(solution6)
