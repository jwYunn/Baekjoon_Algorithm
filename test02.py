def check_diff_one(a, b, c):
    if a == b and b != c:
        return 2
    if b == c and c != a:
        return 0
    if c == a and a != b:
        return 1
    
def check_rest(isMax, a, b, c):
    value = 0
    
    if isMax:
        value = max(a, b, c)
    else:
        value = min(a, b, c)

    if value == a:
        return [1, 2]
    if value == b:
        return [0, 2]
    if value == c:
        return [0, 1]
    
def check_win_group(a, b, c):
    if a == 0:
        return 2
    if b == 0:
        return 0
    if c == 0:
        return 1  
    return
    
    
def check_lose_group(a, b, c):
    if a == 0:
        return 1
    if b == 0:
        return 2
    if c == 0:
        return 0  
    return
    
def check_win_two(isWin ,a, b):
    if a == 1 and b == 2:
        if isWin:
            return 2
        else:
            return 1
    if a == 0 and b == 2:
        if isWin:
            return 0
        else:
            return 2
    if a == 0 and b == 1:
        if isWin:
            return 1
        else:
            return 0



def solution(n, m, points, hands):
    answer = 0
    persons = [0] * n
    
    for i in range(m):
        print("hands", hands[i])
        print("points", points)
        print("persons", persons)
        array = [[], [], []]
        
        idx = 0
        for j in hands[i]:
            if j == "S":
                array[0].append(idx)
            elif j == "R":
                array[1].append(idx)
            else:
                array[2].append(idx)
            idx += 1
        
        point = points[i]
        print(array)
        
        s_count = len(array[0])
        r_count = len(array[1])
        p_count = len(array[2])
        
        # 모양이 한 가지인 경우
        if s_count == n or r_count == n or p_count == n:
            print(1)
            if i != m - 1:
                points[i + 1] += point
            continue
            
        # 모양이 세 가지인 경우
        elif s_count != 0 and r_count != 0 and p_count != 0:
            # 세 그룹의 크기가 모두 같은 경우
            if s_count == r_count and r_count == p_count:
                print(2)
                if i != m - 1:
                    points[i + 1] += point
                continue
                
            # 그룹의 크기가 모두 다른 경우
            elif s_count != r_count and r_count != p_count and s_count != p_count:
                # 라운드에 걸린 점수가 0 이상인 경우
                if points[i] >= 0:
                    print(3)
                    result = check_rest(True, s_count, r_count, p_count)
                    num = check_win_two(True, result[0], result[1])
                    for k in array[check_win_two(True, result[0], result[1])]:
                        persons[k] += point
                    
                # 라운드에 걸린 점수가 음수인 경우
                else:
                    print(4)
                    result = check_rest(False, s_count, r_count, p_count)
                    for k in array[check_win_two(False, result[0], result[1])]:
                        persons[k] += point
                
            # 두 그룹의 크기가 같은 경우
            else:
                print(5)
                num = check_diff_one(s_count, r_count, p_count)
                for k in array[num]:
                    persons[k] += point
                continue
                

        # 모양이 두 가지인 경우
        else:
         # 라운드에 걸린 점수가 0 이상인 경우
            if points[i] >= 0:
                print(6)
                num = check_win_group(s_count, r_count, p_count)
                for k in array[num]:
                    persons[k] += point
            # 라운드에 걸린 점수가 음수인 경우
            else:
                print(7)
                num = check_lose_group(s_count, r_count, p_count)
                for k in array[num]:
                    persons[k] += point
    
    answer = max(persons)
    print(persons)
    return answer

val = solution(7, 1, [5], ["RSSPPPP"])
print(val)