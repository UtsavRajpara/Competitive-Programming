# Question Link:- https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # ans will hold minimum number of operations required
        ans = 0
        for i in logs:
            # when we go up by one directory the operation will decrease by 1
            if i=="../":
                ans-=1
            # nothing to do we neither go one directory up or down
            elif i=='./':
                pass
            # we have gone down by one directory so required operations will increase
            else:
                ans+=1
            # ans<0 means we were in the main directory and we perform ../ which means nothing
            if ans<0:
                ans = 0
        if ans<0:
            return 0
        return ans
