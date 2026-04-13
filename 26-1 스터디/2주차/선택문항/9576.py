T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(M)]
    
    # b 기준 정렬
    students.sort(key=lambda x: x[1])
    
    used = [False] * (N + 1)
    count = 0
    
    for a, b in students:
        for book in range(a, b + 1):
            if not used[book]:
                used[book] = True
                count += 1
                break
    
    print(count)
