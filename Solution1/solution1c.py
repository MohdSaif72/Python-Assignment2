"""
provides different types of containers
"""
import collections

def occur_char():
    """
    tuple with all the characters and their number of occurences in each name of the day
    """
    result = []
    for day in days:
        count_dict = collections.Counter(c.lower() for c in day)
        char = (day, dict(count_dict.most_common(26)))
        result.append(char)
    return  tuple(result)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(occur_char())
