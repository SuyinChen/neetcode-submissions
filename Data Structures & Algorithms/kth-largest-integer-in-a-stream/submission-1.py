class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
    # 1，2，3，3，3 -> 3
    # 1，2，3，3，3, 5 -> 3
    # 1，2，3，3，3, 5, 6 -> 3
    # 1，2，3，3，3, 5, 6, 7 -> 5
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
