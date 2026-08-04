class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for string in strs:
            encoded_str += str(len(string))+"#"+string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        str_li = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            i = j+1
            j = i+length

            string = s[i:j]
            str_li.append(string)

            i = j
            
        return str_li