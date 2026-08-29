#include <string>
#include <vector>
#include <unordered_map>

using namespace std;


int check_max(vector<int> priorities){
    int max_num = 0;
    for(int i=0; i<priorities.size(); i++){
        if (max_num < priorities[i]){
            max_num = priorities[i];
        }
    }
    
    return max_num;
}


int solution(vector<int> priorities, int location) {
    int answer = 0;
    int priorities_size = priorities.size();
    unordered_map<int, int> priorities_map;
    int max_priorities = 0;
    
    for(int i=0; i<priorities_size; i++){
        priorities_map[priorities[i]]++;
        
        if (priorities[i] > max_priorities){
            max_priorities = priorities[i];
        }
    }
    
    int idx = 0;
    while(true){
        if (priorities[idx] == -1){
            idx = (idx + 1)%priorities_size;
        }
        
        if(priorities[idx] == max_priorities){
            priorities_map[priorities[idx]]--;
            priorities[idx] = -1;
            
            if (priorities_map[max_priorities] == 0){
                max_priorities = check_max(priorities);
            }
            
            answer++;
            
            if (idx == location){
                break;
            }
               
        }   
        idx = (idx + 1)%priorities_size;
    }
    return answer;
}