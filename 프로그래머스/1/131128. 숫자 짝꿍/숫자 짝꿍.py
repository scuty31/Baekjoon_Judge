def solution(X, Y):
    answer = ''
    X_dict = {str(x):0 for x in range(10)}
    Y_dict = {str(y):0 for y in range(10)}
    X_list = list(X)
    Y_list = list(Y)
    
    for x in X_list:
        X_dict[x] += 1
    
    for y in Y_list:
        Y_dict[y] += 1
        
    pair_dict = dict()
    
    for i in range(10):
        x_cnt = X_dict[str(i)]
        y_cnt = Y_dict[str(i)]
        pair_dict[str(i)] = min(x_cnt, y_cnt)
    
    for i in reversed(range(10)):
        cnt = pair_dict[str(i)]
        if i == 0 and len(answer) == 0 and cnt != 0:
            answer += str(i)
            continue
        answer += str(i) * cnt
    
    if len(answer) == 0:
        answer = '-1'
    
    return answer