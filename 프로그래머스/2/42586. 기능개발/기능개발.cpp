#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> progress_left_day;
    
    for(int i = 0; i<progresses.size(); i++){
        int left_day = (100 - progresses[i]) / speeds[i];
        if ((100 - progresses[i]) % speeds[i]){
            left_day++;
        }
        progress_left_day.push_back(left_day);
    }

    int stack_idx = -1;
    int progress_left = 0;
    
    for(int i = 0; i<progresses.size(); i++){
        if (progress_left < progress_left_day[i]){
            progress_left = progress_left_day[i];
            stack_idx++;
            answer.push_back(1);
        }
        else{
            answer[stack_idx]++;
        }
    }
    
    return answer;
}