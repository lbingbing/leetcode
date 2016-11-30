class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for e in prerequisites:
            graph[e[1]].append(e[0])
            indegree[e[0]] += 1
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        num = 0
        while q:
            i = q.popleft()
            num += 1
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j]==0:
                    q.append(j)
        return num==numCourses
