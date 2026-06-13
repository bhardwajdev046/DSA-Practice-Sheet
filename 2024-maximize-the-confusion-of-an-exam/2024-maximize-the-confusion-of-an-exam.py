class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq=0
        left=0
        hash={}
        maxi=float('-inf')
        for right in range(len(answerKey)):
            hash[answerKey[right]]=hash.get(answerKey[right],0)+1
            max_freq= max(max_freq,hash[answerKey[right]])

            while (right-left+1)-max_freq > k:
                hash[answerKey[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi