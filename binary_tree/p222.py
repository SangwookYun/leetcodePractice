from TreeNode import TreeNode
class Solution:
    def countNodes(self, root):
        pass

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
    root5 = TreeNode(5)

    solution = Solution()
    solution1 = solution.countNodes(root1)
    print(solution1)
    solution2 = solution.countNodes(root4)
