class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter, longer = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        longestSubstring = ""
        for substringLength in range(1, len(shorter)+1):
            if len(shorter) % substringLength == 0 and len(longer) % substringLength == 0:
                shortCombined = shorter[:substringLength] * (len(shorter)//substringLength)
                longCombined = shorter[:substringLength] * (len(longer)//substringLength)
                if shortCombined == shorter and longCombined == longer:
                    print('short: ', shortCombined, "long: ", longCombined)
                    longestSubstring = shorter[:substringLength]

        return longestSubstring


solution = Solution()
print(solution.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))