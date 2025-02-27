import os
import sys
import time
import webbrowser
from urllib import urlopen
from bs4 import BeautifulSoup
Total = 0

# Setup / Welcome function definition
def Setup():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("~~~~ Music Folder File Renamer ~~~~")
    print("There are (%d) releases to be processed" % Total)
    input("Press Enter to continue...\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("~~~~ Music Folder File Renamer ~~~~")

# Process function definition - for each folder in root directory
def ProcessFolder():
    print(DirArray[i])
    Skip = input("Skip release? Yes: Anykey + Enter | No: Enter")

    if Skip:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~ Music Folder File Renamer ~~~~")
        return
    else:
        Artist = input("Please enter the name of this Artist.\n")   #Initial user input of artist and release name
        Release = input("Please enter the name of this Release.\n") #from displayed directory name.

        #Creates a discogs search URL for the release, opens the webpage and parses its contents using BeautifulSoup
        SearchUrl = "http://www.discogs.com/search/?q=" + Artist.replace(" ", "+") + "+" + Release.replace(" ", "+")
        SearchPage = urlopen(SearchUrl)
        soup = BeautifulSoup(SearchPage, 'html.parser')
        result = soup.find("a", {"class": "search_result_title"}).attrs["href"] #Obtains href attribute of the search result

        #Creates the actual release URL, opens the webpage and parses its contents using BeautifulSoup
        ResultUrl = "http://www.discogs.com" + result
        ResultPage = urlopen(ResultUrl)
        soup2 = BeautifulSoup(ResultPage, "html.parser")

        #Use of <td> HTML tags on the webpage to access information about the release
        meta_label = soup2.find("td", {"class": "label has_header"})
        meta_catno = soup2.find("td", {"class": "catno has_header"})
        meta_year = soup2.find("td", {"class": "year has_header"})
        label = meta_label.get_text()
        catno = meta_catno.get_text()
        year = meta_year.get_text()

        #Creates the new directory name
        NewName = "[" + catno + "] " + Artist + " - " + Release + " (" + year + ")"
        print(NewName)
        time.sleep(1)
        os.rename(DirArray[i], NewName)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~ Music Folder File Renamer ~~~~")

# Main Execution
DirArray = os.listdir(os.getcwd())
Total = len(DirArray)
Setup()
# DirArray.remove("rename3")
i = 0
while i < Total:
    ProcessFolder()
    i += 1
# del DirArray[0]

# for index, item in enumerate(DirArray):
#     ProcessFolder(index)
# for value in DirArray:
#     ProcessFolder(value)

print("All new releases have been processed, exiting now...\n")
sys.exit()
