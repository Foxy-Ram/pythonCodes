from bs4 import BeautifulSoup
import requests as req
import pprint

# Here the below website ( link ) is used for web scrape .
url = r'https://www.scrapethissite.com/pages/simple/'
page = req.get(url)
status = page.status_code
soup = BeautifulSoup(page.content, 'html.parser')

# _______countries_______
cn = soup.find_all('h3', class_='country-name')
cc = soup.find_all('span', class_='country-capital')
pop = soup.find_all('span',class_='country-population')
limit = 0
countries = []
countries_capital = []
population = []
for i, j, k in zip(cn, cc, pop):
    a = i.text.replace('\n', '')
    countries.append(" ".join(a.split()))
    countries_capital.append(j.text)
    population.append(k.text)
    if limit == 4:  # Change this value 4 for number of result.
        break
    limit += 1

pprint.pprint(countries)
pprint.pprint(countries_capital)
pprint.pprint(population)

