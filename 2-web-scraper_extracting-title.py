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


# Extracts the title of web page
page_title = soup.title


# Prints the result
print(page_title)