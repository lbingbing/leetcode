class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> prerequisites_graph(numCourses);
        for(auto e : prerequisites){
            prerequisites_graph[e.first].push_back(e.second);
        }
        vector<int> mark(numCourses,0);
        for(int i=0;i<numCourses;++i){
            if(mark[i]==0){
                bool has_cycle = 0;
                dfs(prerequisites_graph,mark,i,has_cycle);
                if(has_cycle) return 0;
            }
        }
        return 1;
    }
    void dfs(vector<vector<int>>& prerequisites_graph, vector<int>& mark, int i, bool& has_cycle) {
        mark[i] = 1;
        for(int j : prerequisites_graph[i]){
            if(mark[j]==0){
                dfs(prerequisites_graph,mark,j,has_cycle);
            }else if(mark[j]==1){
                has_cycle = 1;
            }
            if(has_cycle) return;
        }
        mark[i] = 2;
    }
};
