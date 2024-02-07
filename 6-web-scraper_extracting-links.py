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


# Creates all_links as an empty list
all_links = []


# Extracts and stores in top_items according to instructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    # strip() removes whitespace
    text = text.strip() if text is not None else ''
    
    href = ahref.get('href')
    # strip() removes whitespace
    href = href.strip() if href is not None else ''
    # Append adds data to the all_links list
    all_links.append({"href": href, "text": text})


# Prints the result
print(all_links) 