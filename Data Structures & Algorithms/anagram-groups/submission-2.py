from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_list = defaultdict(list)

        for word in strs:
            char_list = [0]*26

            for character in word:
                char_list[ord(character)-ord('a')]+=1
            
            anagram_list[tuple(char_list)].append(word)

        return list(anagram_list.values())