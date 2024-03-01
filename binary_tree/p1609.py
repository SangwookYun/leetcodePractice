from hash.TreeNode import TreeNode
class Solution:
    def isEvenOddTree (self, root) -> int:
        pass
        queue = [root]
        check = []
        temp_queue = []
        cnt = 0

        while queue or temp_queue:
            while queue:
                cur = queue.pop(0)
                if cur.left:
                    temp_queue.append(cur.left)
                if cur.right:
                    temp_queue.append(cur.right)
                check.append(cur.val)

            print("queue", queue)
            print("temp_queue",temp_queue)
            print("check",check)
      
            print(cnt)

            if cnt%2==0:
                for i in range(len(check)):
                    if check[i]%2 ==0:
                        return False
                for i in range(len(check)-1):
                    if check[i]- check[i+1] >=0:
                        return False
            else:
                for i in range(len(check)):
                    if check[i]%2 ==1:
                        return False
                for i in range(len(check)-1):
                    if check[i]- check[i+1] <=0:
                        return False
            queue = temp_queue.copy()
            temp_queue = []
            check = []
            cnt +=1
            print("queue", queue)
            print("temp_queue",temp_queue)
            print("_____")
        return True

if __name__ == "__main__":
    solution = Solution()

    # root1 = TreeNode(1)
    # root2 = TreeNode(10)
    # root3 = TreeNode(4)
    # root4 = TreeNode(3)
    # root5 = TreeNode(7)
    # root6 = TreeNode(9)
    # root7 = TreeNode(12)
    # root8 = TreeNode(8)
    # root9 = TreeNode(6)
    # root10 = TreeNode(2)
    

    # root1.left = root2
    # root1.right = root3
    # root2.left = root4
   
    # root3.left= root5
    # root3.right= root6

    # root4.left = root7
    # root4.right = root8
    # root5.left = root9
    # root6.right = root10
    
    # #TestCase1
    # print("TESTCASE1")
    # # print("PASS" if solution.isEvenOddTree(root1) == 2 else "FAILED")
    # print(solution.isEvenOddTree(root1))
    # print("------")
    
    
    root1 = TreeNode(5)
    root2 = TreeNode(4)
    root3 = TreeNode(2)
    root4 = TreeNode(3)
    root5 = TreeNode(3)
    root6 = TreeNode(7)
    
    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right= root5

    root3.left = root6
    
    #TestCase1
    print("TESTCASE2")
    # print("PASS" if solution.isEvenOddTree(root1) == 2 else "FAILED")
    print(solution.isEvenOddTree(root1))
    print("------")
    
    # # root1 = TreeNode(9)
    # # #TestCase3
    # # print("TESTCASE3")
    # # print("PASS" if solution.pseudoPalindromicPaths(root1) == 1 else "FAILED")
    # # print(solution.pseudoPalindromicPaths(root1))
    # # print("------")
