class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            charCounts = [0]*26
            for i in range(len(word)):
                charCounts[ord(word[i])-ord('a')]+=1
            
            tup = tuple(charCounts)
            if tup not in seen:
                seen[tup] = [word]
            else:
                seen[tup].append(word)
        ans = []
        for key in seen:
            ans.append(seen[key])
        return ans