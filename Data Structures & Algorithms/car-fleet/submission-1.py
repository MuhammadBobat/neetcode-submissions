class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        # if a car ahead has a LARGER time, then the car behind will join its fleet
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return(len(stack))

        

        