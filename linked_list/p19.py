from ListNode import ListNode
class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        m = 0
        prev = None
        cur = head
        
        while cur != None:
            count +=1
            cur = cur.next
        m= count-n
        cur = head
        count =0
        while count <m:
            prev = cur
            cur = cur.next
            count +=1
        if prev is None:
            return head.next
        else:
            prev.next = cur.next

        return head
    

        
if __name__ == "__main__":
    solution = Solution()

    root1 = ListNode(1)
    root2 = ListNode(2)
    root3 = ListNode(3)
    root4 = ListNode(4)
    root5 = ListNode(5)

    n = 2

    root1.next = root2
    root2.next = root3
    root3.next = root4
    root4.next = root5

    #TestCase1
    print("TESTCASE1")
    print(solution.removeNthFromEnd(root1, n))
    print("------")

    root1 = ListNode(1)

    n = 1

    root1.next = root2

    #TestCase1
    print("TESTCASE1")
    print(solution.removeNthFromEnd(root1, n))
    print("------")