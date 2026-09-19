#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    vector<char> stack;
    
    for(int i = 0; i<number.size(); i++){
        if (stack.empty()){
            stack.push_back(number[i]);
            continue;
        }
        if (stack.back() < number[i]){
            while (!stack.empty() && k > 0 && stack.back() < number[i]){
                stack.pop_back();
                k--;
            }
            stack.push_back(number[i]);
        }
        else{
            stack.push_back(number[i]);
        }
    }
    
    if (k>0){
        while (k>0){
            stack.pop_back();
            k--;
        }
    }
    
    for(int i = 0; i<stack.size(); i++){
        answer += stack[i];
    }
    
    return answer;
}