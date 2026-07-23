class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations)
        n=len(citations)
        left=0
        right=n-1
        ans=0
        while left<=right:
            mid=(left+right)//2
            if citations[mid]<(n-mid):
                left=mid+1
            elif citations[mid]>=(n-mid):
                ans=n-mid
                right=mid-1
        return ans