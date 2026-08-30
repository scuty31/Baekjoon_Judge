#include <string>
#include <vector>
#include <set>

using namespace std;


set<int> check_num(string numbers, int level, vector<bool> visited, string num, set<int> num_list){
    if (level == numbers.size()){
        num_list.insert(stoi(num));
        
        return num_list;
    }
    
    for(int i=0; i<numbers.size(); i++){
        if (visited[i]){
            continue;
        }
        
        visited[i] = true;
        
        num_list.insert(stoi(num+numbers[i]));
        num_list = check_num(numbers, level+1, visited, num+numbers[i], num_list);
        
        visited[i] = false;
    }
    
    return num_list;
}


int check_prime(set<int> num_list){
    int cnt = 0;
    int max_num = *num_list.rbegin();
    vector<bool> prime_vector(max_num+1, true);
    prime_vector[0] = false;
    prime_vector[1] = false;
    
    for(int i=2; i< prime_vector.size(); i++){
        if (!prime_vector[i]){
            continue;
        }
        
        for(int j=2*i; j<prime_vector.size(); j+=i){
            prime_vector[j] = false;
        }
    }
    
    for(int num:num_list){
        if (prime_vector[num]){
            cnt++;
        }
    }
    
    return cnt;
}


int solution(string numbers) {
    int answer = 0;
    vector<bool> visited(numbers.size(), false);
    set<int> num_list;
    
    num_list = check_num(numbers, 0, visited, "", num_list);
    
    answer = check_prime(num_list);
    
    return answer;
}