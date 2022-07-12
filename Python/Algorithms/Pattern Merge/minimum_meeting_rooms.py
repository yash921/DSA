# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

# Example 1:

# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
# occur in any of the two rooms later.

def minimumMeetingRooms(meetings):
    meetings.sort(key=lambda x: x[0])

    rooms, start, end = 0, 0, 1
    





Meetings: [[1,4], [2,5], [7,9]]
print(minimumMeetingRooms(Meetings))