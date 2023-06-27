import heapq
class ArrangeMeetings:
    def minMeetingRooms(self,intervals):
        # if not intervals:
        #     return 0
        intervals.sort(key = lambda x : x[0])
        rooms = []

        heapq.heappush(rooms, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval[1])
        
        return len(rooms)
    


time_intervals = [[3,19],[8,12],[11,30],[10,20],[2,7],[1,10]]
meetings = ArrangeMeetings()

print(meetings.minMeetingRooms(time_intervals))
