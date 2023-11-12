class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        maximum = max(temperatures)
        res =[]
        for idx, temperatureToday in enumerate(temperatures):
            if temperatureToday == maximum:
                res.append(0)
                continue
            days = 1
            while days+idx <=len(temperatures):
                if days+idx >= len(temperatures):
                    res.append(0)
                    break
                elif temperatures[days + idx] > temperatureToday:
                    res.append(days)
                    break

                days += 1

        return res


temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))

