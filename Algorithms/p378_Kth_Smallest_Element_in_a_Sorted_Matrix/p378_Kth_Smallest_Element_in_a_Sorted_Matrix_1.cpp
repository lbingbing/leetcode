class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        const int max = 0x7fffffff;
        int len = matrix.size();
        for(int i=0;i<k-1;i++){
            matrix[0][0] = max;
            for(int j1=0,j2=0;j1<len&&j2<len;){
                int v1 = matrix[j1][j2];
                int v2 = j1!=len-1 ? matrix[j1+1][j2] : max;
                int v3 = j2!=len-1 ? matrix[j1][j2+1] : max;
                if(v2<v1 && v2<=v3){
                    matrix[j1][j2] = v2;
                    matrix[j1+1][j2] = v1;
                    j1++;
                }else if(v3<v1 && v3<=v2){
                    matrix[j1][j2] = v3;
                    matrix[j1][j2+1] = v1;
                    j2++;
                }else{
                    break;
                }
            }
        }
        return matrix[0][0];
    }
};
