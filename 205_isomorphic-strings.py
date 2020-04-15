#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。


# @lc code=start
class Solution:
    def isIsomorphic(self, s, t) :
        """
        使用哈希表来解决映射问题
        同时遍历两个字符串，将s中的元素作为key，t中的元素作为value
        如果c1已经建立映射，但是映射的对象不是c2，则返回false
        如果c1还没有建立映射，但是c2在values中说明c2是其他元素的映射，也返回false
        如果c1还没有建立映射，c2也没有建立映射，则为它们建立映射
        """
        dic = {}

        for c1,c2 in zip(s,t):
            if c1 in dic and dic.get(c1)!=c2:
                return False
            elif c1 not in dic and c2 in dic.values():
                return False

            else:
                dic[c1] = c2
        return True
        
# @lc code=end

