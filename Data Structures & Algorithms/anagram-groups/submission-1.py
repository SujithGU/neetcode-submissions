class Solution:
    def get_anagram_dict(self,data):
        ana_dict = {}
        for character in data:
            ana_dict[character] = ana_dict.get(character,0)+1
        return ana_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_len_dict_tracker = {}
        output_list = []
        ana_word_tracker = {}

        for word in strs:
            anagram_dict = self.get_anagram_dict(word)
            word_len = len(word)

            if ana_len_dict_tracker.get(word_len) is None:
                g_idx = len(output_list)
                ana_len_dict_tracker[word_len] = [(anagram_dict,g_idx)]
                output_list.append([word])
            else:
                list_data = ana_len_dict_tracker[word_len]
                match_found = False

                for data,idx in list_data:
                    if anagram_dict == data:
                        output_list[idx].append(word)
                        match_found = True
                        break
                if not match_found:
                    g_idx = len(output_list)
                    ana_len_dict_tracker[word_len].append((anagram_dict,g_idx))
                    output_list.append([word])
        
        return output_list

            

