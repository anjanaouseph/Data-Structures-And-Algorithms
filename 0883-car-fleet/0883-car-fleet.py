class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)#sorts based on first element of each pair
        #to arrange from starting position to end position

        stack = []

        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]: #if the second car reaches faster that first car,
            #it means they collide
                stack.pop()
        return len(stack)
        