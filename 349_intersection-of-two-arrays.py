#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/


# @lc code=start
class Solution:
    def intersection(self, nums1, nums2):
        """
        排序 + 双指针解法
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = set()
        
        i = 0
        j = 0

        while i<len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1

        return res
# @lc code=end
class Solution:
    def intersection(self, nums1, nums2) :
        """
        集合解法
        """
        #return set([n for n in nums1 if n in nums2])
        return set(nums1) & set(nums2)
