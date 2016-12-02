class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int n = A.size();
        int sum_A = 0;
        int F = 0;
        for(int i=0;i<n;++i){
            sum_A += A[i];
            F += i*A[i];
        }
        int res = F;
        for(int i=1;i<n;++i){
            // F(i)-F(j)=sum(A)-nA[n-i], 0<=i<=n-1, j=(i-1)%n
            F += sum_A-n*A[n-i];
            if(F>res) res = F;
        }
        return res;
    }
};
