# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2

        if not l2:
            return l1

        sortedFlatList = []

        while l1 != None and l2 != None:

            if l1.val > l2.val:
                sortedFlatList.append(l2.val)
                l2 = l2.next

            elif l1.val <= l2.val:
                sortedFlatList.append(l1.val)
                l1 = l1.next

        while l1 != None:
            sortedFlatList.append(l1.val)
            l1 = l1.next

        while l2 != None:
            sortedFlatList.append(l2.val)
            l2 = l2.next

        return sortedFlatList

