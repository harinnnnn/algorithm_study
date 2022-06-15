# 비트마스크 사용
# 참고 https://coder38611.tistory.com/136
from itertools import combinations
n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)

# 0, 1을 이용한 백트래킹 방법
# 참고 https://resilient-923.tistory.com/324
from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)