#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (37.12%)

# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2) :
        """
        链表不需要等长，但是要考虑最后剩余的一个carry位
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0 #进位
            
        # 不论是否等长均一样处理，以最长的链表为截止条件
        while l1 or l2:
            v1 = l1.val if l1 else 0 #如果链表没有截止则取值
            v2 = l2.val if l2 else 0
            _sum = v1 + v2 + carry
            carry = 0 #使用后即消耗
            if _sum >= 10:
                carry = _sum//10 #先求进位 
                _sum = _sum%10 
            
            node = ListNode(_sum)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # 如果最后的进位没有被消耗则成为最后一个节点
        curr.next = ListNode(carry) if carry else None 
        return dummy.next
            
# @lc code=end



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        edge case:
        1. 等长，最后一位进位
        2. 不等长
        3. 不等长切最后一位进位
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0 #进位
            
        # 处理链表等长到部分
        while l1 and l2:
            _sum = l1.val + l2.val + carry
            carry = 0 #使用后即消耗
            if _sum >= 10:
                carry = _sum//10 #先求进位 
                _sum = _sum%10 
                #print(carry)
            
            node = ListNode(_sum)
            curr.next = node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        #处理不等长部分
        rem = l1 if l1 else l2
        if carry == 0 and rem:
            curr.next = rem
            return dummy.next
        
        print(rem)

        while rem:
            _sum = rem.val + carry  
            carry = 0
            if _sum >= 10:
                carry = _sum//10 #先求进位 
                _sum = _sum%10 
            node = ListNode(_sum)
            curr.next = node
            curr = curr.next
            rem = rem.next

        # 如果进位没有被消耗则成为最后一个节点
        curr.next = ListNode(carry) if carry else None 
        print(curr)
        return dummy.next
            
