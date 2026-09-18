#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;


void select_order(int level, int cnt, string sub_order, vector<string>& sub_orders, int idx, string order){
    if (level == cnt){
        sub_orders.push_back(sub_order);
        return;
    }
    
    for(int i = idx+1; i<order.size()-(level-cnt)-1; i++){
        sub_order += order[i];
        select_order(level+1, cnt, sub_order, sub_orders, i, order);
        sub_order.pop_back();
    }
}


vector<string> substr_orders(string order, int cnt){
    int level = 0;
    vector<string> sub_orders;
    
    select_order(0, cnt, "", sub_orders, -1, order);
    
    return sub_orders;
}


vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    unordered_map <string, int> menu;
    unordered_map <int, int> menu_cnt;
    
    for(int i = 0; i<course.size(); i++){
        menu_cnt[course[i]] = 0;
    }
    
    for(int i = 0; i<orders.size(); i++){
        sort(orders[i].begin(), orders[i].end());
    }
    
    for(int i = 0; i<orders.size(); i++){
        for(int j = 0; j<course.size(); j++){
            vector<string> sub_orders = substr_orders(orders[i], course[j]);
            
            for(int k = 0; k<sub_orders.size(); k++){
                menu[sub_orders[k]]++;
                //cout<<sub_orders[k]<<"\n";
            }
        }
    }
    
    for(const auto& [order, cnt]: menu){
        if (cnt > 1){
            int l = order.size();
        
            for(int i = 0; i<course.size(); i++){
                if (l == course[i]){
                    if (cnt > menu_cnt[course[i]]){
                        menu_cnt[course[i]] = cnt;
                    }
                }
            }
        }
    }
    
    for(const auto& [order, cnt]: menu){
        if (cnt > 1){
            int l = order.size();
            
            if (cnt == menu_cnt[l]){
                answer.push_back(order);
            }
        }
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}