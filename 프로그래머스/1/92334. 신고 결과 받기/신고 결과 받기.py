def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    ban_list = []
    report_dict = dict()
    id_dict = dict()
    
    for i in range(len(id_list)):
        report_dict[id_list[i]] = set()
        id_dict[id_list[i]] = i
    
    for i in range(len(report)):
        a, b = report[i].split()
        report_dict[a].add(b)
    
    report_cnt = [0 for _ in range(len(id_list))]
    
    for key, value in report_dict.items():
        for ban in value:
            report_cnt[id_dict[ban]] += 1
    
    for i in range(len(report_cnt)):
        if report_cnt[i] >= k:
            ban_list.append(id_list[i])

    for key, value in report_dict.items():
        for ban in value:
            if ban in ban_list:
                answer[id_dict[key]] += 1
        
    return answer