"""
We have a system that logs in multiple logs files the start and end time of different events.
combining the log files together, we want to find the combined pe4riod with the most overlappping events lets assume we have preprocessed the data to combine all event start/end times into an array and we have data like:
[[10, 12], [15, 18], [1,5], [2,6], [3,5]]
The result we want to find is [1,6] as [1,5] and [2,6] overlap and their combined range is [1,6], [3,5] overlaps [1,6].
"""

from typing import List, Any

events = [[10, 12], [15, 18], [1,5], [2,6], [3,5]]

def overlap(e1, e2) -> bool:
    if e1[1] >= e2[0]:
        return True
    return False


def getCombinedRange(events: List[Any]) -> List:
    if overlap(events[2], events[3]) is True:
        new = events[2] + events[3]
        res = [new[i] for i in (0, -1)]
        return res


print(getCombinedRange(events))
    