class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0: heapq.heappush(h, (-a, 'a'))
        if b > 0: heapq.heappush(h, (-b, 'b'))
        if c > 0: heapq.heappush(h, (-c, 'c'))

        ans = ''
        cur = None
        while h:
            cnt, letter = heapq.heappop(h)
            print(cnt, letter, cur, ans)
            if h and cur and cur[0] == 2 and cur[1] == letter:
                filCnt, filLetter = heapq.heappop(h)
                filCnt+=1
                ans+=filLetter
                cur = (1, filLetter)
                print(filCnt, cur)
                if filCnt<0: heapq.heappush(h, (filCnt, letter))

            if cur and cur[1]==letter and cur[0]==2: 
                continue

            cnt+=1
            ans+=letter

            if cur and cur[1] == letter: cur = (2, letter)
            else: cur = (1, letter)

            if cnt < 0: heapq.heappush(h, (cnt, letter))
        return ans
