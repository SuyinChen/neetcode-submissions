class Solution:
    def isValid(self, s: str) -> bool:
        #h = {')' : '(', '}' : '{', ']' : '['}
        h = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in range(len(s)):
            if s[i] in h.keys():
                stack.append(s[i])
            else:
                if not stack: 
                    return False
                if h[stack.pop()] != s[i]:
                    return False
                
        #(([]]
        if not stack:
            return True
        return False

        # stack = []
        # for i in range(len(s)):
        #     if s[i] not in h:
        #         stack.append(s[i])
        #     else:
        #         if stack and stack[-1] == h[s[i]]:
        #             stack.pop()
        #         else:
        #             return False
        # return False if stack else True


            