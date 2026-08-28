#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> people;
    
    for(int i = 0; i<participant.size(); i++){
        if (people.find(participant[i]) != people.end()){
            people[participant[i]] += 1;
        }
        else{
            people[participant[i]] = 1;
        }
    }
    
    for(int j=0; j<completion.size(); j++){
        people[completion[j]] -= 1;
    }
    
    for(const auto& [person, cnt] : people){
        if (cnt == 1){
            answer = person;
            break;
        }
    }
    
    return answer;
}