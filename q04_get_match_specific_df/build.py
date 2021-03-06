# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    filter = ipl_df['match_code'] == match_code
    return ipl_df[filter]

get_match_specific_df(598057)
