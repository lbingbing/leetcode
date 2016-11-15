int main(){
    std::default_random_engine gen(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> dis1(0,3);
    std::uniform_int_distribution<int> dis2(0,100);

    Queue q1;
    std::queue<int> q2;

    int m = 1000000;
    for(int i=0;i<m;++i){
        if(q1.empty()!=q2.empty()){
            cout<<"incorrect"<<endl;
            break;
        }
        if(q1.empty() || dis1(gen)<2){
            int v = dis2(gen);
            q1.push(v);
            q2.push(v);
        }else{
            if(q1.peek()!=q2.front()){
                cout<<"incorrect"<<endl;
                break;
            }
            q1.pop();
            q2.pop();
        }
    }

  return 0;
}
