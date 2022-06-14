n, k = map(int, input().split()) # n은 물건의 개수, k는 배낭에 넣을 수 있는 최대 무게
dp = [[0] * (k+1) for _ in range(n+1)] # dp배열의 값은 무게가 j이하인 것 중에서 i번째 물건까지 고려했을 때 "가치"임. 
stuff = [[0, 0]] # stuff 배열에 각 물건 별 무게, 가치 받아서 넣어줄 거임.

for _ in range(n): # 물건의 개수(N)만큼 입력받아야 함.
    stuff.append(list(map(int, input().split()))) # 한줄(물건 하나)씩 입력 받아서 추가.

for i in range(n + 1): # stuff 배열이 [0,0]부터 시작이므로 n+1, k+1 해주어야 함. (물건은 4개긴 한데 배열이 5 * 5 배열이라서.)
    for j in range(k + 1): # 걍 이 반복문에서 dp 배열 채워주는거라고 생각하면 됨 !
        weight = stuff[i][0]
        value = stuff[i][1]

        if weight > j: # 현재 배낭의 무게보다 현재 물건이 더 무거워서 못 넣는 경우
            dp[i][j] = dp[i - 1][j] # 이전의 가치가 그대로 유지됨.
        else: # 현재 물건을 넣을 수는 있지만, 기존 무게에서 무언가를 빼고 현재껄 넣을지, 현재껄 안넣고 기존상태를 유지할지는 최댓값으로 결정.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k]) # 넣을 수 있는 최대 가치를 구하는거니까 당연히 dp 배열의 가장 마지막 인덱스 값이 답이 됨.
