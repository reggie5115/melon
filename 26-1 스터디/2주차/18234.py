import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrots = [tuple(map(int, input().split())) for _ in range(N)]

carrots.sort(key=lambda x: x[1])

answer = 0

for i in range(N):
    w, p = carrots[i]
    answer += w + (T - N + i) * p

print(answer)
