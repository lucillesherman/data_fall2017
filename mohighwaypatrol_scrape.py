import csv
import urllib2
from bs4 import BeautifulSoup

url = "https://www.mshp.dps.missouri.gov/HP68/search.jsp"

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'class': "accidentOutput"})

for tr in table.find_all('tr'):

	for td in tr.find_all('td'):
	
		print td.text

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./mohighwaypatrol.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
