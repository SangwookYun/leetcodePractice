from TreeNode import TreeNode


class Solution:
    def preorder_traversal_recursive(self, root):
        ans = []

        def traversal(root):
            if not root:
                return
            ans.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)

        return ans

    def preorder_traversal_iterative(self, root):
        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)

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
    solution1 = solution.preorder_traversal_recursive(root1)
    print(solution1)
    solution2 = solution.preorder_traversal_recursive(root4)
    print(solution2)
    solution3 = solution.preorder_traversal_recursive(root5)
    print(solution3)

    solution4 = solution.preorder_traversal_iterative(root1)
    print(solution4)
    solution5 = solution.preorder_traversal_iterative(root4)
    print(solution5)
    solution6 = solution.preorder_traversal_iterative(root5)
    print(solution6)
