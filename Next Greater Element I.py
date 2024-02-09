#Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for remaining_num in stack:
            next_greater[remaining_num] = -1

        result = [next_greater[num] for num in nums1]

        return result
		
		

#nums1 = [4, 1, 2]
#nums2 = [1, 3, 4, 2]
#Initialize an empty dictionary next_greater to store the next greater element for each element in nums2 and an empty stack.
#
#next_greater = {}
#stack = []
#
#Iterate through nums2 to find the next greater element for each element.
#
#For num = 1, the stack is empty, so we push 1 onto the stack.
#For num = 3, stack[-1] = 1, which is smaller than 3. Pop 1 from the stack and set next_greater[1] = 3. Push 3 onto the stack.
#For num = 4, stack[-1] = 3, which is smaller than 4. Pop 3 from the stack and set next_greater[3] = 4. Push 4 onto the stack.
#For num = 2, stack[-1] = 4, which is greater than 2. Push 2 onto the stack.
#At this point, the stack contains [4, 2], and next_greater contains {1: 3, 3: 4}.
#
#For any remaining elements in the stack, there is no next greater element. In this case, pop the remaining elements from the stack and set their corresponding values in next_greater to -1.
#
#Pop 2 from the stack and set next_greater[2] = -1.
#Pop 4 from the stack and set next_greater[4] = -1.
#The final next_greater is {1: 3, 2: -1, 3: 4, 4: -1}.
#
#Build the result array based on nums1. Iterate through nums1 and use the values from next_greater to create the result array.
#
#For num = 4, set result[0] = next_greater[4] = -1.
#For num = 1, set result[1] = next_greater[1] = 3.
#For num = 2, set result[2] = next_greater[2] = -1.
#The final result array is [-1, 3, -1]
		