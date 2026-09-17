class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
    
        def dfs(i, remaining, count):
            if remaining == 0:
                return count
            
            if i>=n:
                return -1
                
            if coins[i]>remaining:
                return dfs(i+1, remaining, count)
            else:
                return dfs(i, remaining-coins[i], count+1)
            
        return dfs(0, amount, 0)
        