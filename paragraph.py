import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/').read()

soup = bs.BeautifulSoup(source,'lxml')

#print(soup.text)

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

f = open("text111.txt", "w")
f.write('%s\n' % paragraph)
f.close()

