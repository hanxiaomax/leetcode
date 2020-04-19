#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (61.15%)

# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self,strs):
        """
        异位字符串排序后必须是相同的字符串
        """
        dic={}
        for s in strs:
            sort_str = self.get_sort_str(s)
            if sort_str in dic:#排序后的结果存在，归类为相同
                dic[sort_str].append(s)
            else:#排序后的不存在，新建分类
                dic[sort_str]=[s]
        return list(dic.values())


    def get_sort_str(self, s):
        return ''.join(sorted(list(s)))#字符串排序的特殊处理，不能用str转换
# @lc code=end

