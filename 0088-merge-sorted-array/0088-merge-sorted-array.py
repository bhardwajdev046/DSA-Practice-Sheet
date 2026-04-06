class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1
        t=m+n-1
        if m==0:
            nums1[p1]=nums2[p2]
        
        while p1>=0 and p2>=0:
            if nums1[p1]>=nums2[p2]:
                nums1[t]=nums1[p1]
                t-=1
                p1-=1
            else:
                nums1[t]=nums2[p2]
                t-=1
                p2-=1
        while p2 >= 0:
            nums1[t] = nums2[p2]
            p2 -= 1
            t -= 1