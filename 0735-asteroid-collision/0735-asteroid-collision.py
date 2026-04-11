class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:#collision
                diff = stack[-1] + num #adding a positive and negative no

                if diff > 0:
                    num = 0
                if diff < 0:
                    stack.pop()
                if diff == 0:
                    stack.pop()
                    num = 0

            if num != 0:
                stack.append(num)

        return stack

# TC: O(N)
# SC: O(N)