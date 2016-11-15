class Queue {
    stack<int,vector<int>> stack_in;
    stack<int,vector<int>> stack_out;
    
    void test_and_shift() {
        if(stack_out.empty()){
            while(!stack_in.empty()){
                stack_out.push(stack_in.top());
                stack_in.pop();
            }
        }
    }
public:
    // Push element x to the back of queue.
    void push(int x) {
        stack_in.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        test_and_shift();
        stack_out.pop();
    }

    // Get the front element.
    int peek(void) {
        test_and_shift();
        return stack_out.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        return stack_out.empty()&&stack_in.empty();
    }
};
