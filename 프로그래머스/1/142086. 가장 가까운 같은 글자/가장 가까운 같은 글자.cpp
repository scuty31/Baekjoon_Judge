#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    unordered_map<char, int> hash_map;
    
    for(int i=0; i<s.size(); i++){
        if (hash_map.find(s[i]) != hash_map.end()){
            answer.push_back(i - hash_map[s[i]]);
            hash_map[s[i]] = i;
        }
        else{
            hash_map[s[i]] = i;
            answer.push_back(-1);
        }
        
    }
    return answer;
}