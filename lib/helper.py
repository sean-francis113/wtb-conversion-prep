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
    if("/" in path):
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
    
def process_cmd(cmd_line, options):
    flip = True
    downscale = False
    delete_source = False
    source_path = ""
    dest_path = ""
    
    for cmd in cmd_line:
       if(cmd in options):
            if(cmd == options[0]): # Source Folder
                print(f"Setting Source Folder Path to {cmd_line[cmd_line.index(cmd) + 1]}")
                source_path = cmd_line[cmd_line.index(cmd) + 1]
            elif(cmd == options[1]): # Destination Folder
                print(f"Setting Destination Folder Path to {cmd_line[cmd_line.index(cmd) + 1]}")
                dest_path = cmd_line[cmd_line.index(cmd) + 1]
            elif(cmd == options[2]): # No Flip
                print(f"Setting Flip to False")
                flip = False
            elif(cmd == options[3]): # Downscale
                print(f"Setting Downscale to True")
                downscale = True
            elif(cmd == options[4]): # Delete Source
                print(f"Setting Delete Source to True")
                delete_source = True
                
    return source_path, dest_path, flip, downscale, delete_source