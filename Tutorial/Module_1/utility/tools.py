import dateutil

from datetime import datetime

import numpy as np

def print_info_duration(str_start='2013-08-01 00:00:00', 
                        str_end='2013-08-31 23:59:59', 
                        str_format='%Y-%m-%d %H:%M:%S'):
    """Print out duration information based on start and end date

    Args:
        str_start (str, optional): Specifies the start date in string. Defaults to '2013-08-01 00:00:00'.
        str_end (str, optional): Specifies the end date in string. Defaults to '2013-08-31 23:59:59'.
        str_format (str, optional): Specifies the datetime format for start and end. Defaults to '%Y-%m-%d %H:%M:%S'.
    """
    start_ts = datetime.strptime(str_start, str_format)
    end_ts = datetime.strptime(str_end, str_format)
    print("Start      : {} ".format(start_ts))
    print("End        : {} ".format(end_ts))
    
    print("\nDuration/Delta")
    delta_in_days = end_ts - start_ts
    delta_in_years = dateutil.relativedelta.relativedelta(end_ts, start_ts).years
    print("Total of the recorded timespan is ~{:.2f} days or ~{} years".format(delta_in_days.total_seconds()/60/60/24, delta_in_years))
    
def print_total_energy(sr_of_total):
    """Print information of total energy consumption

    Args:
        sr_of_total (Series): Specifies the list of total energy series (e.g. active and apparent)
    """
    tot = len(sr_of_total)
    for idx in range(tot):
        tmplbl = sr_of_total.index[idx]
        tmpval = sr_of_total[idx]
        print("{} = {:.3f}".format(tmplbl, tmpval))
    if tot == 0:
        print("NO TOTAL ENERGY DATA...!")
    elif tot >1:
        print("Different = {:.3f}".format(sr_of_total[0] - sr_of_total[1]))

