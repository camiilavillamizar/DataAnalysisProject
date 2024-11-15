import os

def is_next_version(version_number):
    #Path
    data_path = "ruta/a/tu/directorio/data"  # Cambia esto a la ruta correcta

    #Get list of files
    files = os.listdir(data_path)

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

