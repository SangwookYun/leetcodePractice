from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = 0
        flag = False
        root = ListNode()
        cur = root
        while l1 or l2:
            if l1 is None:
                sum = l2.val + 0
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + 0
                l1 = l1.next
            else:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            if flag:
                sum += 1
                flag = False

            if sum >= 10:
                sum -= 10
                flag = True
            cur.next = ListNode(sum)
            cur = cur.next

        if flag:
            cur.next = ListNode(1)

        return root.next


if __name__ == "__main__":
    listNode3 = ListNode(3)
    listNode2 = ListNode(4, listNode3)
    listNodeRoot1 = ListNode(2, listNode2)

    listNode6 = ListNode(4)
    listNode5 = ListNode(6, listNode6)
    listNodeRoot2 = ListNode(5, listNode5)

    listNode8 = ListNode(9)
    listNode7 = ListNode(9, listNode8)
    listNodeRoot3 = ListNode(9, listNode7)

    # listNode11 = ListNode(4)
    listNode10 = ListNode(9)
    listNodeRoot4 = ListNode(9, listNode10)

    sol = Solution()
    ans = sol.addTwoNumbers(listNodeRoot1, listNodeRoot2)
    print(ans)

    ans = sol.addTwoNumbers(listNodeRoot3, listNodeRoot4)
    print(ans)
