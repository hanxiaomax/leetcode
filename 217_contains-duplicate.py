#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/

#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# 

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for num in nums:
            if mapping.get(num):
                return True
            else:
                mapping[num]=1
        
        return False

# @lc code=end



        
