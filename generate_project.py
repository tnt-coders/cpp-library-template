import fileinput, os, re

# Replaces keywords in the provided string
def replace_keywords(text):
    text = text.replace("@NAME@", name.upper())
    text = text.replace("@Name@", name[0].upper() + name[1:])
    text = text.replace("@name@", name.lower())
    text = text.replace("@description@", description)
    return text

# Copies a template file and replaces keywords within the file
def copy_template_file(source, destination):
    file = open(source, "r")
    contents = file.read()
    dest_contents = replace_keywords(contents)

    destination = open(destination, "w")
    destination.write(dest_contents)
    return

# Get the name and description of the project
name = input("Name: ")
description = input("Description: ")

# Create the root directory
root = "cpp-" + name
os.makedirs(root)

# Generate project files
print("Generating project files...")
for subdir, dirs, files in os.walk("template"):
    dest_subdir = subdir.replace("template", "")
    dest_subdir = replace_keywords(dest_subdir)

    # Process directories
    for dir in dirs:
        dest_dir = replace_keywords(dir)
        print(root + dest_subdir + os.sep + dest_dir)
        os.makedirs(root + dest_subdir + os.sep + dest_dir)

    # Process files
    for file in files:
        dest_file = replace_keywords(file)
        print(root + dest_subdir + os.sep + dest_file)
        copy_template_file(subdir + os.sep + file, root + dest_subdir + os.sep + dest_file)