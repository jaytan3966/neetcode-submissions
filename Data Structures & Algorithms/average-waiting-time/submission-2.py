class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last = -1

        total_waiting_time = 0
        for arrival, time in customers:
            if last == -1:
                last = arrival+time
                total_waiting_time = time
            else:
                last = max(last, arrival) + time
                total_waiting_time+=(last-arrival)
            
        
        return total_waiting_time/len(customers)