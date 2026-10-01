class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        if stones[-1] == stones[-2]:
            stones.pop()
            stones.pop()
            print(stones)
        else:
            stones[-1] = stones[-1] - stones[-2]
            stones.remove(stones[-2])
            print(stones)
        return self.lastStoneWeight(stones)