class Solution:
    def myAtoi(self, str: str) -> int:
        min = -2147483648
        max = 2147483647
        value = 0
        type = 1
        text = "0"
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            elif str[i] in ['+', '-'] or str[i].isdigit():
                if str[i] == "+":
                    type = 1
                elif str[i] == "-":
                    type = -1
                else:
                    text += str[i]
                j = i + 1
                while j < len(str) and str[j].isdigit():
                    text += str[j]
                    j = j + 1
                value = int(text) * type
                if value > max:
                    value = max
                elif value < min:
                    value = min
                break
            else:
                break

        return value

if __name__ == '__main__':
    s = ""
    S = Solution()
    print(S.myAtoi("  0000000000012345678"))