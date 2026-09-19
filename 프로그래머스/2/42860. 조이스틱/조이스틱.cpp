#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

void set_name(string name, vector<int>& name_cnt){
    for(int i = 0; i<name.size(); i++){
        int cnt = 0;
        if (name[i] - 'A' < 'Z' - name[i]+1){
            cnt = name[i] - 'A';
        }
        else{
            cnt = 'Z' - name[i]+1;
        }
        
        name_cnt[i] = cnt;
    }
    
    return;
}

unordered_map<int, int> check_A(vector<int>& name_cnt){
    unordered_map<int, int> A_idx;
    int s_idx = -1;
    int e_idx = -1;
    
    for(int i = 0; i<name_cnt.size(); i++){
        if (name_cnt[i] == 0 && s_idx == -1){
            s_idx = i;
            e_idx = i;
        }
        else if (name_cnt[i] == 0 && s_idx != -1){
            e_idx = i;
        }
        else if (name_cnt[i] != 0 && s_idx != -1){
            A_idx[s_idx] = e_idx;
            s_idx = -1;
            e_idx = -1;
        }
    }
    
    if (e_idx != -1){
        A_idx[s_idx] = name_cnt.size()-1;
    }
    
    return A_idx;
}


int change_cnt(vector<int>& name_cnt, unordered_map<int, int>& A_idx){
    int result = 0;
    
    for(int i = 0; i<name_cnt.size(); i++){
        result += name_cnt[i];
    }
    
    int min_a = name_cnt.size()-1;
    
    for(const auto& [key, value]: A_idx){
        int a_cnt = 0;
        if (key == 0){
            a_cnt = name_cnt.size()-1 - value;
        }
        else if (value == name_cnt.size()-1){
            a_cnt = key-1;
        }
        else{
            a_cnt = (key-1)*2 + (name_cnt.size()-1 - value);
            int b_cnt = (name_cnt.size()-1 - value)*2 + key-1;
            
            if (a_cnt>b_cnt){
                a_cnt = b_cnt;
            }
        }

        if (min_a > a_cnt){
            min_a = a_cnt;
        }
    }
    
    result += min_a;
    
    return result;
}

int solution(string name) {
    int answer = 0;
    vector<int> name_cnt(name.size(), 0);
    unordered_map<int, int> A_idx;
    
    set_name(name, name_cnt);
    A_idx = check_A(name_cnt);
    
    answer = change_cnt(name_cnt, A_idx);
    
    return answer;
}