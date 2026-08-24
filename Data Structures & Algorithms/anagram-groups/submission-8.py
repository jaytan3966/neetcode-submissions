class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        for word in strs:
            lets = [0]*26
            for i in range(len(word)):
                lets[ord(word[i])-ord('a')]+=1
            
            lets = tuple(lets)
            if lets in seen:
                seen[lets].append(word)
            else:
                seen[lets] = [word]
        
        ans = []
        for lets in seen:
            ans.append(seen[lets])
        
        return ans