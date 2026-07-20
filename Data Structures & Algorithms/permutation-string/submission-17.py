class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        if len(s1)>len(s2):
            return False

        count1 = [0]*26
        count2 = [0]*26

        for _ in range(len(s1)):
            count1[ord(s1[_])-ord('a')]+=1
            count2[ord(s2[_])-ord('a')]+=1
        i = 0
        for j in range(len(s1), len(s2)+1):
            if count1==count2:
                return True
            if j<len(s2):
                count2[ord(s2[i])-ord('a')]-=1
                count2[ord(s2[j])-ord('a')]+=1
                i+=1
        
        return False