import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.imperial-library.info/content/doors-oblivion"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify()) 

main = soup.find('div', class_='entry-content clear')


for br in main.find_all('br'):
    br.replace_with('\n')

for quotes in main.find_all('’'):
    br.replace_with('"')


text = main.get_text(separator="\n\n")


text = "\n".join(line.rstrip() for line in text.splitlines() if line.strip() != "")

print(text)
"""
content = soup.find('div', class_='entry-content')

for br in content.find_all('br'):
    br.replace_with('\n')

parts = []
for p in content.find_all('p'):
    parts.append(p.get_text())

text = "\n\n".join(parts)

text = content.get_text()
print(text)

"""




with open("demofile.txt", "a", encoding="utf-8") as f:
    f.write(text)