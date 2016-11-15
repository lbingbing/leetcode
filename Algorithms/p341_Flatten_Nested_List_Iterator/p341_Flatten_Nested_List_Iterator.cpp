/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
    vector<NestedInteger>* nested_list;
    int index;
    stack<pair<NestedInteger*,int>,vector<pair<NestedInteger*,int>>> my_stack;

    void nextHelper(){
        while(1){
            while(!my_stack.empty()){
                if(++my_stack.top().second!=my_stack.top().first->getList().size()) break;
                my_stack.pop();
            }
            if(my_stack.empty()){
                if(++index==nested_list->size()) break;
                my_stack.push(make_pair(&(*nested_list)[index],0));
            }
            while(!my_stack.top().first->isInteger()&&!my_stack.top().first->getList().empty()){
                my_stack.push(make_pair(&my_stack.top().first->getList()[my_stack.top().second],0));
            }
            if(my_stack.top().first->isInteger()) break;
            else my_stack.pop();
        }
    }

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        nested_list = &nestedList;
        index = -1;
        nextHelper();
    }

    int next() {
        int res = my_stack.top().first->getInteger();
        my_stack.pop();
        nextHelper();
        return res;
    }

    bool hasNext() {
        return index!=nested_list->size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
