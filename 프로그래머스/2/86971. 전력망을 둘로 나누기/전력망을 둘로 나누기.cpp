#include <string>
#include <vector>
#include <queue>

using namespace std;


int check_tree(int n, vector<vector<int>> wires, int idx){
    int s = wires[idx][0];
    int e = wires[idx][1];
    int s_cnt = 0;
    int e_cnt = 0;
    int cnt = 0;
    
    vector<vector<int>> graph(n+1);
    vector<bool> visited(n+1, false);
    
    for(int i=0; i<wires.size(); i++){
        if (i == idx){
            continue;
        }
        
        int start = wires[i][0];
        int end = wires[i][1];
        
        graph[start].push_back(end);
        graph[end].push_back(start);
    }
    
    queue<int> s_q;
    queue<int> e_q;
    
    s_q.push(s);
    visited[s] = true;
    
    e_q.push(e);
    visited[e] = true;
    
    while (!s_q.empty()){
        int node = s_q.front();
        s_q.pop();
        
        for(int n_node:graph[node]){
            if (visited[n_node]){
                continue;
            }
            s_cnt++;
            visited[n_node] = true;
            s_q.push(n_node);
        }
    }
    
    while (!e_q.empty()){
        int node = e_q.front();
        e_q.pop();
        
        for(int n_node:graph[node]){
            if (visited[n_node]){
                continue;
            }
            
            e_cnt++;
            visited[n_node] = true;
            e_q.push(n_node);
        }
    }
    
    if (s_cnt > e_cnt){
        cnt = s_cnt - e_cnt;
    }
    else{
        cnt = e_cnt - s_cnt;
    }
    
    return cnt;
}



int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    
    for(int idx=0; idx<wires.size(); idx++){
        int cnt = check_tree(n, wires, idx);
        
        if (cnt < answer){
            answer = cnt;
        }
    }
    
    return answer;
}