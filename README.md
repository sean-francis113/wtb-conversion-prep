# wtb-conversion-prep
## Requirements:

    * Latest Version of [Python](https://python.org)
    * Latest Version of [Pillow](https://pypi.org/project/pillow/#files) (Make Sure to Download the Correct File for your OS!)

A python program made to make preparing files for DDS-WTB Conversion easier made with modding Granblue Fantasy Relink in mind.

By default, it will do the following:

    * Find all .dds files in the Source Folder.
    * Flip them vertically to work with GBFR's system.
    * Package them into folders named "<filename>.wtb_extracted" in the Destination Folder.

However, there are some options you can specify:

-s : This indicates that the next argument is the Source Folder. For Instance, '-s modding/textures' means that the source folder is 'modding/textures'. This is ***NOT OPTIONAL***.

-d : This indicates that the next argument is the Destination Folder. For Instance, '-d modding/nier_cli' means that the source folder is 'modding/nier_cli'. This is ***NOT OPTIONAL***.

--noflip : Use this argument if you do not want the script to flip the textures before saving the file.

--downscale : Use this argument to automatically downscale the image. This will save the original upscaled and downscaled versions seperately into different folders (4k and 2k respectively)

--delsrc : Use this argument to delete the source file after saving it in the destination.

Example: python main.py -s modding/textures -d modding/nier_cli --downscale

The above example takes all the .dds files from modding/textures, flips them, downscales them, and saves them in modding/nier_cli. Because of the downscale, modding/nier_cli will have two additional folders: modding/nier_cli/4k and modding/nier_cli/2k.