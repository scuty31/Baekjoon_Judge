def solution(book_time):
    answer = 0
    book_time_min = []
    room = []
    
    for i in range(len(book_time)):
        a, b = book_time[i]
        a_hour, a_min = map(int, a.split(':'))
        b_hour, b_min = map(int, b.split(':'))
        
        a_time = a_hour*60 + a_min
        b_time = b_hour*60 + b_min + 10
        
        book_time_min.append((a_time, b_time))
    
    book_time_min.sort()
    
    for i in range(len(book_time)):
        s, e = book_time_min[i]
        
        if len(room) == 0:
            room.append(e)
            continue
        
        is_batch = False
        
        for i in range(len(room)):
            if room[i] <= s:
                room[i] = e
                is_batch = True
                break
        
        if not is_batch:
            room.append(e)
    
    answer = len(room)
    
    return answer