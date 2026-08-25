import requests
import csv
from bs4 import BeautifulSoup

def getcontent(url):

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

    with open("demofile.txt", "a", encoding="utf-8") as f:
        f.write(text)

def getcontent_cycle(baseurl):
    response = requests.get(baseurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify()) 
    
    main = soup.find_all('a', class_='title')

    for link in main:
        getcontent(link["href"])
    


getcontent_cycle("https://www.imperial-library.info/game-books/tes5-skyrim-books")