#include <string>
#include <vector>

using namespace std;


void chek_squair(vector<vector<int>>& arr, vector<int>& answer, int x, int y, int c){
    int base = arr[x][y];
    bool clear = true;
    
    for(int i = x; i<x+c; i++){
        for(int j = y; j<y+c; j++){
            if (base != arr[i][j]){
                clear = false;
                break;
            }
        }
        if (!clear){
            break;
        }
    }
    
    if (clear){
        answer[base]++;
        return;
    }
    
    int half = c / 2;
    vector<vector<int>> quad_vector = {{x, y, half}, {x+half, y, half}, {x, y+half, half}, {x+half, y+half, half}};
    
    for(int idx = 0; idx<4; idx++){
        vector<int> quad = quad_vector[idx];
        int base = arr[quad[0]][quad[1]];
        bool clear = true;
        
        for(int i = quad[0]; i<quad[0]+quad[2]; i++){
            for(int j = quad[1]; j<quad[1]+quad[2]; j++){
                if (base != arr[i][j]){
                    clear = false;
                    break;
                }
            }
            if (!clear){
                break;
            }
        }
        
        if (clear){
            answer[base]++;
        }
        else{
            chek_squair(arr, answer, quad[0], quad[1], quad[2]);
        }
    }
    
}

vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer = {0, 0};
    chek_squair(arr, answer, 0, 0, arr.size());
    
    return answer;
}