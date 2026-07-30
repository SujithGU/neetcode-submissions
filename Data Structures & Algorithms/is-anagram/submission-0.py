class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        char_map_s = {}
        char_map_t = {}

        if len_s != len_t:
            return False
        else:
            for i in range(len_s):
                if char_map_s.get(s[i]) is None:
                    char_map_s[s[i]] = 1
                else:
                    char_map_s[s[i]] += 1

                if char_map_t.get(t[i]) is None:
                    char_map_t[t[i]] = 1
                else:
                    char_map_t[t[i]] += 1

            if len(char_map_s) != len(char_map_t):
                return False
            else:
                for key in char_map_s:
                    if char_map_s.get(key,None) != char_map_t.get(key,None):
                        return False
                return True
