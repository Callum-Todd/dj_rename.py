import os
import sys
import webbrowser

# Setup Definition
def Setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    Total = len(DirArray)
    print("~~~~ Music Folder File Renamer ~~~~")
    print("There are (%d) releases to be processed" % Total)
    raw_input("Press Enter to continue...\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("~~~~ Music Folder File Renamer ~~~~")

# Process Definition - for each folder in root directory
def ProcessFolder(current):
    print(DirArray[current])
    Skip = raw_input("Skip? y/enter: ")
    if Skip == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~ Music Folder File Renamer ~~~~")
        return
    else:
        Artist = raw_input("Please enter the name of this Artist.\n")
        Release = raw_input("Please enter the name of this Release.\n")
        TempName = Artist + Release
        print("Please use the search link below to Catalog ID of Vinyl Release.")
        UrlTemp = "http://www.discogs.com/search/?q=" + Artist.replace(" ", "+") + "+" + Release.replace(" ", "+")
        print(UrlTemp)
        webbrowser.open(UrlTemp, new=2, autoraise=True)
        CATID = raw_input("Please enter Catalog ID for Vinyl Release.\n")
        Date = raw_input("Enter the year of release.\n")
        NewName = "[" + CATID + "] " + Artist + " - " + Release + " (" + Date + ")"
        os.rename(DirArray[current], NewName)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~ Music Folder File Renamer ~~~~")

DirArray = os.listdir(os.getcwd())
DirArray.remove(sys.argv[0])
Setup()

for index, item in enumerate(DirArray):
    ProcessFolder(index)

print("All new releases have been processed, exiting now...\n")
sys.exit()
