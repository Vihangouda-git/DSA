class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        mind = float('inf')

        while curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = pos
                else:
                    mind = min(mind, pos - last)

                last = pos

            prev = curr
            curr = curr.next
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        maxd = last - first

        return [mind, maxd]