def solution(k, tangerine):
    answer = 0
    tan = [0]
    tangerine_dict = {0:0}
    
    for i in range(len(tangerine)):
        if tangerine_dict.get(tangerine[i]):
            tan[tangerine_dict[tangerine[i]]] += 1
        else:
            tangerine_dict[tangerine[i]] = len(tan)
            tan.append(1)
    
    tan.sort(reverse = True)
    
    for j in range(len(tan)):
        k -= tan[j]
        answer += 1
        
        if k <= 0:
            break
    
    return answer