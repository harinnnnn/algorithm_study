s = input()
stack = []
temp = 1 # temp 초기값이 0이면 아무리 곱해도 0이므로 1로 선언
answer = 0

for i in range(len(s)):
    if (s[i] == '('): # 열린 괄호들은 각각의 값을 temp에 곱해두고 stack에 푸쉬.
        temp *= 2
        stack.append(s[i])
    elif (s[i] == '['): # 열린 괄호들은 각각의 값을 temp에 곱해두고 stack에 푸쉬.
        temp *= 3
        stack.append(s[i])

    elif (s[i] == ')'): # 닫힌 괄호의 경우, 
        if not stack or stack[-1] == '[': # 스택의 top에 있는 괄호와 비교 후 다른 괄호쌍이면 바로 종료.
            answer = 0
            break
        if (s[i-1] == '('): # 같은 괄호 쌍이면 정답에 temp값을 더해주고
            answer += temp
        temp //= 2 # temp는 해당 괄호를 제외한 값으로 다시 돌려놓음.
        stack.pop() # pop 잊지 말기
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if (s[i-1] == '['):
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    answer = 0

print(answer)

    