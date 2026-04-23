class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash = {}
        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = []
            hash[nums[i]].append(i)
        res = [0] * n

        for key in hash:
            lst = hash[key]
            size = len(lst)

            prefix = [0] * (size + 1)
            for i in range(size):
                prefix[i + 1] = prefix[i] + lst[i]

            for i in range(size):
                index = lst[i]
                left = i * lst[i] - prefix[i]
                right = (prefix[size] - prefix[i + 1]) - (size - i - 1) * lst[i]
                res[index] = left + right

        return res
