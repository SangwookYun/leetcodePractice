from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root):
        ans = []
        stack = [[root]]

        while stack:
            nodes = stack.pop()
            next_nodes = []
            cur_vals = []
            for node in nodes:
                if node:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
                    cur_vals.append(node.val)

            if len(next_nodes) != 0:
                stack.append(next_nodes)
            if len(cur_vals) != 0:
                ans.append(cur_vals)

        return ans


if __name__ == "__main__":
    print("WORKING!")

    root5 = TreeNode(7)
    root4 = TreeNode(15)
    root3 = TreeNode(20, root4, root5)
    root2 = TreeNode(9)
    root1 = TreeNode(3, root2, root3)
    sol = Solution()
    print(sol.levelOrder(root1))
