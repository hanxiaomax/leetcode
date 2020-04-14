#https://leetcode-cn.com/problems/walls-and-gates/
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        m = len(rooms)
        n = len(rooms[0])
        # 先把有门的地方都放进来，定义有门的地方path距离是0
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
        # 多源同时进行BFS
        while q:
            r,c,path = q.popleft()
            for i in range(4):
                newr,newc = r+dr[i],c+dc[i]
                if 0<=newr<m and 0<=newc<n and 2147483647 == rooms[newr][newc]:
                    rooms[newr][newc] = path+1
                    q.append((newr,newc,path+1)

作者：mereder
链接：https://leetcode-cn.com/problems/walls-and-gates/solution/duo-yuan-bfs-by-mereder/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。