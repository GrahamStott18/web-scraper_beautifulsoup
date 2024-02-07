# Webscraping program to pull html data from designated webpag and creating .CSV file with extracted data.

# Imports requests module from library.
# REQUESTS module give ability to send HTTP requests using python, this is to request the webpage.
# Documentation at (https://requests.readthedocs.io/en/latest/) 
import requests

# Imports bs4 from the BeautifulSoup library.
# BeautifulSoup module has features parse anything on the web you give it. 
# Documentation at (https://beautiful-soup-4.readthedocs.io/en/latest/) 
from bs4 import BeautifulSoup

# Imports csv module
import csv


# Requests the web page contents from the specified URL 
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# Parses the web page content, using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


# Creates all_products as an empty list
all_products = []


# Extracts and stores in all_products according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    # .strip() removes whitespace from scrapped data 
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')
    
    # Adds extracted data to all_products list 
    all_products.append({
        "name": name, 
        "description": description,
        "price": price,
        "reviews": reviews, 
        "image": image
    })
    

keys = all_products[0].keys()

# Creates .CSV file, and will save into the same directory as this file. 
with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)