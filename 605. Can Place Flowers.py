class Solution:
    def canPlaceFlowers(self, flowerbed, n: int):
        if n < 1:
            return True
        if flowerbed == [0]: return True if n == 1 else False
        spot = 1
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n >= 1:
            n -= 1
            flowerbed[0] = 1
            spot = 2

        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n >= 1:
            n -= 1
            flowerbed[-1] = 1

        if n < 1:
            return True

        while spot < len(flowerbed):
            if n < 1:
                return True

            if flowerbed[spot] == 1:
                spot += 1
                continue

            if flowerbed[spot] == 0 and flowerbed[spot - 1] == 0 and flowerbed[spot + 1] == 0:
                flowerbed[spot] = 1
                n -= 1
                if n < 1 and spot < len(flowerbed): return True
                spot += 2
                continue

            spot += 1
        return False