#include <string>
#include <vector>
#include <unordered_map>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> clothes_types;
    
    for(int i = 0; i<clothes.size(); i++){
        if (clothes_types.count(clothes[i][1])==0){
            clothes_types[clothes[i][1]]++;
        }
        clothes_types[clothes[i][1]]++;
    }
    
    for (const auto& [key, value]: clothes_types){
        answer *= value;
    }
    
    answer--;
    
    return answer;
}