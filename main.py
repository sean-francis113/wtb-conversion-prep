import sys
import os
import shutil

import lib.helper as help

def main():
    args = sys.argv[1:]
    arg_len = len(args)
    
    ext = ".dds"
    slash = "\\"
    
    if(not sys.platform == "win32" or not sys.platform == "win64"):
        slash = "/"
    
    if(arg_len <= 1):
        sys.exit("The Command Must Be Formatted With a Destination and Source Folder.\nFor Instance: \"python main.py <path to nier_cli> <path to dds files>\"")
        
    if(not os.path.exists(args[0]) or not os.path.exists(args[1])):
        sys.exit("The Destination or Source Folder Path is Not Valid!")
        
    dest_path = help.ensure_folder_path(args[0])
    source_path = help.ensure_folder_path(args[1])
    
    file_list = os.listdir(source_path)
    file_list = help.filter_files(file_list, ext)
    
    for file in file_list:
        filename = file.replace(ext, "")
        file_path = f"{source_path}{file}"
        wtb_dir = f"{dest_path}{filename}.wtb_extracted"
        
        print(f"Copying {file} to {wtb_dir}")
        
        if(not os.path.exists(wtb_dir)):
            os.mkdir(wtb_dir)
        
        wtb_file_list = os.listdir(wtb_dir)
        if(len(wtb_file_list) > 0):
            for wtb_file in wtb_file_list:
                os.remove(f"{wtb_dir}{slash}{wtb_file}")
        
        shutil.copy2(file_path, wtb_dir)
        
    sys.exit("Done!")
    
main()