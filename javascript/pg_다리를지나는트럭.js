function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = Array.from({ length: bridge_length }, () => 0);

    while (bridge.length) {
      bridge.shift();
      answer += 1;

      if (truck_weights.length) {
        let sum = bridge.reduce(function add(sum, curValue) {
          return sum + curValue;
        });

        if (sum + truck_weights[0] <= weight) {
          bridge.push(truck_weights.shift());
        } else {
          bridge.push(0);
        }
      }
    }

    return answer;
}
