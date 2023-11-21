class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter, longer = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        gcd= ""
        for i in range(1, len(longer)//2+1):
            print("start: " + longer[:i])
            print("end: " + longer[-i:])
            if longer[:i] == longer[-i:]:
                gcd = longer[:i]


                # return gcd
        return gcd


solution = Solution()
print(solution.gcdOfStrings(str1 = "ABABABAB", str2 = "ABAB"))