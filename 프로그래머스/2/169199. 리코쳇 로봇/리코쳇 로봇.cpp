#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int move(vector<string>& board, pair<int, int> r, pair<int, int> g){
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};
    int n = board.size();
    int m = board[0].size();
    queue<pair<int, int>> q;
    vector<vector<int>> visited(n, vector<int>(m, -1));
    int result = -1;
    
    q.push(r);
    visited[r.first][r.second] = 0;
    
    while (!q.empty()){
        pair<int, int> player = q.front();
        int x = player.first;
        int y = player.second;
        q.pop();
        
        for(int i = 0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx < 0 || ny < 0 || nx >= n || ny >= m){
                continue;
            }
            if(board[nx][ny] == 'D'){
                continue;
            }
            
            int mx = nx;
            int my = ny;
            
            while (true){
                mx = nx + dx[i];
                my = my + dy[i];
                
                if (mx < 0 || my < 0 || mx >= n || my >= m){
                    break;
                }
                if (board[mx][my] == 'D'){
                    break;
                }
                
                nx = mx;
                ny = my;
            }
            
            if (visited[nx][ny] == -1 || visited[nx][ny] > visited[x][y] + 1){
                visited[nx][ny] = visited[x][y] + 1;
                q.push(make_pair(nx, ny));
            }
            
            if(nx == g.first && ny == g.second){
                result = visited[nx][ny];
                return result;
            }
        }
    }
    
    return -1;
}

int solution(vector<string> board) {
    int answer = 0;
    pair<int, int> r;
    pair<int, int> g;
    
    for(int x = 0; x < board.size(); x++){
        for(int y = 0; y < board[0].size(); y++){
            if(board[x][y] == 'R'){
                r = {x, y};
            }
            else if(board[x][y] == 'G'){
                g = {x, y};
            }
        }
    }

    if(g.first > 0 && g.first < board.size()-1 && g.second > 0 && g.second < board[0].size()-1){
        int x = g.first;
        int y = g.second;

        if(board[x-1][y] != 'D' && board[x+1][y] != 'D' && board[x][y-1] != 'D' && board[x][y+1] != 'D'){
            return -1;
        }
    }
    
    answer = move(board, r, g);
    
    return answer;
}