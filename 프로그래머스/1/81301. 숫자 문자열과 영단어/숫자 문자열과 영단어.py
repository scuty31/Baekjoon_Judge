def solution(s):
    eng_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num, eng in enumerate(eng_num):
        s = s.replace(eng, str(num))

    answer = int(s)

    return answer