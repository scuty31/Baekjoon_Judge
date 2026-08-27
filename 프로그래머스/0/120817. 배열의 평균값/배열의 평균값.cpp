#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    double num_sum = 0;
    
    for(int i = 0; i < numbers.size(); i++){
        num_sum += numbers[i];
    }
    answer = num_sum / numbers.size();
        
    return answer;
}