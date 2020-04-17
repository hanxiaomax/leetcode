# https://leetcode-cn.com/problems/first-unique-character-in-a-string/submissions/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dc = Counter(s)

        for index,_ in enumerate(s):
            if dc.get(_) == 1:
                return index
        else:
            return -1