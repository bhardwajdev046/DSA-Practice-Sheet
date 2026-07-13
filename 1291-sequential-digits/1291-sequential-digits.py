class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit="123456789"
        ans=[]
        for length in range(len(str(low)),len(str(high))+1):
            for i in range(len(digit)-length+1):
                nums=int(digit[i:i+length])
                if nums>=low and nums<=high:
                    ans.append(nums)
        return ans