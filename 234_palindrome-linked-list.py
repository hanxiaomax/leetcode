#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.37%)

# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head):
            "反转字符串"
            pre = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp

            return pre

        slow,fast = head,head
        # 双指针找到中间节点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        re = reverseList(slow)#反转后半段链表
        
        start,end = head,re

        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next

        reverseList(re)#恢复后半段链表，注意前面不能改变re
        #print(head) # 可以直接打印链表

        return True
# @lc code=end

