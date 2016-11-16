class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        return (A<G&&E<C&&B<H&&F<D ? -(min(C,G)-max(A,E))*(min(D,H)-max(B,F)) : 0)+(C-A)*(D-B)+(G-E)*(H-F);
    }
};
