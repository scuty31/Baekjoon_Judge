#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> left;
    
    for(int i=0; i<progresses.size(); i++){
        int left_progresses = (100 - progresses[i]);
        int left_time = left_progresses / speeds[i];
        
        if (left_progresses % speeds[i]){
            left_time++;
        }
        
        left.push_back(left_time);
    }
    
    int last_time = 0;
    for(int j=0; j<left.size(); j++){
        if (last_time < left[j]){
            last_time = left[j];
            answer.push_back(1);            
        }
        else{
            answer[answer.size()-1]++;
        }
    }
    
    return answer;
}