import os
import sys

def ensure_folder_path(path, remove_file=True):
    """Helper Function to Ensure Folder Path Provided is Valid.

    Args:
        path (str): The Folder Path to Ensure
        remove_file (bool, optional): If True, Removes the File at the End of the Path. Defaults to True.

    Returns:
        str: The New Ensured Folder Path
    """
    
    slash = "\\"
    if(not sys.platform == "win32" or not sys.platform == "win64"):
        path.replace("\\", "/")
        slash = "/"
        
    if(remove_file):
        if("." in path[-4 :]):
            path = path[: path.rfind(slash) + 1]
            
    if(path[-1] != slash):
        path = f"{path}{slash}"
        
    return path
        
def filter_files(file_list, ext):
    """Filters Out the Files in the List to Keep Only Those With the Provided File Extension.

    Args:
        file_list (list): The List of Files to Filter
        ext (str): The File Extension to Keep

    Returns:
        list: The Filtered List
    """
    
    final_list = []
    for file in file_list:
        if(ext in file):
            final_list.append(file)
            
    return final_list