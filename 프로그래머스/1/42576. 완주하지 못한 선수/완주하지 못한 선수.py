def solution(participant, completion):
    answer = ''
    people = dict()
    
    for p in participant:
        if people.get(p):
            people[p] += 1
        else:
            people[p] = 1
    
    for c in completion:
        people[c] -= 1
    
    for person, complete in people.items():
        if complete:
            answer = person
            break
    
    return answer