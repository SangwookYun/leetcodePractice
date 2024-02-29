from TreeNode import TreeNode
class Solution:
    def findDuplicateSubtrees(self, root):
        self.hash_table = {}
        self.ans = []
        if root is None:
            return []
        self.recursive(root)
        print("DONE")
        print(self.hash_table)
        # ans = []
        # for key, value in self.hash_table.items():
        #     if value >0:
        #         ans.append(list(key))
        # print(ans)
        # return ans
        return self.ans

    def recursive(self, node):
        if node is None:
            return
        sub_tree= []
        sub_tree.append(node)
        sub_tree.append(node.val)
        print("node val", node.val)
        if node.left:
            print("node.left.val", node.left.val)
            sub_tree.append(node.left.val)
        if node.right:
            print("node.right.val", node.right.val)
            sub_tree.append(node.right.val)
        print(sub_tree)
        print(self.hash_table)
        if tuple(sub_tree) in list(self.hash_table.keys()):
            self.hash_table[tuple(sub_tree)] +=1
            self.ans.append(node)
        else:
            self.hash_table[tuple(sub_tree)] =0
        self.recursive(node.left)
        self.recursive(node.right)




if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)

    root1.left = root2
    root1.right = root3
    root2.left = root4
    #TestCase1
    print("TESTCASE1")
    print(solution.findDuplicateSubtrees(root1))
    print("------")
    