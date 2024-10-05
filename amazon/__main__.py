from datetime import datetime
import requests
import csv
import bs4

#because every browser is different than the other
USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
 
REQUEST_HEADER={
    'User-Agent': USER_AGENT,
    'Accept_language':'en-Us , en;q=0.5'
}
def scraper(html):
    product = {}
    soup = bs4.BeautifulSoup(html, 'lxml')
    product["Title"] = get_title(soup).text.strip()
    product["Price"] = get_price(soup).text.strip()
    product["Ratings"] = get_rating(soup).text.strip()
    print(product)

def get_price(soup):
    return soup.find('span', attrs={'class':'a-price-whole'})

def get_title(soup):
    return soup.find('span', attrs={'id':"productTitle"})

def get_rating(soup):
    return soup.find('span', attrs={'class':"a-icon-alt"})

def get_page_html(url):
    response = requests.get(url=url,headers=REQUEST_HEADER)
    return response.content

if __name__ == "__main__":
    #reading from csv files 
    with open('amazon/amazon_products_urls.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            url = row[0]
            html = get_page_html(url)
            scraper(html)