#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

void DFS(int level, int n, unordered_map<string, bool>& visited, unordered_map<string, unordered_set<string>>& banned_cnt, int answer, vector<string>& banned_id, set<vector<string>>& visited_ban_id, vector<string>& banned_id_list){
    if (n==level){
        vector<string> enter_list = banned_id_list;
        sort(enter_list.begin(), enter_list.end());
        visited_ban_id.insert(enter_list);
        return;
    }
    
    for(const auto& id:banned_cnt[banned_id[level]]){
        if (visited[id]){
            continue;
        }
        
        visited[id] = true;
        banned_id_list.push_back(id);
        
        DFS(level+1, n, visited, banned_cnt, answer, banned_id, visited_ban_id, banned_id_list);
        
        banned_id_list.pop_back();
        visited[id] = false;
    }
    
    return;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 1;
    unordered_map<string, unordered_set<string>> banned_cnt;
    unordered_set<string> ban_id_set;
    
    for(int i = 0; i<banned_id.size(); i++){
        banned_cnt[banned_id[i]] = {};
    }
    
    for(auto& [id, cnt]:banned_cnt){
        for(int j = 0; j<user_id.size(); j++){
            if (id.size() == user_id[j].size()){
                bool is_ban_id = true;
                
                for(int k=0; k<id.size(); k++){
                    if(id[k] != '*' && id[k] != user_id[j][k]){
                        is_ban_id = false;
                        break;
                    }
                }
                
                if (is_ban_id){
                    banned_cnt[id].insert(user_id[j]);
                    ban_id_set.insert(user_id[j]);
                }
            }
        }
    }
    
    unordered_map<string, bool> visited;
    set<vector<string>> visited_ban_id;
    vector<string> banned_id_list;
    
    for(const auto& id: ban_id_set){
        visited[id] = false;
    }
    
    DFS(0, banned_id.size(), visited, banned_cnt, answer, banned_id, visited_ban_id, banned_id_list);
    
    answer = visited_ban_id.size();
    
    return answer;
}