def solution(players, callings):
    res = {player: i for i, player in enumerate(players)} 
    for i in callings:
        idx = res[i] 
        res[i] -= 1 
        res[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1] 
    return players
