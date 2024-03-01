from hash.TreeNode import TreeNode
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

    def buildTree(self, inorder, postorder):
        if not inorder:
            return
        
        r = postorder.pop()
        root = TreeNode(r)
        i = inorder.index(r)
    
        root.right=self.buildTree(inorder[i+1:],postorder) 
        root.left=self.buildTree(inorder[:i],postorder) 
        return root

        

    
    
if __name__ == "__main__":
    # Test Case1
    inorder1 = [9,3,15,20,7]
    postorder1 = [9,15,7,20,3]

    # Test Case2
    inorder2 = [-1]
    postorder2 = [-1]

    # Test Case3
    inorder3 = [2,1]
    postorder3 = [2,1]

    # Test Case4
    inorder4 = [3,2,1]
    postorder4 = [3,2,1]

    # Test Case5
    inorder5 = [1,3,2]
    postorder5 =[3,2,1]
    sol = Solution()
    
    ans1 = sol.buildTree(inorder1, postorder1)
    ans2 = sol.buildTree(inorder2, postorder2)
    ans3 = sol.buildTree(inorder3, postorder3)
    ans4 = sol.buildTree(inorder4, postorder4)
    ans5 = sol.buildTree(inorder5, postorder5)

    print(sol.levelOrder(ans1))
    print(sol.levelOrder(ans2))
    print(sol.levelOrder(ans3))
    print(sol.levelOrder(ans4))
    print(sol.levelOrder(ans5))

    