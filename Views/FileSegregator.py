import tkinter as tk
def segregate_files(files, insta_version):
    # Form the base path
    bas_path = "/instahms"

    # Add the test server version
    if insta_version == "12.4":
        bas_path += "1204/"
    else:
        bas_path += "/"

    # Make Testserver file path for each path
    file_paths = files.split(",")
    file_paths = [file_path.strip() for file_path in file_paths]
    file_paths = [file_path.replace("\n","") for file_path in file_paths]
    files_path_in_testserver = []

    for file in file_paths:
        file_path = bas_path
        if file.endswith(".class") or file.endswith(".sql") or file.endswith(".xml"):
            file_path += f"WEB-INF/{file[7:]}"   # each file path will start with "target/...."
        
        elif file.endswith(".jsp") or file.endswith(".js"):
            file_path += file[7:]
        
        else:
            print("Unrecognised file!")
        
        files_path_in_testserver.append(file_path)
    
    return files_path_in_testserver
