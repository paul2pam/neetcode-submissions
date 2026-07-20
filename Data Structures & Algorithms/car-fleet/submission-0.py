class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars)


        stack = []
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            while len(stack) > 0 and stack[-1] <= time:
                stack = stack[:-1]
            stack.append(time)

        return len(stack)