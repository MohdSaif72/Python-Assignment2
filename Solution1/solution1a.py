"""
A list of tuples which has the two consequtive days grouped together
"""
def grouped_days():
    """
    Returns a list of tuples containing consecutive pairs of days.
    """
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    list_days = []
    for x in range(len(days) - 1):
        list_days.append((days[x], days[x + 1]))
    return list_days

print(grouped_days())
