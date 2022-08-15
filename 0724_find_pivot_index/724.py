class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i, x in enumerate(nums):
            if left_sum == (total_sum - left_sum - x):
                return i
            left_sum += x
        return -1
        

if __name__ == "__main__":
    sol = Solution()
    input = [1,7,3,6,5,6]
    ans = sol.pivotIndex(input)
    print(ans)
