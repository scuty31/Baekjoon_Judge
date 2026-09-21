#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int bfs(vector<vector<int>> maps, int characterX, int characterY, int itemX, int itemY){
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};
    queue<pair<int, int>> q;
    vector<vector<int>> visited(102, vector<int>(102, -1));
    
    q.push(make_pair(characterY, characterX));
    visited[characterY][characterX] = 0;
    
    while (!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        
        for(int i = 0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx >= maps.size() || ny >= maps.size()){
                continue;
            }
            if (maps[ny][nx] != 1){
                continue;
            }
            if (visited[ny][nx] != -1){
                continue;
            }
            
            q.push(make_pair(ny, nx));
            visited[ny][nx] = visited[y][x] + 1;
            
            if (nx == itemX && ny == itemY){
                return visited[ny][nx];
            }
        }
    }
    
    return visited[itemY][itemX];
}

void make_line(vector<vector<int>>& rectangle, vector<vector<int>>& maps){
    for(int i=0; i<rectangle.size(); i++){
        int sx = 2*rectangle[i][0];
        int sy = 2*rectangle[i][1];
        int ex = 2*rectangle[i][2];
        int ey = 2*rectangle[i][3];
        
        for(int x = sx; x <= ex; x++){
            for(int y = sy; y <= ey; y++){
                if (x == sx || x == ex || y == sy || y == ey){
                    if (maps[y][x] == 0){
                        maps[y][x] = 1;
                    }
                }
                else{
                    maps[y][x] = 2;
                }
            }
        }
    }
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    vector<vector<int>> maps(102, vector<int>(102, 0));
    
    make_line(rectangle, maps);
    
    characterX *= 2;
    characterY *= 2;
    itemX *= 2;
    itemY *= 2;
    
    answer = bfs(maps, characterX, characterY, itemX, itemY)/2;
    
    return answer;
}