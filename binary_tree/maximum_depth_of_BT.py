from TreeNode import TreeNode


class Solution:
    def maxDepth_topdown(self, root):
        self.cur_max = 0

        def traversal(root, level):
            if not root:
                self.cur_max = max(self.cur_max, level)
                return
            traversal(root.left, level+1)
            traversal(root.right, level+1)
        traversal(root, 0)

        return self.cur_max

    def maxDepth_bottomup(self, root):
        pass


if __name__ == "__main__":
    root6 = TreeNode(100)
    root5 = TreeNode(7, root6)
    root4 = TreeNode(15)
    root3 = TreeNode(20, root4, root5)
    root2 = TreeNode(9)
    root1 = TreeNode(3, root2, root3)
    sol = Solution()
    print("## TOPDOWN ##")
    print(sol.maxDepth_topdown(root1))

    print(sol.maxDepth_bottomup(root1))
