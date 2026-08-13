class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        # prefix=0
        # count=0
        # for ele in courses:
        #     if prefix+ele[0]<=ele[1]:
        #         prefix += ele[0]
        #         count += 1
        # return count
        heap=[]
        total=0
        for ele in courses:
            heapq.heappush(heap,-ele[0])
            total += ele[0]
            if total > ele[1]:
                x=-heapq.heappop(heap)
                total -= x
        return len(heap)


        