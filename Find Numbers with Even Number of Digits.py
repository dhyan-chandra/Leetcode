#Find Numbers with Even Number of Digits


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if(len(str(num)) % 2 == 0):
                res = res + 1
        return res

# return len([i for i in nums if len(str(i)) % 2 == 0])

# [12,345,2,6,7896]
# ["12","345","2","6","7896"]   --> map
# [2,3,1,1,4]                   --> map
# [2,4]               --> filter
# 2                   --> reduce