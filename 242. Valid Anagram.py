class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True
        else:
            tmp_dict = {}
            for i in range(len(s)):
                if s[i] not in tmp_dict.keys():
                    tmp_dict[s[i]] = 1
                else:
                    tmp_dict[s[i]] += 1

                if t[i] not in tmp_dict.keys():
                    tmp_dict[t[i]] = -1
                else:
                    tmp_dict[t[i]] -= 1

            for key in tmp_dict.keys():
                if tmp_dict[key] != 0:
                    return False
        return True