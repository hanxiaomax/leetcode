#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.32%)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) :
        """
        根据索引遍历时，如果没有一个伪头部，
        则删除时slow.next = slow.next.next会取到空
        """
        dummy_node = ListNode(0)
        dummy_node.next = head

        slow,fast = dummy_node,dummy_node
    
        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
            
        return dummy_node.next
# @lc code=end

