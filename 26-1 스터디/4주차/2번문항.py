#https://school.programmers.co.kr/learn/courses/30/lessons/389479

def solution(players, m, k):
    answer = 0

    # expire[t] = t시에 반납되는 서버 수
    expire = [0] * 25

    current = 0  # 현재 운영 중인 서버 수

    for hour in range(24):
        # 반납 처리
        current -= expire[hour]

        # 현재 시간에 필요한 서버 수
        need = players[hour] // m

        # 부족하면 증설
        if need > current:
            add = need - current
            answer += add
            current += add

            # k시간 뒤 반납 예약
            if hour + k <= 24:
                expire[hour + k] += add

    return answer
