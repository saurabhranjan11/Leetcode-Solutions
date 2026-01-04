class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def isprime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        total = 0
        for n in nums:
            p = round(n**(1/3))
            if p ** 3 == n and isprime(p):
                total += 1 + p + p*p + n
                continue

            for j in range(2,int(n**0.5) + 1):
                if n % j == 0:
                    i = (n//j)
                    if i != j and isprime(i) and isprime(j):
                        total += 1 + j + i + n
                    break
        return total