import requests
import json
import bs4
import requests
from lxml import etree

USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
 
REQUEST_HEADER={
    'User-Agent': USER_AGENT,
    'Accept_language':'en-Us , en;q=0.5'
}
def get_html(link):
    return requests.get(link, headers=REQUEST_HEADER).content

def get_current_price(row):
    html = get_html(row)
    # scraping
    soup = bs4.BeautifulSoup(html, 'lxml')
    main_div = soup.find('span', attrs={'class': 'ud-sr-only'})
    
    if main_div is not None:
        titel = main_div.text.strip()
        print(titel)
    else:
        print("main_div not found for row: ", row)

if __name__ == "__main__":
    with open("udemy-sales/courses.json") as f:
        file = json.load(f)
    for row in file:
        course_title = list(file.get(row).keys())
        old_price = list(file.get(row).values())
        print(old_price, "\n")
        get_current_price(row)