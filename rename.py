# Rewritten on the 9th October
# Callum Todd, 2019

import os
from bs4 import BeautifulSoup
import requests

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# Get Folders
dir_path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(dir_path)
changes = []

# Remove script from files
for file in files:
    if file.endswith('.py'):
        files.remove(file)

for file in files:
    print(file)
    # print("Ready to continue?")

inp = input("Ready? (enter|n): ")
if inp == ("n"):
    print("Exiting..")
    exit()

# Main Loop
for folder in files:
    print("\nCurrent directory:  " + folder)
    print("Please enter the name of the artist and release (leave empty to skip) :")

    artist = input()
    if artist == '':
        continue
    release = input()


    url_prefix = "https://www.discogs.com/search/?q="
    url_postfix = "&type=all"
    url = url_prefix + artist.replace(" ", "+") + "+" + release.replace(" ", "+") + url_postfix
    try:
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        result = soup.find('a', {"class" : "search_result_title"})
        result_url = "https://www.discogs.com" + result['href']
        print(result_url)
        try:
            req = requests.get(result_url)
            soup = BeautifulSoup(req.content, features="html.parser")
            meta_label = soup.find("td", {"class": "label has_header"})
            meta_catno = soup.find("td", {"class": "catno has_header"})
            meta_year = soup.find("td", {"class": "year has_header"})
            meta_artist = soup.find("td", {"class": "artist"})
            meta_title = soup.find("td", {"class": "title"}).find_next('a')
            title = meta_title.text
            name = "[%s] %s - %s (%s)" % (meta_catno.text, meta_artist.text, title, meta_year.text)
            name = name.replace('/', '')
            print(name)
            inp = input("Is the name correct? (enter|n) :")
            if inp == 'n':
                continue
            print("Before:  " + dir_path + "/" + folder)
            print("After:   " + dir_path + '/' + name)
            changes.append(dir_path + '/' + name + '/')
            os.rename(dir_path + "/" + folder +'/', dir_path + '/' + name + '/')
        except:
            print("Release page could not be accessed.")
    except:
        print("Page could not be found. Did you spell the the title and artist correctly?")

print("\n Changes made:")
for change in changes:
    print(change)



