# Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().
#
# Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called while testing.


# Example 1:
#
# Input: n = 1
# Output: [2]
# Example 2:
#
# Input: n = 2
# Output: [2,8]
# Example 3:
#
# Input: n = 3
# Output: [3,8,10]

class Solution:
    def __init__(self):
        self.hash = [1] * 7
        self.count = 0
        self.rn = 8

    def rand10(self):
        self.count += 1
        if self.count == 10:
            self.hash = [1] * 7
            self.rn = 8
            self.count = 0
        num = rand7()
        if self.hash[num - 1] == 0 and self.rn == 11:
            while True:
                num = rand7()
                if self.hash[num - 1]:
                    self.hash[num - 1] = 0
                    return num
        elif self.hash[num - 1] == 0 and self.rn != 11:
            r = self.rn
            self.rn += 1
            return r
        else:
            self.hash[num - 1] = 0
            return num
