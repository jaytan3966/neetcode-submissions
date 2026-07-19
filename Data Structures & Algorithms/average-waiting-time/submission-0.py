class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        n = len(customers)
        lastFinish = -1
        ans = 0
        for arriv, time in customers:
            lastFinish = max(lastFinish, arriv)+time
            ans+=(lastFinish-arriv)
        return ans/n
