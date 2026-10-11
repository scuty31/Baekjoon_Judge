def solution(players, callings):
    answer = []
    player_dict = dict()
    
    for i in range(len(players)):
        player_dict[players[i]] = i
        
    for call in callings:
        idx = player_dict[call]
        pre_player = players[idx-1]
        
        players[idx-1] = call
        players[idx] = pre_player
        
        player_dict[pre_player] = idx
        player_dict[call] = idx-1
        
    return players