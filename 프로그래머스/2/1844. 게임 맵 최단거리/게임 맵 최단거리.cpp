#include<vector>
#include<queue>
#include<tuple>
using namespace std;


int move_player(vector<vector<int>>& maps){
    int n = maps.size();
    int m = maps[0].size();
    vector<vector<int>> visited(n, vector<int>(m, -1));
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};
    queue<vector<int>> q;
    
    q.push({0, 0});
    visited[0][0] = 1;
    
    while (!q.empty()){
        vector<int> xy = q.front();
        int x = xy[0];
        int y = xy[1];
        q.pop();
        
        for(int i = 0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx >= n || ny >= m){
                continue;
            }
            if (maps[nx][ny] == 0){
                continue;
            }
            if (visited[nx][ny] != -1){
                continue;
            }
            if (visited[nx][ny] == -1 || visited[nx][ny] > visited[x][y] + 1){
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    return visited[n-1][m-1];
}


int solution(vector<vector<int> > maps)
{
    int answer = 0;
    
    answer = move_player(maps);
    
    return answer;
}