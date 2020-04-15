#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (47.71%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 164K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 示例 1:
# 
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶:
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#

# @lc code=start
class Solution:
    """
    如果已经排序则使用双指针可以实现o(n)，否则可以考虑用哈希表跟踪出现次数
    """"
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i,j = 0,0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1

        return res
        
# @lc code=end

