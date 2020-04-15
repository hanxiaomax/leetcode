class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        


    def add(self, number) :
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)


    def find(self, value: int):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        dic = {}
        for n in self.nums:
            complement = value - n
            if dic.get(complement) is not None:
                return True
            else:
                dic[n] = complement
        return False


class TwoSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        


    def add(self, number) :
        """
        Add the number to an internal data structure..
        同时进行个数统计
        """
        if self.nums.get(number) is not None:
            self.nums[number]+=1
        else:
            self.nums[number] = 1


    def find(self, value) :
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.nums.keys():
            complement = value - n #求补数
            if complement!=n: # 如果两数不等，那么只要能确定数据集中有该补数即可
                if complement in self.nums:
                    return True
            elif self.nums.get(complement,0) > 1:#如果两数相等，则该数的个数必须大于1
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```