def conflictingAppointments(intervals):

    intervals.sort(key=lambda x: x[0])

    # [[1,4], [2,5], [7,9]]


    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] <= end:
            count += 1
        else:
            start = interval[0]
            end = interval[1]
    return True


Appointments = [[4,5], [2,3], [3,6]]
print(conflictingAppointments(Appointments))