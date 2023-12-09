class Solution(object):
    def increasingTriplet(self, nums):
        if len(set(nums)) < 3: return False

        for idxi, i in enumerate(nums):
            greater_than_i = list(filter(lambda x: x > i, nums[idxi:]))
            if len(greater_than_i) < 2: continue
            for j in greater_than_i:
                greater_than_j = list(filter(lambda x: x > j, greater_than_i[greater_than_i.index(j):]))
                if len(greater_than_j) > 0:
                    print(i,j, greater_than_j[0])
                    return True
        return False




s = Solution()
s.increasingTriplet([1,5,0,4,1,3])