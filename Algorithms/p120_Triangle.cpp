class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> table(n,0);
        vector<int> table_tmp(n);
        table[0] = triangle[0][0];
        for(int i=1;i<n;++i){
            table_tmp[0] = table[0]+triangle[i][0];
            for(int j=1;j<=i-1;++j){
                table_tmp[j] = min(table[j-1],table[j])+triangle[i][j];
            }
            table_tmp[i] = table[i-1]+triangle[i][i];
            for(int j=0;j<=i;++j){
                table[j] = table_tmp[j];
            }
        }
        return *min_element(table.begin(),table.end());
    }
};
