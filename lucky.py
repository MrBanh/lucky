#! python3
# lucky.py - Opens several google search results

import bs4
import requests as req
import sys
import webbrowser as wb

# Downloads the search result page from google
print('Googling...')
res = req.get(f'http://google.com/search?q={" ".join(sys.argv[1:])}')
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    wb.open(f'http://google.com{linkElems[i].get("href")}')
