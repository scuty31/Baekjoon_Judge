#include <string>
#include <vector>

using namespace std;


string reverse_op(string w){
    for(int i=0; i<w.size(); i++){
        if (w[i]=='('){
            w[i] = ')';
        }
        else{
            w[i] = '(';
        }
    }
    
    return w;
}


string set_op(string p){
    if(p == ""){
        return p;
    }
    
    int idx = 0;
    int balance = 0;

    for (int i = 0; i < (int)p.size(); i++) {
        balance += (p[i] == '(') ? 1 : -1;
        if (balance == 0) {
            idx = i;
            break;
        }
    }
    
    string u = p.substr(0, idx + 1);
    string v = p.substr(idx + 1);
    
    vector<int> stack;
    bool is_perfect = true;
    
    for (int i=0; i<u.size(); i++){
        if(u[i] == '('){
            stack.push_back(u[i]);
        }
        else{
            if (stack.empty()){
                is_perfect = false;
                break;
            }
            else{
                stack.pop_back();
            }
        }
    }
    
    if (!stack.empty()){
        is_perfect = false;
    }
    
    string result;
    
    if (is_perfect){
        result += u;
        result += set_op(v);
    }
    else{
        result += "(";
        result += set_op(v);
        result += ")";
        u = u.substr(1, u.size()-2);
        result += reverse_op(u);
    }
    
    return result;
}


string solution(string p) {
    string answer = "";
    
    answer = set_op(p);
    
    return answer;
}