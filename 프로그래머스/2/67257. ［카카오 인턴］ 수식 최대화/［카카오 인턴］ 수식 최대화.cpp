#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long check_result(vector<long long> num, vector<char> op, vector<char> op_vector, long long answer){
    long long result = 0;
    int idx = 0;
    
    for (int i = 0; i< 3; i++){
        idx = 0;
        
        while (idx < op.size()){
            if (op[idx] == op_vector[i]){
                if (op[idx] == '+'){
                    long long number = num[idx] + num[idx+1];
                    num[idx] = number;
                    num.erase(num.begin()+1+idx);
                    op.erase(op.begin()+idx);
                }
                else if (op[idx] == '-'){
                    long long number = num[idx] - num[idx+1];
                    num[idx] = number;
                    num.erase(num.begin()+1+idx);
                    op.erase(op.begin()+idx);
                }
                else{
                    long long number = num[idx] * num[idx+1];
                    num[idx] = number;
                    num.erase(num.begin()+1+idx);
                    op.erase(op.begin()+idx);
                }
            }
            else{
                idx++;
            }
            
            if (idx == op.size()){
                break;
            }
        }
    }
    
    result = num[0];
    
    if (result < 0){
        result *= -1;
    }
    
    if (answer < result){
        answer = result;
    }
    
    return answer;
}

long long solution(string expression) {
    long long answer = 0;
    vector<long long> num;
    vector<char> op;
    int idx = 0;
    
    for(int i = 0; i<expression.size(); i++){
        if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*'){
            string num_str = expression.substr(idx, i-idx);
            num.push_back(stoi(num_str));
            op.push_back(expression[i]);
            idx = i+1;
        }
    }
    
    string num_str = expression.substr(idx);
    num.push_back(stoi(num_str));
    
    vector<char> op_select = {'+', '-', '*'};
    
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            for(int k = 0; k<3; k++){
                if(i == j || i == k || j == k){
                    continue;
                }
                vector<char> op_vector;
                op_vector.push_back(op_select[i]);
                op_vector.push_back(op_select[j]);
                op_vector.push_back(op_select[k]);
                
                answer = check_result(num, op, op_vector, answer);
            }
        }
    }
    
    
    return answer;
}