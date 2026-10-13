class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []

        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        for p, s in cars:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
                
        return len(stack)
