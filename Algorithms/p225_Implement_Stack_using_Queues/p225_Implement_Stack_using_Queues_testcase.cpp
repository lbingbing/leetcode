int main(){
    std::default_random_engine gen(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> dis1(0,3);
    std::uniform_int_distribution<int> dis2(0,100);

    Stack stack1;
    std::stack<int> stack2;

    int m = 1000000;
    for(int i=0;i<m;++i){
        if(stack1.empty()!=stack2.empty()){
            cout<<"incorrect 1"<<endl;
            break;
        }
        if(!stack1.empty()){
            if(stack1.top()!=stack2.top()){
                cout<<"incorrect 2, "<<stack1.top()<<" "<<stack2.top()<<endl;
                break;
            }
        }
        if(stack1.empty() || dis1(gen)<2){
            int v = dis2(gen);
            stack1.push(v);
            stack2.push(v);
        }else{
            stack1.pop();
            stack2.pop();
        }
    }

  return 0;
}
