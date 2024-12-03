import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce site
url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

# Send a GET request to the website
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the product listings
products = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')

# Open a CSV file to write the data
with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Rating'])

    # Loop through the products and extract the necessary information
    for product in products:
        # Extract product name
        product_name = product.find('a', class_='title').text.strip()

        # Extract product price
        product_price = product.find('h4', class_='price').text.strip()

        # Extract product rating
        product_rating = product.find('div', class_='ratings').find('p', class_='pull-right').text.strip()

        # Write the product data to the CSV file
        writer.writerow([product_name, product_price, product_rating])

print("Data has been written to products.csv")