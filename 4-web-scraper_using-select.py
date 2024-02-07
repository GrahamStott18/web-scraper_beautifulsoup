# Webscraping program to pull html data from designated webpage.

# Imports requests module from library.
# REQUESTS module give ability to send HTTP requests using python, this is to request the webpage.
# Documentation at (https://requests.readthedocs.io/en/latest/) 
import requests

# Imports bs4 from the BeautifulSoup library.
# BeautifulSoup module has features parse anything on the web you give it. 
# Documentation at (https://beautiful-soup-4.readthedocs.io/en/latest/) 
from bs4 import BeautifulSoup


# Requests the web page contents from the specified URL 
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# Parses the web page content, using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


# Creates empty list of all_h1_tags
all_h1_tags = []

# Sets all_h1_tags to all h1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Creates seventh_p_text and sets it to 7th p element text of the page
seventh_p_text = soup.select('p')[6].text


# Prints the result
print(all_h1_tags, seventh_p_text)