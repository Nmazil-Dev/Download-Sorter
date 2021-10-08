import os

#Access the downloads folder at this path
path = 'C:/Users/ANDY/Downloads' #Change path to downloads folder
entries = os.listdir(path)
extensions = []

gpro = ["gp3", "gp4", "gp5", "gpx"]
images = ["JPG","jpg", "img", "PNG", "png"]

#Search files for their extensions for dir names
for entry in entries:
    extension_start = entry.rfind(".")
    if entry[extension_start:] not in extensions:
        extensions.append(entry[extension_start+1:])
for extension in extensions:
    if extension in gpro:
        mkdir_path = path + "/" + "Gpro"
    elif extension in images:
        mkdir_path = path + "/" + "Images"
    else:
        mkdir_path = path + "/" + extension
    try:
        os.mkdir(mkdir_path)
    except FileExistsError:
        pass

#Move files to their designated folder based on extension
for entry in entries:
    extension_start = entry.rfind(".")
    entry_extension = entry[extension_start+1:]
    if entry_extension in gpro:
        mkdir_path = path + "/" + "Gpro" + "/" + entry
    elif entry_extension in images:
        mkdir_path = path + "/" + "Images" + "/" + entry
    else:
        extension_index = extensions.index(entry_extension)
        mkdir_path = path + "/" + extensions[extension_index] + "/" + entry
    orig_path = path + "/" + entry
    try:
        print("Moved " + entry)
        os.rename(orig_path, mkdir_path)
    except PermissionError:
        pass