class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i, char in enumerate(s):
            if char == "(":
                left_stack.append(("(", i))
            elif char == ")":
                if len(left_stack) > 0:
                    left_stack = left_stack[:-1]
                elif len(star_stack) > 0:
                    star_stack = star_stack[:-1]
                else:
                    return False
            elif char == "*":
                star_stack.append(("*", i))
        if len(left_stack) > len(star_stack):
            print("false because left")
            return False
        for i in range(len(left_stack)-1, -1, -1):
            j = len(star_stack) - len(left_stack) + i
            if left_stack[i][1] > star_stack[j][1]:
                print(f"false because, {left_stack}, {star_stack}")
                return False
        return True
                