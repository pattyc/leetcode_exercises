class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        while i < len(s):
            match s[i]:
                case 'I':
                    if i+1 < len(s):
                        if s[i+1] == 'V':
                            num += 4
                            i += 2
                            continue
                        elif s[i+1] == 'X':
                            num += 9
                            i += 2
                            continue
                    num += 1
                case 'V':
                    num += 5
                case 'X':
                    if i+1 < len(s):
                        if s[i+1] == 'L':
                            num += 40
                            i += 2
                            continue
                        elif s[i+1] == 'C':
                            num += 90
                            i += 2
                            continue
                    num += 10
                case 'L':
                    num += 50
                case 'C':
                    if i+1 < len(s):
                        if s[i+1] == 'D':
                            num += 400
                            i += 2
                            continue
                        elif s[i+1] == 'M':
                            num += 900
                            i += 2
                            continue
                    num += 100
                case 'D':
                    num += 500
                case 'M':
                    num += 1000
                case _:
                    return -1
            i += 1
        return num

if __name__ == "__main__":
    sol = Solution()
    r1 = "III"
    r2 = "LVIII"
    r3 = "DCXXI"
    print(sol.romanToInt(r1))
    print(sol.romanToInt(r2))
    print(sol.romanToInt(r3))
