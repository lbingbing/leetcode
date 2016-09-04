class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        typedef pair<int,int> heap_e; // first: v, second: column index
        int m = matrix.size();
        int n = m;
        vector<heap_e> heap(n);
        vector<int> ptr(m,0); // pointer in each column
        for(int i=0;i<n;i++){
            heap[i] = heap_e(matrix[0][i],i);
        }
        for(int i=n/2-1;i>=0;i--){
            heapify(heap,n,i);
        }
        for(int i=0;i<k-1;i++){
            int col = heap[0].second;
            int p = ++ptr[col];
            if(p<m){
                heap[0].first = matrix[p][col];
            }else{
                heap[0] = heap[n-1];
                heap.pop_back();
                n--;
            }
            heapify(heap,n,0);
        }
        return heap[0].first;
    }
    void heapify(vector<pair<int,int>>& heap, int n, int i){
        typedef pair<int,int> heap_e; // first: v, second: column index
        while(i<n){
            int l = l_child(i);
            int r = r_child(i);
            heap_e node = heap[i];
            if(l<n && heap[l].first<node.first && (r>=n || heap[l].first<=heap[r].first)){
                heap[i] = heap[l];
                heap[l] = node;
                i = l;
            }else if(r<n && heap[r].first<node.first && heap[r].first<=heap[l].first){
                heap[i] = heap[r];
                heap[r] = node;
                i = r;
            }else{
                break;
            }
        }
    }
    inline int l_child(int i){ return i*2+1; }
    inline int r_child(int i){ return i*2+2; }
    inline int parent(int i){ return (i-1)/2; }
};
