function solution(n, times) {
    times.sort((a,b) => a-b); // 일단 검사시간 작은 심사관부터 계산하기 위해 오름차순 정렬
    let left = 1; // 최소로 걸릴 시간
    let right = n * times[times.length -1]; // 최대로 걸릴 시간(일단 최고로 오래 걸리는 심사관이 n명을 다 검사했을 때의 시간임)
    let answer = right; // 최대값.

    while(left <= right){ // 이분탐색 시작
        let mid = Math.floor((left + right) / 2);
        let count = 0 // 한 사람당 검사할 수 있는 사람 수
                        
        times.forEach(value => {
            count += Math.floor(mid / value); // 한 사람당 몇명 할 수 있는지
            if(count >= n) { // 총 검사대상자 보다 한 사람당 할 수 있는 능력치가 더 큰경우
                answer = Math.min(mid, answer); // 시간의 최솟값
                return;
            };
        });
        if (count >= n) { // 찾는 값과 다를 경우 탐색범위 축소
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    return answer;
}
        

// 코드가 더 깔끔
function solution(n, times) {
  let left = 1;
  let right = n * Math.max(...times);

  while (left < right) {
    const temp = Math.floor((left + right) / 2);

    const count = times.reduce((acc, time) => {
      return acc + Math.floor(temp / time);
    }, 0);

    if (count >= n) {
      right = temp; // 이 코드는 right를 temp-1로 안두고 temp로 둠 .. !
    } else {
      left = temp + 1;
    }
  }

  return right;
}
