#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int i = 0; i<commands.size(); i++){
        int x = commands[i][0]-1;
        int y = commands[i][1]-1;
        int z = commands[i][2]-1;
        
        vector<int> tmp_list;
        
        for(int l = x; l<=y; l++){
            tmp_list.push_back(array[l]);
        }
        
        sort(tmp_list.begin(), tmp_list.end());
        answer.push_back(tmp_list[z]);
    }
    
    return answer;
}