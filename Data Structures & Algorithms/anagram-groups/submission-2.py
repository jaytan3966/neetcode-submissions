class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        anagrams = {}
        for word in strs:
            letters = [0]*26
            for char in word:
                letters[ord(char)-ord('a')]+=1
            if tuple(letters) in anagrams:
                anagrams[tuple(letters)].append(word)
            else:
                anagrams[tuple(letters)] = [word]
        ans = []
        for item in anagrams.values():
            ans.append(item)
        return ans
            