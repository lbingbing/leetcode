class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses,0);
        for(auto e : prerequisites){
            graph[e.second].push_back(e.first);
            ++indegree[e.first];
        }
        queue<int> q;
        for(int i=0;i<numCourses;++i){
            if(indegree[i]==0) q.push(i);
        }
        int num = 0;
        while(!q.empty()){
            int i = q.front();
            q.pop();
            ++num;
            for(int j : graph[i]){
                if(--indegree[j]==0) q.push(j);
            }
        }
        return num==numCourses;
    }
};
