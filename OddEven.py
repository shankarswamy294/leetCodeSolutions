from itertools import product

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        import math
        ans = [0]*num_people
        turn = int((-1 + math.sqrt(1+8*candies))//(2*num_people))
        remaining = candies - ((turn*num_people) * (turn*num_people) + (turn*num_people)+1)//2
        print(turn)
        for ind in range(num_people):
            old_val= ((2*(ind+1))+(turn-1)*num_people)*turn
            print(old_val)
            ans[ind] += int(old_val//2)
            c_val = (ind + 1) + (turn*num_people)

            if remaining and remaining-c_val>0:
                ans[ind]+=c_val
                remaining-=c_val
            else:
                ans[ind]+=remaining
                remaining = 0

        print(ans)

x=Solution()
x.distributeCandies(90,4)