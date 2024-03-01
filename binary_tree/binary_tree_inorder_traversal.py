from hash.TreeNode import TreeNode


class Solution:
    def inorder_traversal_recursive(self, root):
        ans = []

        def traversal(root):
            if not root:
                return
            traversal(root.left)
            ans.append(root.val)
            traversal(root.right)

        traversal(root)
        return ans

    def inorder_traversal_iterative(self, root):
        stack = []
        ans = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

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
    # solution1 = solution.inorder_traversal_recursive(root1)
    # print(solution1)
    # solution2 = solution.inorder_traversal_recursive(root4)
    # print(solution2)
    # solution3 = solution.inorder_traversal_recursive(root5)
    # print(solution3)
    solution4 = solution.inorder_traversal_iterative(root1)
    print(solution4)
    # solution5 = solution.inorder_traversal_iterative(root4)
    # print(solution5)
    # solution6 = solution.inorder_traversal_iterative(root5)
    # print(solution6)
