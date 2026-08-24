class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for word in strs:
            characters = [0] * 26

            for char in word:
                characters[ord(char)-ord("a")]+=1
            characters = tuple(characters)
            if characters not in table:
                table[characters] = [word]
            else:
                table[characters].append(word)
        return table.values()