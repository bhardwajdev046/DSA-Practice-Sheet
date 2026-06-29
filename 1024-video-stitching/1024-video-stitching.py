class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x:x[0])
        n=len(clips)
        count = 0
        i = 0
        current_end = 0
        farthest = 0

        while current_end < time:

            for i in range(n):
                if clips[i][0] <= current_end:
                    farthest = max(farthest, clips[i][1])
                    i += 1

            if farthest == current_end:
                return -1

            count += 1
            current_end = farthest

        return count
                