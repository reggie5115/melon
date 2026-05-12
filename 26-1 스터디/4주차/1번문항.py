#https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=python3

def solution(s):
    answer = []
    last_index = {}

    # 문자열을 한 글자씩 확인
    for i, ch in enumerate(s):

        if ch in last_index:  # 이전에 같은 문자가 나온 적이 있다면
            answer.append(i - last_index[ch])  # 현재 위치 - 이전 위치 = 거리
        else:
            answer.append(-1)

        last_index[ch] = i  # 현재 문자의 위치를 최신 위치로 갱신

    return answer
