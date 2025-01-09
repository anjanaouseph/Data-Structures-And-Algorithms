# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        if len(nestedList) == 0:
            return 0

        queue = deque([[nested, 1] for nested in nestedList]) #add all in depth of 1.

        total = 0

        #Use queue for BFS, here we explore all elements in a depth before moving to next depth.
        while queue:
            nested, depth = queue.popleft()

            if nested.isInteger():
                total += nested.getInteger() * depth

            else:
                for each in nested.getList():
                    queue.append([each, depth+1])

        return total
