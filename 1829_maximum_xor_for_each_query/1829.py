from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (2 ** maximumBit) - 1
        out = []
        total = 0

        for i in nums:
            total ^= i
            out.append(total ^ max_val) 
        return out.reverse()

def main():
    #nums = [0,1,1,3]
    #nums = [2,3,4,7]
    nums = [0,1,2,2,5,7]
    max_bit = 3
    sol = Solution()
    out = sol.getMaximumXor(nums, max_bit)
    print(out)

if __name__ == "__main__":
    main()
