import os
from .constants_common import DATA_PATH

def is_next_version(version_number):

    #Get list of files
    files = os.listdir(DATA_PATH)

    #Filter files that have the pattern
    versions = [
        int(f.split("_V")[-1].split(".csv")[0])
        for f in files
        if f.startswith("fullData_V") and f.endswith(".csv")
    ]

    #If there is no versions
    if not versions:
        next_version = 1

    else:
        #Find highest version and add one
        next_version = max(versions) + 1

    return version_number == next_version

