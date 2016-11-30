class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prerequisites_graph = [[] for i in range(numCourses)]
        for i,j in prerequisites:
            prerequisites_graph[i].append(j)
        mark = [0]*numCourses
        for i in range(numCourses):
            if mark[i]==0:
                has_cycle = [False]
                self.dfs(prerequisites_graph,mark,i,has_cycle)
                if has_cycle[0]:
                    return False
        return True

    def dfs(self, prerequisites_graph, mark, i, has_cycle):
        mark[i] = 1
        for j in prerequisites_graph[i]:
            if mark[j]==0:
                self.dfs(prerequisites_graph,mark,j,has_cycle)
            elif mark[j]==1:
                has_cycle[0] = True
            if has_cycle[0]:
                return
        mark[i] = 2
