class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if 2 * offset == i:
                offset *= 2

            output[i] = output[i - offset] + 1
        return output