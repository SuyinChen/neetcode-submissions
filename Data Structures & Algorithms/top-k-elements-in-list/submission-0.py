class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            # count = {1:4} 1 appears 4 times
            count[n] = 1 + count.get(n, 0)
        # put in the bucket based on the count
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        # from len(freq) - 1 to 1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
