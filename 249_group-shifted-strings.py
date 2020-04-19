# https://leetcode-cn.com/problems/group-shifted-strings/
class Solution(object):
    def groupStrings(self, strs):
        dic = {}
        for s in strs:
            encode = ""
            for i in range(len(s)-1):
                dist = (ord(s[i+1]) - ord(s[i]))%26 #等价于下面的写法
                # if dist <0 :
                #     dist = 26 - dist

                encode += str(dist)

            if encode in dic:
                dic[encode].append(s)
            else:
                dic[encode] = [s]

        return [dic[_] for _ in dic.keys()]
# 如果是依次和首字母做差，则要添加连字符