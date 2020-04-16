class Logger:
    """
    使用哈希表存放当前字符串上一次打印的时间，判断本次是否打印
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        

    def shouldPrintMessage(self, timestamp, message) :
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.data:
            in_time = self.data.get(message)
            if timestamp - in_time >= 10:
                self.data[message] = timestamp
                return True
            else:
                return False
        else:
            self.data[message] = timestamp
            return True

from collections import deque

class Logger2(object):
    """
    使用集合和队列来处理，如果队列中的消息满足打印条件则出队，使用集合来加速判断是否存在
    因为队列里面存放的是元组不方便用in
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
