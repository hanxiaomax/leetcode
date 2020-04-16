#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (56.14%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 22K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合
# 
# 具体地说，你的设计应该包含以下的功能
# 
# 
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 

# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。
# 
# 
#

# @lc code=start
class MyHashMap:
    """
    使用链表还是数组要看所需的操作，例如删除操作使用链表则为o(1)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.DEEP = 2096
        self.data = [Bucket() for i in range(self.DEEP)]

    def _hash(self,key):
        return key % self.DEEP

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.data[self._hash(key)].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.data[self._hash(key)].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.data[self._hash(key)].remove(key)

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)