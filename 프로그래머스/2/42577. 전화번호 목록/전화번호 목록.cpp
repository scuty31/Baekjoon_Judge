#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_set<string> phone(phone_book.begin(), phone_book.end());
    
    for(int i=0; i<phone_book.size(); i++){
        string pre = "";
        for(int j=0; j<phone_book[i].size()-1; j++){
            pre += phone_book[i][j];
            
            if(phone.count(pre)){
                answer = false;
                break;
            }
        }
        
        if(!answer){
            break;
        }
    }
    
    return answer;
}