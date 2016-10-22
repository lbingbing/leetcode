# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList
        self.index = -1
        self.my_stack = []
        self.nextHelper()

    def nextHelper(self):
        while True:
            while self.my_stack:
                self.my_stack[-1][1] += 1
                if(self.my_stack[-1][1]!=len(self.my_stack[-1][0].getList())):
                    break
                self.my_stack.pop()
            if not self.my_stack:
                self.index += 1
                if self.index==len(self.nested_list):
                    break
                self.my_stack.append([self.nested_list[self.index],0])
            while not self.my_stack[-1][0].isInteger() and self.my_stack[-1][0].getList():
                self.my_stack.append([self.my_stack[-1][0].getList()[self.my_stack[-1][1]],0])
            if self.my_stack[-1][0].isInteger():
                break
            else:
                self.my_stack.pop()

    def next(self):
        """
        :rtype: int
        """
        res = self.my_stack[-1][0].getInteger()
        self.my_stack.pop()
        self.nextHelper()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index!=len(self.nested_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
