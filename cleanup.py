#!/usr/bin/python3

# create a commandline interface
import argparse
from os import listdir, walk, rename
from os.path import isfile, join, exists
import string

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)
parser.add_argument("dirpath")  # positional argument
parser.add_argument("-r", "--recursive", default=False, action="store_true") # optional argument
parser.add_argument("-c", "--clean", required=True)  # required argument
# parser.add_argument("-n", "--new-dir")  # optional argument
args = parser.parse_args()


def main():
    # print(args.dirpath, args.clean, args.recursive)
    
    # check if dirpath exists
    if exists(args.dirpath):
        clean_dir(args.dirpath, args.clean, args.recursive)
    
def clean_dir(dirpath: string, clean: string, recursive: bool):
    if recursive:
        for root, dirs, files in walk(dirpath, followlinks=True):
            for file in files:
                if clean in file:
                    print(file, clean in file)
                    try:
                        rename(join(root, file), join(root, file).replace(clean, ""))
                    except:
                        print("Could not rename", join(root, file))
            for dir in dirs:
                if clean in dir:
                    print(file, clean in file)
                    try:
                        rename(join(root, dirs), join(root, dirs).replace(clean, ""))
                    except:
                        print("Could not rename", join(root, dirs))
    else:
        for file in listdir(dirpath):
                print(file, clean in file)
                if clean in file:
                    try:
                        rename(join(dirpath, file), join(dirpath, file).replace(clean, ""))
                    except:
                        print("Could not rename", join(dirpath, file))
    
if __name__ == "__main__":
    main()
