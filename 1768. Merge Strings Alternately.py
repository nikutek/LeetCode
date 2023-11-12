class Solution:
    class Solution:
        def mergeAlternately(self, word1: str, word2: str) -> str:
            shorter = word1 if len(word1) <= len(word2) else word2
            longer = word1 if shorter == word2 else word2
            result = ''
            for i in range(len(shorter)):
                result += word1[i] + word2[i]
            if len(longer) > len(shorter):
                result += longer[(len(longer) - len(shorter)):]

            return result


solution = Solution()
print(solution.mergeAlternately('cdf', 'a'))
