# this script prints out a list of article titles from the NY Times homepage
# I imagine that there is going to be some href/metadata work here but I really don't know

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text,features = "html.parser")

# gets everything that is between <h2> tags (which are titles)
titles = soup.find_all("span")

for title in titles:
	print(title.string)


