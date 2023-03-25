# NEF to JPG converter
# by xP9nda
# 25 March 2023

# Imports
import os
import rawpy
from PIL import Image

# Functions
def checkFolderExists(folder):
    # Check if the given folder exists
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("\n'{0}' folder created.\n".format(folder))

def convertNEF():
    filesConverted = 0
    
    # Get all content of the 'converting' folder
    convertingContent = os.listdir("converting")
    for file in convertingContent:
        # If the file is not an NEF file
        if not file[-4:].lower() == ".nef":
            print("'{0}' is not a .NEF file.".format(file))
            continue
        
        newFileName = file.strip(".nef") + ".jpg"
        convertingPath = "converting/"
        outputPath = "output/"
        
        # If a file with the same name exists already in the output folder
        if os.path.exists(outputPath + newFileName):
            print("A file with the name '{0}' already exists in the 'output' folder.".format(file))
            continue
        
        # Read the image file
        with rawpy.imread(convertingPath + file) as raw:
            # Convert the image to RGB data
            newImageRGB = raw.postprocess(use_camera_wb = True)
            
            # Save the image as JPG
            newImageArray = Image.fromarray(newImageRGB)
            newImageArray.save(outputPath + newFileName, quality = 100, optimize = True)
            print("'{0}' successfully converted and saved.".format(file))
            filesConverted += 1
    
    print("\nConverted {0} files.".format(filesConverted))

def main():
    checkFolderExists("converting")
    print("Please place all .NEF files into the 'converting' folder.")
    input("Press [ENTER] to convert all files when you are ready.")
    checkFolderExists("output")
    convertNEF() 
    input("Press [ENTER] to quit the program.")

# Code
if __name__ == "__main__":
    main()