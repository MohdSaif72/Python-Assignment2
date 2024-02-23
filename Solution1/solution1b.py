"""
A dictionary which has the name of the day as the key and value as a tuple with following values
"""
def dict_days():
    """
    Returns a dictionary containing information about each day.
    """
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    dict_info = {}
    for x in days:
        occurrence = days.index(x) + 1
        # occurrence = x + 1
        short = x[:3]
        lower = x.lower()
        upper = x.upper()
        length = len(x)

        dict_info[x] = (occurrence, short, lower, upper, length)
    return dict_info
print(dict_days())
