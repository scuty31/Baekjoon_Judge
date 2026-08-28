#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int min_num = *min_element(arr.begin(), arr.end());
    
    if (arr.size() == 1){
        answer.push_back(-1);
    }
    else{
        for(int i = 0; i<arr.size(); i++){
            if (arr[i] > min_num){
                answer.push_back(arr[i]);
            }
        }
    }
    return answer;
}