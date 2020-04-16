#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射
# 
# 具体地说，你的设计应该包含以下的功能
# 
# 
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
# 
# 
# 
# 示例：
# 
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1 
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到) 
# 
# 
# 
# 注意：
# 
# 
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。
# 
# 
#

# @lc code=start
class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.DEEP = 1000
        self.data = [Backet() for i in range(self.DEEP)]
    
    def _hash(self,key):
        return key % self.DEEP
        

    def add(self, key: int) -> None:
        
        hash_index = self._hash(key)
        self.data[hash_index].insert(key)

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        self.data[hash_index].delete(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_index = self._hash(key)
        return self.data[hash_index].exist(key)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Backet:
    def __init__(self):
        self.head = Node(0)
        self.size = 0
    
    def insert(self,value):
        if self.exist(value):
            return 
        
        pre = self.head
        curr = self.head
        while curr is not None:
            pre = curr
            curr = curr.next

        node = Node(value)
        pre.next = node
        self.size += 1
    
    def __repr__(self):
        curr = self.head.next
        #print("sizeof ",self.size)
        while curr is not None:
            #print(curr.value,end="->")
            curr = curr.next
        return ''
        
    def delete(self,value):
        pre = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                pre.next = curr.next
                self.size -= 1
                return 
            pre = curr
            curr = curr.next
        
            
    
    def exist(self,value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                #print('true')
                return True
            curr = curr.next

        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

