function solution(str1, str2) {
    var answer = '';
    
    const maxStrLength = Math.max(str1.length, str2.length);

    for (let i = 0; i < maxStrLength; i++) 
        answer += str1[i] + str2[i];
    
    return answer;
}
