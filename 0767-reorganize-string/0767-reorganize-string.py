class Solution:
    def reorganizeString(self, s: str) -> str:
        # char_freq = {}
        # for c in s:
        #     char_freq[c] = char_freq.get(c, 0) + 1
        
        # max_heap = [(-freq, char) for char, freq in char_freq.items()]
        # heapq.heapify(max_heap)

        # res = []
        # prev_freq, prev_char = 0, ""

        # while max_heap:
        #     freq, char = heapq.heappop(max_heap)
        #     res.append(char)

        #     if prev_freq < 0:
        #         heapq.heappush(max_heap, (prev_freq, prev_char))
            
        #     freq += 1
        #     prev_freq, prev_char = freq, char
        
        # if len(res) != len(s):
        #     return ""
        
        # return "".join(res)
        hash={}
        for ch in s:
            hash[ch]=hash.get(ch,0)+1
            
        maxi=max(hash.values())
        letter=max(hash,key=hash.get)

        res= [""]*len(s)
        if maxi>((len(s)+1)/2):
            return ""
        idx=0
        while(hash[letter]>0):
            res[idx]=letter
            idx+=2
            hash[letter]-=1
        
        for ch in hash:
            while hash[ch]>0:
                if idx>=len(s):
                    idx=1
                res[idx]=ch
                idx+=2
                hash[ch]-=1

        return "".join(res)