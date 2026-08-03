class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_n = s.lower()
        L , R = 0,len(s)-1

        while L < R:
            if str_n[L].isalnum() and str_n[R].isalnum():
                if str_n[L]!=str_n[R]:
                    return False
                else:
                    L+=1
                    R-=1
            else:
                if not str_n[L].isalnum():
                    L+=1
                else:
                    R-=1
        
        return True