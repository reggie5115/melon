T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(M)]
    
    score = [0] * (N + 1)
    
    for a, b in students:
        for i in range(a, b + 1):
            score[i] += 1
    
    used = [False] * (N + 1)
    
    count = 0
    
    for a, b in students:
        min_score = float('inf')
        chosen_book = -1
        
        for i in range(a, b + 1):
            if not used[i]:
                if score[i] < min_score:
                    min_score = score[i]
                    chosen_book = i
        
        if chosen_book != -1:
            used[chosen_book] = True
            count += 1
    
    print(count)
