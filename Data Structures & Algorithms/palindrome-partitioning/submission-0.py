class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        n = len(s)

        def dfs(l, r):
            if r >= n:
                if l == r:
                    ans.append(cur.copy())
                return

            if isPalindrome(s, l,r):
                cur.append(s[l:r+1])
                dfs(r+1,r+1)
                cur.pop()
            dfs(l, r+1)
            
        def isPalindrome(s, l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        dfs(0,0)
        return ans