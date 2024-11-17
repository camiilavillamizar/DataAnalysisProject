import os
from .check_version import is_next_version
from .constants_common import DATA_PATH

def exportDataVersion(data, version):

    if is_next_version(version):
        file_name = "fullData_V" + str(version) + ".csv"
        full_path = os.path.join(DATA_PATH, file_name)

        data.to_csv(full_path, index=False)
        print("File "+ file_name + " created")
    else: 
        print("Version not allowed")