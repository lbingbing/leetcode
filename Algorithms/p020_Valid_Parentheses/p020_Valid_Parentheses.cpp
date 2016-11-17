class Solution {
public:
    bool isValid(string s) {
        stack<char> my_stack;
        for(char c : s){
            if(c=='('||c=='['||c=='{'){
                my_stack.push(c);
            }else if(my_stack.empty() ||
                     c==')'&&my_stack.top()!='(' ||
                     c==']'&&my_stack.top()!='[' ||
                     c=='}'&&my_stack.top()!='{'){
                return 0;
            }else{
                my_stack.pop();
            }
        }
        return my_stack.empty();
    }
};
