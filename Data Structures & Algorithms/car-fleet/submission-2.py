class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        time = 0
        count = 1
        flag = 0
        for p,s in sorted(pair)[::-1]:
            d = (target - p)/s
            if flag == 0:
                time = d
                flag = 1
            if d > time:
                count += 1
                time = d
        return count