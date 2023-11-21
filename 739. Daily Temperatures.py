class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res =[]
        for idx, temperatureToday in enumerate(temperatures, start=1):
            foundFlag = False
            for daysElapsed, temp in enumerate(temperatures[idx:], start=1):
                if temp > temperatureToday:
                    res.append(daysElapsed)
                    foundFlag = True
                    break
            if not foundFlag: res.append(0)
        return res


temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))

