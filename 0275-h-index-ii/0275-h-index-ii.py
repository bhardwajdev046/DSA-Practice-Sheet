class Solution:
    # def helper(self,citations, papers):
    #     count=0
    #     for i in citations:
    #         if i>=papers:
    #             count+=1
    #     return count
    # def hIndex(self, citations: List[int]) -> int:
    #     low=1
    #     high=len(citations)

    #     while low<=high:
    #         papers=(low+high)//2
    #         count=self.helper(citations, papers)
    #         if count<papers:
    #             low=papers+1
    #         elif count>papers:
    #             high=papers-1
    #         else:
    #             return count
    #     return 0
    def hIndex(self, citations: List[int]) -> int:
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