#include <string>
#include <vector>
//#include <bits/stdc++.h>

using namespace std;

int check_dungeons(int k, int level, vector<vector<int>> dungeons, vector<bool> visited, int cnt){
    if (level == dungeons.size()){
        cnt = level;
        return cnt;
    }
    
    for(int i=0; i<dungeons.size(); i++){
        if (visited[i]){
            continue;
        }
        
        if (k < dungeons[i][0]){
            continue;
        }
        
        visited[i] = true;
        k -= dungeons[i][1];
        
        //cout << k << " " << level << " " << cnt << " " << "\n";
        
        cnt = check_dungeons(k, level+1, dungeons, visited, cnt);
        
        visited[i] = false;
        k += dungeons[i][1];
    }
    
    if (level > cnt){
        cnt = level;
    }
    
    return cnt;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<bool> visited(dungeons.size(), false);
    
    answer = check_dungeons(k, 0, dungeons, visited, 0);
    
    return answer;
}