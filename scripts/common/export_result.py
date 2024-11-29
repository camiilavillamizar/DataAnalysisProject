import os
from .check_version import is_next_version
from .constants_common import RESULTS_PATH

def export_csv_result(data, name):

    file_name = name + ".csv"
    full_path = os.path.join(RESULTS_PATH, file_name)

    data.to_csv(full_path, index=False)
    print("File "+ file_name + " created in temp")
