#https://www.geeksforgeeks.org/how-to-write-the-output-to-html-file-with-python-beautifulsoup/
import requests
from bs4 import BeautifulSoup

urls = 'https://www.discountbank.co.il/DB/private'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("test23.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")

f.close()