class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        i = len(digits) - 1
        digits[i] += 1

        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
