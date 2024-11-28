import requests
# pip install bs4
from bs4 import BeautifulSoup

# Set the url of the webpage you want to scrape
url = 'https://www.example.cl'

# Send an HTTP request to the URL and retrieve the HTML content
response = requests.get(url)

# Create a BeautifulSoup object that parses the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')

# Print the text and href attribute of each link
for link in links:
    print(link.get('href'), link.text)