from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        val_dict = OrderedDict()
        for i in range(len(s)):
            if s[i] not in val_dict.keys():
                val_dict[s[i]] = [1, i]
            else:
                val_dict[s[i]][0] = val_dict[s[i]][0] + 1

        for key, val in val_dict.items():
            if val[0] == 1:
                return val[1]
        return -1
