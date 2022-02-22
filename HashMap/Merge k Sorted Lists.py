class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        nums = [(head.val, i) for i, head in enumerate(lists) if head]
        heapify(nums)
        while nums:
            _, i = heappop(nums)
            tail.next = lists[i]
            tail = tail.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(nums, (lists[i].val, i))
        return dummy.next
