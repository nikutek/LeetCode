class Solution:
    def reverseVowels(self, s):
        allPossibleVowels = 'aeiou'
        vowelsInWord = []
        s=list(s)
        for idx, letter in enumerate(s):
            if letter.lower() in allPossibleVowels:
                s[idx] = '_'
                vowelsInWord.append(letter)

        for idx, letter in enumerate(s):
            if letter == '_':
                s[idx] = vowelsInWord[-1]
                vowelsInWord.pop()

        return ''.join(s)


s = Solution()
print(s.reverseVowels("hello"));
