class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        seen = {}
        for word in strs:
            chars = [0]*26
            for i in range(len(word)):
                chars[ord(word[i])-ord('a')]+=1
            chars = tuple(chars)
            if chars in seen:
                seen[chars].append(word)
            else:
                seen[chars] = [word]
        
        ans = []
        for arr in seen:
            ans.append(seen[arr])
        return ans
