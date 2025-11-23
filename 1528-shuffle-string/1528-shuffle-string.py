class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li = [""] * len(indices)
        for i in range(len(indices)):
            li[indices[i]]=s[i]
        return "".join(li)