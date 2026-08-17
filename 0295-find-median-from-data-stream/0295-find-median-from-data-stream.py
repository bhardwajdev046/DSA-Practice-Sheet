class MedianFinder:

    def __init__(self):
        self.max_leftheap=[]
        self.min_rightheap=[]

    def addNum(self, num: int) -> None:
        if len(self.max_leftheap) == 0 or num < -self.max_leftheap[0]:
            heapq.heappush(self.max_leftheap,-num)
        else:
            heapq.heappush(self.min_rightheap, num)

        if abs(len(self.max_leftheap) - len(self.min_rightheap)) > 1:
            temp = -heapq.heappop(self.max_leftheap)
            heapq.heappush(self.min_rightheap, temp)

        elif len(self.max_leftheap) < len(self.min_rightheap):
            temp1 = heapq.heappop(self.min_rightheap)
            heapq.heappush(self.max_leftheap, -temp1)

    def findMedian(self) -> float:
        if (len(self.max_leftheap) + len(self.min_rightheap))%2 != 0:
            return -self.max_leftheap[0]
        else:
            return (-self.max_leftheap[0] + self.min_rightheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()