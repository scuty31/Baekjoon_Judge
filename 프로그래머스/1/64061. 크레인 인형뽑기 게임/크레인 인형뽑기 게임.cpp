#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> stack;
    
    for(int i=0; i<moves.size(); i++){
        int y = moves[i]-1;
        
        for(int x=0; x<board.size(); x++){
            if(board[x][y] != 0){
                int pick_up = board[x][y];
                if ((!stack.empty()) && (pick_up == stack.back())){
                    stack.pop_back();
                    answer+=2;
                }
                else{
                    stack.push_back(pick_up);
                }
                board[x][y] = 0;
                break;
            }
        }
    }
    
    return answer;
}