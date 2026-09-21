#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

void travel(unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& tickets_map, string cur, vector<string>& answer){
    while (!tickets_map[cur].empty()){
        string next_travel = tickets_map[cur].top();
        tickets_map[cur].pop();
        
        travel(tickets_map, next_travel, answer);
    }
    answer.push_back(cur);
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> tickets_map;
    
    for(int i = 0; i<tickets.size(); i++){
        tickets_map[tickets[i][0]].push(tickets[i][1]);
    }
    
    travel(tickets_map, "ICN", answer);
    reverse(answer.begin(), answer.end());
    
    return answer;
}