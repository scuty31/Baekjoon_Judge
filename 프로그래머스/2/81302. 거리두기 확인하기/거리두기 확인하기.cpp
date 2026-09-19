#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<pair<int, int>> check_people(vector<string>& place){
    vector<pair<int, int>> people;
    
    for(int x = 0; x<place.size(); x++){
        for(int y = 0; y<place[x].size(); y++){
            if (place[x][y] == 'P'){
                people.push_back({x, y});
            }
        }
    }
    
    return people;
}

int check_room(vector<string>& place, pair<int, int> person){
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};
    queue<vector<int>> q;
    vector<vector<bool>> visited(place.size(), vector<bool>(place[0].size(), false));
    
    int x = person.first;
    int y = person.second;
    
    q.push({x, y, 0});
    visited[x][y] = true;
    
    while (!q.empty()){
        vector<int> tmp = q.front();
        q.pop();
        x = tmp[0];
        y = tmp[1];
        int cnt = tmp[2];
        
        for(int i = 0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx >= place.size() || ny >= place[0].size()){
                continue;
            }
            if (cnt == 2){
                continue;
            }
            if (visited[nx][ny]){
                continue;
            }
            if (place[nx][ny] == 'X'){
                continue;
            }
            if (place[nx][ny] == 'P'){
                return 0;
            }
            
            visited[nx][ny] = true;
            q.push({nx, ny, cnt+1});
        }
    }
    
    return 1;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    for(int i = 0; i< places.size(); i++){
        vector<pair<int, int>> people = check_people(places[i]);
        int result = 1;
        for(int j = 0; j<people.size(); j++){
            result = check_room(places[i], people[j]);
            
            if (result == 0){
                break;
            }
        }
        
        answer.push_back(result);
    }
    
    return answer;
}