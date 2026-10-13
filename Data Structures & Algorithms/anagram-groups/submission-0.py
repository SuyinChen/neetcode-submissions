class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {(1,0,0,0,1,0,...,0,1,0,...): ["eat", "tea", "ate"]}
        result = defaultdict(list)
        for string in strs:
            # initialize count for a-z
            count = [0] * 26
            for character in string:
                # counting how many characters are there in this word
                count[ord(character) - ord('a')] += 1
                # [1, 0, 0, 0, 1, 0, 0, ... , 0, 1, 0, 0, 0, 0, 0, 0]
            result[tuple(count)].append(string)
        return list(result.values())