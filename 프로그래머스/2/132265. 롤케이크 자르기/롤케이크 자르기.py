def solution(topping):
    answer = 0
    left_topping = {topping[0]:1}
    right_topping = dict()
    left_cnt = 1
    right_cnt = 0
    
    for i in range(1, len(topping)):
        if right_topping.get(topping[i]):
            right_topping[topping[i]] += 1
        else:
            right_topping[topping[i]] = 1
            right_cnt += 1
    
    for i in range(1, len(topping)):
        if left_cnt > right_cnt:
            break
        elif left_cnt == right_cnt:
            answer += 1
        
        now_topping = topping[i]
        
        if left_topping.get(now_topping):
            left_topping[now_topping] += 1
        else:
            left_topping[now_topping] = 1
            left_cnt += 1
        
        right_topping[now_topping] -= 1
        
        if right_topping[now_topping] == 0:
            right_cnt -= 1
    
    return answer