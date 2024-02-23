"""
pandas helps in working with data sets and analyzing the data 
"""
import pandas as pd
from Solution1 import solution1a
from Solution1 import solution1b
from Solution1 import solution1c

def export_to_excel(data, filename):
    """
    function creates a pandas DataFrame and 
    then exports data into Excel file with the given filename.
    """
    df = pd.DataFrame(data)
    df.to_excel(filename+'.xlsx', index=False)

export_to_excel(solution1a.grouped_days(), 'consecutivedays')
export_to_excel(solution1b.dict_days().values(), 'InformationDay')
export_to_excel(solution1c.occur_char(), 'OccurChar')
