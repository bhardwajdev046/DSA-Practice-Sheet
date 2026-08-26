class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # hash = {}
        # left = 0
        # ans=""
        # for right in range(len(s)):
        #     hash[s[right]] = hash.get(s[right],0)+1
        #     while hash.get('1',0)>k:
        #         hash[s[left]] = hash.get(s[left],0)-1
        #         if hash[s[left]] == 0:
        #             del hash[s[left]]
        #         left+=1                    
        #     if hash.get('1', 0) == k:
        #         # unnecessary starting zeros hatao
        #         while s[left] == '0':
        #             hash['0'] -= 1
        #             if hash['0'] == 0:
        #                 del hash['0']
        #             left += 1
        #         curr = s[left:right + 1]

        #         if (ans == "" or
        #             len(curr) < len(ans) or
        #             (len(curr) == len(ans) and curr < ans)):
        #             ans = curr

        # return ans

        count = 0
        left = 0
        ans = ""
        for right in range(len(s)):
            if s[right] == '1':
                count += 1
            while count > k:
                if s[left] == '1':
                    count -= 1
                left += 1
            if count == k:
                # remove useless leading zeros
                while s[left] == '0':
                    left += 1
                curr = s[left:right + 1]
                if ans == "" or len(curr) < len(ans) or \
                   (len(curr) == len(ans) and curr < ans):
                    ans = curr

        return ans
                