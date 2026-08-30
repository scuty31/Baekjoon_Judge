#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    brown = (brown - 4)/2;         // 가로 + 세로 길이
    
    for(int x=1; x<(brown/2)+1; x++){
        int y = brown - x;
        cout << y << ", " << x << "\n";
        
        if (x*y == yellow){
            answer = {y+2, x+2};
            break;
        }
    }
    
    return answer;
}