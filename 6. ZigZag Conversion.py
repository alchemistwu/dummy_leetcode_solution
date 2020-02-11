class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_of_lists = ['' for _ in range(numRows)]
        total_index = 0
        flag = True
        line_index = 0
        step = 1
        while (total_index < len(s)):
            if (line_index < numRows and flag) or (line_index >= 0 and not flag):
                list_of_lists[line_index] += s[total_index]
                total_index += 1
                line_index += step
            else:
                if flag:
                    flag = False
                    if numRows == 1:
                        line_index = 0
                    else:
                        line_index = numRows - 2
                    step = -1
                else:
                    flag = True
                    if numRows == 1:
                        line_index = 0
                    else:
                        line_index = 1
                    step = 1
        final_string = ""
        for i in list_of_lists:
            final_string += i
        return final_string

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 4
    # s = "AB"
    # numRows = 1
    S = Solution()
    S.convert(s, numRows)