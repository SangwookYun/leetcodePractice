from PTreeNode import PTreeNode

class Solution:
    def connect(self, root):
        queue = [root]
        ans = []
        level = 0
        if not root:
            return root
        if not root.left or not root.right:
            return queue

        while len(queue)!= 0:
            cur = queue.pop(0)
            if cur:
                ans.append(cur)
                queue.append(cur.left)
                queue.append(cur.right)

        cur = 0
        count = 0
        for idx in range(len(ans)-1):
            if cur == (2**count)-1:
                ans[idx].next = None
                count+=1
                cur=0
            else:
                ans[idx].next = ans[idx+1]
                cur+=1
        ans[len(ans)-1].next = None

        return root

        


            

if __name__=="__main__":
    print("WORKING!")
    # node15 = PTreeNode(15)
    # node14 = PTreeNode(14)
    # node13 = PTreeNode(13)
    # node12 = PTreeNode(12)
    # node11 = PTreeNode(11)
    # node10 = PTreeNode(10)
    # node9 = PTreeNode(9)
    # node8 = PTreeNode(8)

    # node7 = PTreeNode(7, node14, node15)
    # node6 = PTreeNode(6, node12, node13)
    # node5 = PTreeNode(5, node10, node11)
    # node4 = PTreeNode(4, node8, node9)
    # node3 = PTreeNode(3, node6, node7)
    # node2 = PTreeNode(2, node4, node5)
    # node1 = PTreeNode(1, node2, node3)

    node1 = PTreeNode(0)
    sol = Solution()
    sol.connect(node1)