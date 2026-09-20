#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    int answer = 0;
    priority_queue<int> q;
    
    for(int i = 0; i<enemy.size(); i++){
        q.push(-enemy[i]);
        
        if (q.size() > k){
            int x = q.top();
            q.pop();
            n += x;
        }
        
        if (n < 0){
            answer = i;
            break;
        }
    }
    
    if (answer == 0){
        answer = enemy.size();
    }
    
    return answer;
}