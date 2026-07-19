class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def stoi(num):
            res = 0
            power = len(num) - 1
            for i in range(len(num)):
                res += int(num[i]) * (10**power)
                power -= 1
            return res


            
        return str(stoi(num1) * stoi(num2))
