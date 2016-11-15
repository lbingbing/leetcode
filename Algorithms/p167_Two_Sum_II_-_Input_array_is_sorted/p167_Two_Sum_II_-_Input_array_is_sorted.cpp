class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i=0,j=numbers.size()-1;i<j;){
            int sum = numbers[i]+numbers[j];
            if(sum<target){
                i++;
            }else if(sum>target){
                j--;
            }else{
                vector<int> res(2);
                res[0] = i+1;
                res[1] = j+1;
                return res;
            }
        }
        return vector<int>();
    }
};
