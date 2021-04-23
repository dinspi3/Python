import requests
from bs4 import BeautifulSoup

urls = 'https://www.simplilearn.com/tutorials/python-tutorial/python-automation-projects'
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