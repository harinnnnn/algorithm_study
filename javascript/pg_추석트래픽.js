// https://unho94.tistory.com/m/204
function solution(lines) {
    var answer = 0;

    const timeline = {}     // 타임라인을 저장할 객체
  
    lines.map(v => v.split(' ')).forEach(v => {
        const hour = parseInt(v[1].slice(0, 2)) * 3600000       // 시간을 밀리초로 변경
        const minute = parseInt(v[1].slice(3, 5)) * 60000       // 분을 밀리초로 변경
        const second = parseFloat(v[1].slice(6)) * 1000         // 초를 밀리초로 변경
      
        let end = hour + minute + second 
        const duration = parseFloat(v[2].replace('s', '')) * 1000 
        const start = end - duration + 1          
        end += 1000                                
      
        timeline[start] = timeline[start] === undefined ? 1 : timeline[start] + 1  
        timeline[end] = timeline[end] === undefined ? -1 : timeline[end] - 1        
    })
  
    let cnt = 0
    Object.keys(timeline).sort((a,b) => a - b).forEach(v => {       
        cnt += timeline[v] 
        answer = Math.max(answer, cnt)
    })

    return answer;
}
