from TreeNode import TreeNode


class Solution:
    def preorder_traversal(self, root):
        ans = []

        def traversal(root):
            if not root:
                return
            ans.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)

        return ans


if __name__ == "__main__":
    # Test Case1

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)

    root1.right = root2
    root2.left = root3

    # Test Case2
    root4 = []

    # Test Case3
    root5 = TreeNode(5)

    solution = Solution()
    solution1 = solution.preorder_traversal(root1)
    print(solution1)
    solution2 = solution.preorder_traversal(root4)
    print(solution2)
    solution3 = solution.preorder_traversal(root5)
    print(solution3)
