#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# https://leetcode-cn.com/problems/linked-list-cycle/description/
#

# 给定一个链表，判断链表中是否有环。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #防止访问空指针，要注意判断
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next


        while slow!=fast:
            if fast and fast.next : #防止访问空指针，要注意判断
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        
        return True
    
# @lc code=end

