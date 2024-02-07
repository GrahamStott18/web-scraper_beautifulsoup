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


# Creates top_items as an empty list
top_items = []


# Extracts and stores in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        # strip() removes whitespace
        "title": title.strip(),
        "review": review_label.strip()
    }
    # append adds to the list
    top_items.append(info)


# Prints the result
print(top_items)