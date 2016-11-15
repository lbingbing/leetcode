class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> operands;
        vector<int> operators;
        while(1){
            string::size_type end;
            operands.push_back(stoi(input,&end));
            input.erase(0,end);
            if(input.empty()){
                break;
            }
            if(input[0]=='+'){
                operators.push_back(0);
            }else if(input[0]=='-'){
                operators.push_back(1);
            }else{
                operators.push_back(2);
            }
            input.erase(0,1);
        }
        return subExpressionResults(operands,operators,0,operands.size()-1);
    }
    
    // operators[i]: 0:+, 1:-, 2:*
    // i,j: subrange of operands
    vector<int> subExpressionResults(const vector<int>& operands, const vector<int>& operators, int i, int j){
        vector<int> results;
        if(i<j){
            // k: operator index
            for(int k=i;k<j;++k){
                vector<int> results_l = subExpressionResults(operands,operators,i,k);
                vector<int> results_r = subExpressionResults(operands,operators,k+1,j);
                for(int v1 : results_l){
                    for(int v2 : results_r){
                        int v;
                        if(operators[k]==0){
                            v = v1+v2;
                        }else if(operators[k]==1){
                            v = v1-v2;
                        }else{
                            v = v1*v2;
                        }
                        results.push_back(v);
                    }
                }
            }
        }else{
            results.push_back(operands[i]);
        }
        return results;
    }
};
