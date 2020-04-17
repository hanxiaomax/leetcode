#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#


# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    虽然a，b不一样长，但是a+b = b+a 所以将到达结尾的指针再指向另一个链表的头
    如果两个链表有相交的节点，则因为移动速度一样，最终比如交汇于交点
    """
    def getIntersectionNode(self, headA, headB) :
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA
# @lc code=end

