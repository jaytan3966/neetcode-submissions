class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        e = len(s3)
        if n+m != e: return False

        i, j, k = 0, 0, 0

        while k<e:
            if i<n and s1[i] == s3[k]:
                i+=1
                k+=1
            elif j<m and s2[j] == s3[k]:
                j+=1
                k+=1
            else:
                return False
        return k==e