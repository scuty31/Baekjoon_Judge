#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(string word) {
    int answer = 0;
    unordered_map<int, char> alpha;
    
    alpha[1] = 'A';
    alpha[2] = 'E';
    alpha[3] = 'I';
    alpha[4] = 'O';
    alpha[5] = 'U';
    
    vector<int> idx = {1};
    
    while(true){
        string new_word = "";
        for(int i = 0; i<idx.size(); i++){
            new_word += alpha[idx[i]];
        }
        answer++;
        
        if (new_word == word){
            return answer;
        }
        
        if(idx.size() < 5){
            idx.push_back(1);
        }
        else{
            idx[idx.size()-1]++;
            
            while(idx.back() == 6){
                idx.pop_back();
                idx[idx.size()-1]++;
            }
        }
    }
    
    
    return answer;
}