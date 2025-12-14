class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        seat = corridor.count("S")
        if seat == 0 or seat % 2 != 0:
            return 0

        ways = 1
        seat_count = 0
        plant_count = 0

        for ch in corridor:
            if ch == "S":
                seat_count += 1
                if seat_count > 2 and seat_count % 2 == 1:
                    ways = (ways * (plant_count + 1) % mod)
                    plant_count = 0
            else:
                if seat_count % 2 == 0 and seat_count > 0:
                    plant_count += 1
        return ways