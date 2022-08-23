from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        while prices != []:
            min_num = min(prices)
            min_index = prices.index(min_num)
            max_num = max(prices[min_index:])
            if (max_num - min_num) > highest:
                highest = max_num - min_num
            prices = prices[:min_index]
        return highest


if __name__ == "__main__":
    sol = Solution()
    input = [7, 1, 5, 3, 6, 4]
    ans = sol.maxProfit(input)
    print(ans)


"""
Solution

O(n) time
Throughout one iteration, at each stage
    - update if it is a new minimum
    - if it is not lower than the current number check if it returns a new highest profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit


"""
