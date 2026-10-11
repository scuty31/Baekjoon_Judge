def check_finish(n, year, month, day, t_year, t_month, t_day):
    month += n
    
    if month > 12 and month % 12 != 0:
        year += month // 12
        month %= 12
    elif month > 12 and month % 12 == 0:
        year += month // 12 - 1
        month = 12
    
    if year < t_year:
        return True
    elif year > t_year:
        return False
    
    if month < t_month:
        return True
    elif month > t_month:
        return False
    
    if day <= t_day:
        return True

    return False


def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    tyear_str, tmonth_str, tday_str = today.split('.')
    
    t_year = int(tyear_str)
    t_month = int(tmonth_str)
    t_day = int(tday_str)
    
    for term in terms:
        a, b = term.split()
        term_dict[a] = int(b)
        
    for i in range(len(privacies)):
        privacy = privacies[i]
        date, a = privacy.split()
        year_str, month_str, day_str = date.split('.')
        
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
        
        if check_finish(term_dict[a], year, month, day, t_year, t_month, t_day):
            answer.append(i+1)
        
    return answer