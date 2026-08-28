#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max_width = 0;
    int max_hight = 0;
    
    for(int i=0; i<sizes.size(); i++){
        int w = sizes[i][0];
        int h = sizes[i][1];
        
        if(w < h){
            int tmp = w;
            w = h;
            h = tmp;
        }
        
        if(max_width < w){
            max_width = w;
        }
        if(max_hight < h){
            max_hight = h;
        }
    }
    
    answer = max_hight * max_width;
    
    return answer;
}