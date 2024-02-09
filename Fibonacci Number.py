#Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        i = 0
        j = 1

        for p in range(n):
            i, j = j, i+j
        return i


# # 0 1 1 2 3 5 8 13 ...... ## n = 4
#   i j

#   i = 0 , j = 1
#   i = 1 , j = 1
#   i = 1 , j = 2
#   i = 2 , j = 3