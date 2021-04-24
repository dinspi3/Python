# https://www.geeksforgeeks.org/how-to-scrape-paragraphs-using-python/?ref=rp
# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup


# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://www.discountbank.co.il/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    print(data.get_text())

f = open("text111.txt", "w")
f.write('%s\n' % data)
f.close()
