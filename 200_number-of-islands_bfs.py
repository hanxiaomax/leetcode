#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# 首先理解题意，相连的一片1为一个岛
# @lc code=start
from collections import deque
class Solution:
   def numIslands(self, grid) :
        """
        首先理解题意，相连的一片1为一个岛
        """
        if len(grid)==0:#注意判断特殊条件
            return 0
        
        queue = deque()
        count = 0
        R,C = len(grid),len(grid[0])

        def neighbour(r,c):
            "获取邻接元素，也可以用方向矩阵代替"
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def bfs(r,c):
            while queue:#出队一个元素
                nr,nc = queue.popleft()
                for nr,nc in neighbour(nr, nc):#对其周围对元素，如果是陆地则入队并标记
                    if grid[nr][nc] == '1':
                        grid[nr][nc] = '0' 
                        queue.append((nr,nc))

        #遍历矩阵
        for r,rows in enumerate(grid):
            for c, value in enumerate(rows):
                if value == "1": #对于一块陆地，将其加入队列并使用bfs搜索它周围的全部陆地
                    count+=1# 入队时增加
                    queue.append((r,c))
                    bfs(r,c)
                    grid[r][c] = '0' # 标记为已经访问
                    
        
        return count

# @lc code=end


