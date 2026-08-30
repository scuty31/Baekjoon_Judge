#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> one = {1, 2, 3, 4, 5};
    vector<int> two = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> score = {0, 0, 0};
    
    for(int i=0; i<answers.size(); i++){
        int answer_num = answers[i];
        
        if(one[i%one.size()] == answer_num){
            score[0]++;
        }
        if(two[i%two.size()] == answer_num){
            score[1]++;
        }
        if(three[i%three.size()] == answer_num){
            score[2]++;
        }
    }
    
    int max_score = 0;
    for(int j=0; j<3; j++){
        if (max_score < score[j]){
            max_score = score[j];
            answer = {j+1};
        }
        else if(max_score == score[j]){
            answer.push_back(j+1);
        }
    }
    
    return answer;
}