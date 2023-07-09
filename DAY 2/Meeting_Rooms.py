import heapq
class Arrange_Meetings:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x[0]) # sorting on the basis of start time.

        rooms = []

        heapq.heappush(rooms, intervals[0][1])  # start time of the first meeting

        for interval in intervals[1:]:
            if interval[0] >= rooms[0]: # checking if start time of the current meeting is greater than or equal to the end time of the meeting at the top of the room(stack)
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])

        return(len(rooms))


time_intervals = [[3,19],[8,12],[11,30],[10,20],[2,7],[1,10]]

meetings = Arrange_Meetings()

print(meetings.minMeetingRooms(time_intervals))



'''
Time Complexity:

Sorting: The intervals are sorted based on their start time using the intervals.sort() method, which takes O(n log n) time complexity, where 'n' is the number of intervals.
Heap Operations: The code iterates through the intervals and performs heap operations. Heap operations such as heappush() and heappop() have a time complexity of O(log k), where 'k' is the number of elements in the heap. In the worst case, all intervals may need separate rooms, so the number of heap operations can be up to 'n'. Therefore, the overall time complexity of the heap operations is O(n log n).
Hence, the total time complexity of the code is O(n log n).

Space Complexity:

Sorting: The sorting operation does an in-place sort, so it does not require additional space. Therefore, the space complexity for sorting is O(1).
Heap: The code uses a heap, implemented as a list called 'rooms', to store the end times of the meetings. In the worst case, all intervals may need separate rooms, so the maximum number of elements in the heap can be 'n'. Hence, the space complexity for the heap is O(n).
Additional Variables: The code uses a few additional variables such as 'intervals', 'rooms', and 'interval' to store and manipulate data. The space required for these variables is insignificant compared to the input size, so we can consider it as O(1).
Therefore, the total space complexity of the code is O(n).

In summary, the time complexity of the code is O(n log n), and the space complexity is O(n).

'''
