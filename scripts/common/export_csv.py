from check_version import is_next_version

def exportDataVersion(data, version):

    if is_next_version(version):
        file_name = "fullData_V" + version + ".csv"
        data.to_csv(file_name, index=False)
        print("File "+ file_name + " created")
    else: 
        print("Version not allowed")