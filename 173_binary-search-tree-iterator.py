#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
# https://leetcode-cn.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (72.32%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 25.3K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
# 
# 
# 
# 示例：
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
# 
# 
# 
# 提示：
# 
# 
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    """
    实现一个分步执行的二叉树中序遍历
    """
    def __init__(self, root: TreeNode):
        self.stack = []
        self._in_order(root)

    def next(self) -> int:
        """
        @return the next smallest number
        每次调用next，出队一个子左节点并返回值。同时访问其右子节点并将它的左子节点全部入队列
        """
        p = self.stack.pop()
        if p.right:
            self._in_order(p.right)
        return p.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
    
    def _in_order(self,root):
        #左子节点全部入队列
        while root:
            self.stack.append(root)
            root = root.left
          

# Time O(n)
# Space O(h) 
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

