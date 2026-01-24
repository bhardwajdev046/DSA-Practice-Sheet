class Solution:
    def solve(self,idx,nums,ds,res):
        res.append(ds.copy())
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            self.solve(i+1,nums,ds,res)
            ds.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # def solve(num1, num2):
        #     if len(num2) == 0:
        #         return [tuple(sorted(num1))]  # store as tuple for set use later

        #     digit = num2[0]
        #     pick = solve(num1 + [digit], num2[1:])
        #     notpick = solve(num1, num2[1:])
        #     return pick + notpick

        # nums.sort()
        # result = solve([], nums)
        # # use set to remove duplicates, then convert back to list of lists
        # unique_result = [list(x) for x in set(result)]
        # return unique_result
        nums.sort()
        res=[]
        ds=[]
        self.solve(0,nums,ds,res)
        return res


