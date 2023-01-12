from ListNode import ListNode


class Solution:
    def rotateRight(self, head, k: int):
        if k == 0 or (not head):
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        k = length-(k % length)

        if k == length:
            return head
        first = head
        second = head
        n = 1
        while n < k:
            first = first.next
            n += 1
        second = first.next
        first.next = None

        cur = second

        while cur and cur.next:
            cur = cur.next

        cur.next = head

        return second


if __name__ == "__main__":
    print("START")
    sol = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    node8 = ListNode(2)
    node7 = ListNode(1, node8)
    node6 = ListNode(0, node7)

    node9 = ListNode(1)
    ans2 = sol.rotateRight(node9, 1)
    print(ans2)

    while ans2:
        print(ans2.val)
        ans2 = ans2.next
