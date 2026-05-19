class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse = True)

        while len(stones) > 1:
            remainder = stones[0] - stones[1]
            print(stones)
            print(remainder)
            if remainder > 0:
                stones.append(remainder)
            stones = sorted(stones[2:], reverse = True)
                
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

        