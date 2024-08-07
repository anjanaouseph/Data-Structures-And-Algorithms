class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            #stack[-1] indicates top of the stack
            while stack and stack[-1][0] < temp:#if temp is greater that top of stack
               stack_temp, stack_index = stack.pop()
               result[stack_index] = index - stack_index
            stack.append((temp,index))

        return result  