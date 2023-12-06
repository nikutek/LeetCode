class Solution:
    def productExceptSelf(self, nums):
        res = [1 for i in range(len(nums))]

        for idx, i in enumerate(nums):
            for j in range(len(res)):
                if j != idx:
                    res[j] = res[j] * i

        print(res)
        return res