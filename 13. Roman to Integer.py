class Solution:
    def romanToInt(self, s: str) -> int:
        val_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val = 0
        pos = 0
        while (pos < len(s)):
            if pos < len(s) - 1:
                tmp_val = val_dict[s[pos + 1]] - val_dict[s[pos]]
                if tmp_val > 0:
                    pos += 1
                    val += tmp_val
                else:
                    val += val_dict[s[pos]]
            else:
                val += val_dict[s[pos]]
            pos += 1
        return val
