#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (38.19%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    41.1K
# Total Submissions: 107.5K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = dict()
        for i,num in enumerate(nums):
            #print(mapping)
            j = mapping.get(num)
            #print(i,j)
            if j is not None and nums[i] == nums[j] and abs(i-j)<=k:
                return True
            
            else:
                mapping[num] = i
        return False
# 下面这样的写法是错误的，因为满足前两个条件时，不能将是否满足第三个条件作为结果输出
# 当第三个条件不满足时，程序还可以继续向下找，所以不能马上返回
# if j is not None and nums[i] == nums[j] :
#    return abs(i-j)<=k
# @lc code=end

