#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# 首先理解题意，相连的一片1为一个岛
# @lc code=start
class Solution:
       def numIslands(self, grid) :
        """
        首先理解题意，相连的一片1为一个岛
        """
        if len(grid)==0:#注意判断特殊条件
            return 0
            
        count = 0
        R,C = len(grid),len(grid[0])


        def neighbour(r,c):
            "获取邻接元素，也可以用方向矩阵代替"
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r,c):
            grid[r][c] = '0' # 类似于记录已经遍历过的元素（将连成一片的岛屿击沉）
            for nr,nc in neighbour(r,c):
                if grid[nr][nc] == '1':
                    dfs(nr,nc)
        
        for r,rows in enumerate(grid):
            for c, value in enumerate(rows):
                if value == "1":
                    count+=1
                    dfs(r,c)
                    
        
        return count

ss = Solution()
res = ss.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(res)
# @lc code=end


