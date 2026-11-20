class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        def dfs(cur_digit, cur_num):
            if low <= cur_num <= high:
                ans.append(cur_num)

            if cur_digit>9 or cur_num>high:
                return
            
            cur_num = (cur_num*10)+cur_digit
            cur_digit+=1

            dfs(cur_digit, cur_num)
            
            return
        
        for i in range(1, 10):
            dfs(i+1, i)
        ans.sort()
        return ans