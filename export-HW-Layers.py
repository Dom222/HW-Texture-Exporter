#!/usr/bin/env python

from gimpfu import *
from os.path import join

def export_HW_Layers(image, __unused_drawable, directory, name_pattern, include_underscore):
    suffixes = [
        "_DIFF",
        "_SPEC",
        "_GLOW",
        "_NORM",
        "_TEAM",
        "_STRP",
        "_PAIN",
        "_REFL",
        "_PROG", # Ore
        "_DIFX", # Thruster
        "_SPEX", # Thruster
        "_GLOX", # Thruster
        "_REFX", # Thruster
        "_WARP", # Planet
        "_CLD1", # Planet
        "_CLD2", # Planet
        "_CLD3", # Planet
        "_PROG", # Cosmic
        "_NOIZ"  # Dustvein
    ]
    for layer in image.layers:
        for i in suffixes:
            if i in layer.name:
                if include_underscore:
                    if ".tga" in layer.name or ".TGA" in layer.name:
                        filename = directory + "\\" + name_pattern + "_" + layer.name #join(directory, name_pattern % layer.name)
                        raw_filename = name_pattern + "_" + layer.name
                    else:
                        filename = directory + "\\" + name_pattern + "_" + layer.name + ".tga" #join(directory, name_pattern % layer.name)
                        raw_filename = name_pattern + "_" + layer.name + ".tga"
                else:
                    if ".tga" in layer.name or ".TGA" in layer.name:
                        filename = directory + "\\" + name_pattern + layer.name #join(directory, name_pattern % layer.name)
                        raw_filename = name_pattern + layer.name
                    else:
                        filename = directory + "\\" + name_pattern + layer.name + ".tga" #join(directory, name_pattern % layer.name)
                        raw_filename = name_pattern + layer.name + ".tga"
                rle = 0
                origin = 0
                pdb.file_tga_save(image, layer, filename, raw_filename, rle, origin)

register(
    "python_fu_export_HW_Layers",
    "Save all layers into separate files",
    "Save all layers into separate files",
    "Xercodo & Dom2",
    "Xercodo & Dom2",
    "2015",
    "<Image>/File/Export HW Maps...",
    "*",
    [
        (PF_DIRNAME, "directory", "Directory to put the images in", "/"),
        (PF_STRING, "name_pattern", "Base file name. Output will be name__layer.tga", ""),
        (PF_BOOL, "include_underscore", "If the export should include an underscore in front of each layer.", 1),
    ],
    [],
    export_HW_Layers
)

main()
