class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    # 1) Build last-occurrence map manually
        last = {}
        for i in range(len(s)):
            last[s[i]] = i   # store last index of each character

        res = []
        i = 0
        n = len(s)

    # 2) Loop until we cover whole string
        while i < n:
            start = i
            end = last[s[i]]   # last index of starting character
            j = i + 1

        # 3) Expand window if needed
            while j <= end:
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1

        # 4) Save the size of this partition
            res.append(end - start + 1)

        # 5) Move to next partition
            i = end + 1

        return res
