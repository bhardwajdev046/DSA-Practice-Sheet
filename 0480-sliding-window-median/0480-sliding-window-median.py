class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # left=0
        # ans=[]
        # temp=nums[left:left+k]
        # temp.sort()
        # mid=k//2
        # if k%2!=0:
        #     ans.append(temp[mid])
        # else:
        #     ans.append((temp[mid-1]+temp[mid])/2)
        # for right in range(k,len(nums)):
        #     temp.remove(nums[left])
        #     temp.append(nums[right])
        #     left+=1
        #     temp.sort()
        #     mid=k//2
        #     if k%2!=0:
        #         ans.append(temp[mid])
        #     else:
        #         ans.append((temp[mid-1]+temp[mid])/2)
        # return ans


        ans = []
        max_leftheap = []      # max heap -> negative values
        min_rightheap = []     # min heap -> positive values
        delayed = {}
        left_size = 0
        right_size = 0

        # First window
        for i in range(k):
            if not max_leftheap or nums[i] <= -max_leftheap[0]:
                heapq.heappush(max_leftheap, -nums[i])
                left_size += 1
            else:
                heapq.heappush(min_rightheap, nums[i])
                right_size += 1

            # Balance
            if left_size - right_size > 1:
                x = -heapq.heappop(max_leftheap)
                heapq.heappush(min_rightheap, x)
                left_size -= 1
                right_size += 1

            elif right_size > left_size:
                x = heapq.heappop(min_rightheap)
                heapq.heappush(max_leftheap, -x)
                right_size -= 1
                left_size += 1

        # First median
        if k % 2:
            ans.append(float(-max_leftheap[0]))
        else:
            ans.append((-max_leftheap[0] + min_rightheap[0]) / 2)
        left = 0
        for right in range(k, len(nums)):
            old = nums[left]
            new = nums[right]

            # 1. Mark old as delayed
            delayed[old] = delayed.get(old, 0) + 1

            # old belongs to which heap?
            if old <= -max_leftheap[0]:
                left_size -= 1
            else:
                right_size -= 1

            # 2. Add new element
            if not max_leftheap or new <= -max_leftheap[0]:
                heapq.heappush(max_leftheap, -new)
                left_size += 1
            else:
                heapq.heappush(min_rightheap, new)
                right_size += 1

            # 3. Balance valid elements
            if left_size - right_size > 1:
                x = -heapq.heappop(max_leftheap)
                heapq.heappush(min_rightheap, x)
                left_size -= 1
                right_size += 1

            elif right_size > left_size:
                x = heapq.heappop(min_rightheap)
                heapq.heappush(max_leftheap, -x)
                right_size -= 1
                left_size += 1


            # 4. Remove delayed TOP
            while max_leftheap and -max_leftheap[0] in delayed:
                x = -heapq.heappop(max_leftheap)
                delayed[x] -= 1
                if delayed[x] == 0:
                    del delayed[x]


            while min_rightheap and min_rightheap[0] in delayed:
                x = heapq.heappop(min_rightheap)
                delayed[x] -= 1
                if delayed[x] == 0:
                    del delayed[x]

            # 5. Median
            if k % 2:
                ans.append(float(-max_leftheap[0]))
            else:
                ans.append((-max_leftheap[0] + min_rightheap[0]) / 2)
            left += 1
        return ans