function solution(board, moves) {
  var answer = 0;
  let basket = [];

  moves.forEach((m) => {
    for (let i = 0; i < board.length; i++) {
      if (board[i][m - 1] === 0) {
        continue;
      } else {
        let current = board[i][m - 1];
        board[i][m - 1] = 0;
        if (basket.length && current === basket[basket.length - 1]) {
          basket.pop();
          answer += 2;
        } else basket.push(current);
        return;
      }
    }
  });

  return answer;
}
