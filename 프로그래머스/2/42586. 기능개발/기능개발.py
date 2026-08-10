def solution(progresses, speeds):
    answer = [1]
    end_day = []

    for i in range(len(progresses)):
        left_work = 100 - progresses[i]
        finish_day = left_work // speeds[i]

        if left_work % speeds[i] > 0:
            finish_day += 1

        end_day.append(finish_day)

    day_cnt = end_day[0]
    day_idx = 0

    for i in range(1, len(end_day)):
        if end_day[i] <= day_cnt:
            answer[day_idx] += 1
        else:
            day_cnt = end_day[i]
            day_idx += 1
            answer.append(1)

    return answer