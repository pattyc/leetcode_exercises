class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 0
        i = 0
        while num < n:
            num = pow(3, i)
            if num == n:
                return True
            i += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    input = 27
    ans = sol.isPowerOfThree(input)
    print(ans)
