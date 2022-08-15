class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            index = t.find(c)
            if index == -1:
                return False
            t = t[index + 1 :]
        return True


if __name__ == "__main__":
    solution = Solution()
    out = solution.isSubsequence("ace", "ahbdcoce")
    print(out)
