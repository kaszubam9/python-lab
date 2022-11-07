#!/usr/bin/env python3
from pathlib import Path
import os
from pathlib import Path
from PIL import Image


def CountOfFiles():
    count = 0
    for root, dirs, files in os.walk('TestDir'):
        count += len(files)
    print(f'File count:{count}')

def DirectoryStructure():
    tab = ""
    for root, dirs, files in os.walk('TestDir'):
        print(tab, root)
        tab+="\t"
        if len(files):
            print(f"{tab}Files:")
            for f in files:
                print(f"{tab}  {f}")
        if len(dirs):
            print(f"{tab}Subdirectories:")
            for d in dirs:
                print(f"{tab}  {d}")

def ConvertToPng():
    image = Image.open(r'TestDir\kotki.jpg')
    image.save(r'TestDir\kotki.png')


if __name__ == '__main__':
    CountOfFiles()
    DirectoryStructure()
    ConvertToPng()