#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> phonecetmon(nums.begin(), nums.end());
    
    if(nums.size()/2 < phonecetmon.size()){
        answer = nums.size()/2;
    }
    else{
        answer = phonecetmon.size();
    }
    
    return answer;
}