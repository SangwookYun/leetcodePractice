from hash.TreeNode import TreeNode

class Solution:
    def postorder_traversal_recursive(self, root):
        ans = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            traversal(root.right)
            ans.append(root.val)
        traversal(root)

        return ans

    def postorder_traversal_iterative(self, root):
        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            ans.append(cur.val)
        return ans[::-1]


if __name__ == "__main__":
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)

    root1.right = root2 
    root2.left = root3
    solution = Solution()
    solution1 = solution.postorder_traversal_recursive(root1)
    print(solution1)
    solution2 = solution.postorder_traversal_iterative(root1)
    print(solution2)
    print("WORKING!")