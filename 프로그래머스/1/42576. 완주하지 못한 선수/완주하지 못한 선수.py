from collections import Counter

def solution(participant, completion):
    answer = ''
    part_count = Counter(participant)
    
    for comp in completion:
        part_count[comp] -= 1
    
    for person, cnt in part_count.items():
        if cnt == 1:
            return person
    
    return answer