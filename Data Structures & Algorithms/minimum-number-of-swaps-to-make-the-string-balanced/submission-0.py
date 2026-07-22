class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        maxBalance = 0
        n = len(s)

        for i in range(n):
            if s[i] == '[':
                balance+=1
            else:
                balance-=1
                maxBalance = max(maxBalance, -balance)
        return (maxBalance+1)//2