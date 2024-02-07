# Webscraping program to pull html data from designated webpage.

# Imports requests module from library.
# REQUESTS module give ability to send HTTP requests using python, this is to request the webpage.
# Documentation at (https://requests.readthedocs.io/en/latest/) 
import requests


# Requests the web page contents from the specified URL 
# Stores the result in res variable 
res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

# Stores data as variable txt
txt = res.text
# Stores status code as variable
status = res.status_code

# Prints the results
print(txt, status)