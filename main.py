import sys
import os
import shutil

from PIL import Image, ImageOps

import lib.helper as help


def main():

    # MUST BE ORDERED: Source Folder, Destination Folder, No Flip, Downscale, Delete Source
    cmd_options = ["-s", "-d", "--noflip", "--downscale", "--delsrc"]

    help_str = """Command Arguments:

        -s : This indicates that the next argument is the Source Folder. For Instance, '-s modding/textures' means that the source folder is 'modding/textures'

        -d : This indicates that the next argument is the Destination Folder. For Instance, '-d modding/nier_cli' means that the source folder is 'modding/nier_cli'

        --noflip : Use this argument if you do not want the script to flip the textures before saving the file.

        --downscale : Use this argument to automatically downscale the image. This will save the original upscaled and downscaled versions seperately into different folders (4k and 2k respectively)

        --delsrc : Use this argument to delete the source file after saving it in the destination.

        Example: python main.py -s modding/textures -d modding/nier_cli --downscale

        The above example takes all the .dds files from modding/textures, flips them, downscales them, and saves them in modding/nier_cli. Because of the downscale, modding/nier_cli will have two additional folders: modding/nier_cli/4k and modding/nier_cli/2k."""

    # Will We Not Flip the Image on Copy?
    flip = True

    # Will We Downscale Images?
    downscale = False

    # Do We Delete the Source File?
    delete_source = False

    # Which File Extension Are We Working With?
    ext = ".dds"

    # Initializing Which Slash the Folder Path Uses
    slash = "\\"

    # Grab Command Arguments
    args = sys.argv[1:]
    arg_len = len(args)

    # If There Are No Arguments
    if (arg_len < 1):
        sys.exit(
            "You Must Include Commands. Use --help for the list of Command Arguments.")

    if ("--help" in args):
        sys.exit(help_str)

    dest_path = ""
    source_path = ""

    # Process Command Arguments
    source_path, dest_path, flip, downscale, delete_source = help.process_cmd(
        args, cmd_options)

    # If There Are No Folder Path Arguments
    if (dest_path == "" or source_path == ""):
        sys.exit("The Commandline Must Include a Source and Destination Path. Use --help for the list of Command Arguments.")

    # Ensure Folder Paths Are Valid for OS
    source_path = help.ensure_folder_path(source_path)
    dest_path = help.ensure_folder_path(dest_path)

    # Exit if Source Folder Does Not Exist
    if (not os.path.exists(source_path)):
        sys.exit("The Source Folder Path is Not Valid! Make Sure the Folder Path is Spelled Correctly. Use --help for the list of Command Arguments.")

    # Create Destination if Needed
    if (not os.path.exists(dest_path)):
        print(f"Creating Destination Folder")
        os.makedirs(dest_path)

    # Get Correct Folderpath Slash for Future Use
    if ("/" in source_path):
        source_path.replace("\\", "/")
        slash="/"

    # Grab All Files and Filter List By Extension
    file_list=os.listdir(source_path)
    file_list=help.filter_files(file_list, ext)
    
    print(f"Found {len(file_list)} \'{ext}\' Files in {source_path}")

    # Work on Each Filtered File
    for file in file_list:
        filename=file.replace(ext, "")
        file_path=f"{source_path}{file}"
        wtb_dir=f"{dest_path}{filename}.wtb_extracted"

        wtb_4k_dir=f"{dest_path}4k{slash}{filename}.wtb_extracted"
        wtb_2k_dir=f"{dest_path}2k{slash}{filename}.wtb_extracted"

        print(f"Working on {file}...")

        # Create New WTB Folder if Needed
        if (not os.path.exists(wtb_dir)):
            print(f"\tCreating Folder: {wtb_dir}")
            os.makedirs(wtb_dir)

        # Remove Any Files Already in WTB Folder
        print(f"\tSearching {wtb_dir} For Files")
        wtb_file_list=os.listdir(wtb_dir)
        print(f"\tFound {len(wtb_file_list)} Files")
        if (len(wtb_file_list) > 0):
            for wtb_file in wtb_file_list:
                print(f"\tRemoving {wtb_file}")
                os.remove(f"{wtb_dir}{slash}{wtb_file}")

        # Initialize Image Variables for Editting if Needed
        img=None
        downscaled_img=None

        if (flip):
            print(f"\tFlipping {file}")
            img=Image.open(f"{file_path}")
            img=ImageOps.flip(img)

        if (downscale):
            if (img is None):
                img=Image.open(f"{file_path}")

            print(f"\tDownscaling {file}")
            downscaled_img=img.resize((int(img.width / 2), int(img.height / 2)))

        if (not img is None):
            if (downscale):
                print(
                    f"\tSaving Upscale and Downscale {file} to the Folders:\n\t\t{wtb_4k_dir}\n\t\t{wtb_2k_dir}")

                # Create New 4k WTB Folder if Needed
                if (not os.path.exists(wtb_4k_dir)):
                    print(f"\tCreating Folder: {wtb_4k_dir}")
                    os.makedirs(wtb_4k_dir)

                # Create New 2k WTB Folder if Needed
                if (not os.path.exists(wtb_2k_dir)):
                    print(f"\tCreating Folder: {wtb_2k_dir}")
                    os.makedirs(wtb_2k_dir)

                img.save(f"{wtb_4k_dir}{slash}{file}")
                downscaled_img.save(f"{wtb_2k_dir}{slash}{file}")
            else:
                print(f"\tSaving Flipped {file} to {wtb_dir}")
                img.save(f"{wtb_dir}{slash}{file}")

            if (delete_source):
                print(f"\tDeleting Source File")
                os.remove(file_path)
        else:
            if (not delete_source):
                print(f"\tCopying {file} to {wtb_dir}")
                shutil.copy2(file_path, wtb_dir)
            else:
                print(f"\tMoving {file} to {wtb_dir}")
                shutil.move(file_path, wtb_dir)

    sys.exit("Done!")

main()
