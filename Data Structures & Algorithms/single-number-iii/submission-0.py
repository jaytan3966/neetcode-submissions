class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        # Find a bit where the two unique numbers differ
        diff_bit = xor & -xor

        a = 0
        b = 0

        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]