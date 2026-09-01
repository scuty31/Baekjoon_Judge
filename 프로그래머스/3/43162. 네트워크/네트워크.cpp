#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;


void BFS(const vector<vector<int>>& graph, int idx, vector<bool>& visited){
    queue<int> q;
    q.push(idx);
    visited[idx] = true;
    
    while(!q.empty()){
        auto node = q.front();
        q.pop();
        
        for(auto next_node:graph[node]){
            if (visited[next_node]){
                continue;
            }
            
            q.push(next_node);
            visited[next_node] = true;
        }
    }
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<vector<int>> graph(n);
    vector<bool> visited(n, false);
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i==j){
                continue;
            }
            if(computers[i][j]==1){
                graph[i].push_back(j);
            }
        }
    }
    
    for(int i=0; i<n; i++){
        if (visited[i]){
            continue;
        }
        BFS(graph, i, visited);
        answer++;
    }
    
    
    return answer;
}