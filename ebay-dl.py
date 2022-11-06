import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string

    >>>parse_itemssold('38 sold')
    38
    >>>parse_itemssold('14 watchers')
    0
    >>>parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_price(text):
    '''
    >>> parse_price('$520.99')
    52099
    >>> parse_price('$0.99 to $39.98')
    99
    >>> parse_price('Tap item to see current priceSee price')
    
    '''
    numbers = ''
    if text[0] == '$':
        for c in text:
            if c in '1234567890':
                numbers += c
            elif c == ' ':
                break
        return int(numbers)
    else:
        return None

def parse_shipping(text):
    '''
    >>> parse_shipping('Free shipping')
    0
    >>> parse_shipping('+$10.60 shipping')
    1060
    >>> parse_shipping('+$5.99 shipping')
    599
    '''
    numbers = ''
    if text[0] == '+':
        for c in text:
            if c in '1234567890':
                numbers += c
            elif c == ' ':
                break
        return int(numbers)
    else:
        return 0

# this if statement says only run code below when the python file is run "normally"
# where normally means not in the doctests
if __name__ == '__main__':

    # get command line argument
    parser = argparse.ArgumentParser(description ='Download information from ebay and convert to JSON')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default = 10)
    parser.add_argument('--csv', default = False) 
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # list of all items found in all ebay webpages 
    items = []

    # loop over the ebay webpages
    for page_number in range(1, int(args.num_pages) + 1):

        # build the URL
        url = 'https://www.ebay.com/sch/i/html?_from=R40&_nkw='
        url += args.search_term
        url += '&_sacat=0&LH_TitleDesc=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=', url)

        # download the html 
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text

        # process the html
        soup = BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items[1:]:
            
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            freereturns = False
            tags_freereturns = soup.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text) 
            
            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_price(tag.text)

            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping, .s-item__freeXDays')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)
            
            status = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text

            item = {
                'name': name,
                'free_returns': freereturns,
                'items_sold': items_sold,
                'price': price,
                'shipping': shipping,
                'status': status,
            }
            items.append(item)

    # write the json into a file

    if args.csv:
        f = csv.writer(open(args.search_term + '.csv', 'w'))
        f.writerow(['name', 'free_returns', 'items_sold', 'price', 'shipping', 'status'])
        for item in items:
            f.writerow([item['name'],
                        item['free_returns'],
                        item['items_sold'],
                        item["price"],
                        item["shipping"],
                        item["status"]])
    else:
        filename = args.search_term + '.json'
        with open(filename, 'w', encoding='ascii') as f:
            f.write(json.dumps(items))
        

#MAKE CSV FILE instead of JSON (note to self)
#python3 ebay-dl.py --num_pages=1 --csv=True 'stuffed animal'
#python3 ebay-dl.py --num_pages=1 'stuffed animal'
