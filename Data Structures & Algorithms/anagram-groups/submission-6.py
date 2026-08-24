class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        n = len(strs)

        for i in range(n):
            alpha = [0]*26

            for c in range(len(strs[i])):
                alpha[ord(strs[i][c])-ord('a')]+=1
            
            if tuple(alpha) in words:
                words[tuple(alpha)].append(strs[i])
            else:
                words[tuple(alpha)] = [strs[i]]
        
        ans = []
        for word in words:
            ans.append(words[word])
        return ans
        