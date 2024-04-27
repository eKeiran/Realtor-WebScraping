import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_realtor_data(base_url, location):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',  # Do Not Track request header
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers'
    }

    with requests.Session() as session:
        session.headers.update(headers)
        url = f"{base_url}/realestateandhomes-search/{location}"

        try:
            response = session.get(url)
            response.raise_for_status() 
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')

        data_list = []

        for listing in soup.find_all('div', class_='BasePropertyCard_propertyCard__nbKDx'):  
            title_element = listing.find('span', class_='BrokerTitle_titleText__Y8pb0')
            
            if title_element and title_element.get_text(strip=True):
                title = title_element.get_text(strip=True)
            else:
                title = "No Title"

            price_element = listing.find('div', class_='price-wrapper')
            if price_element:
                price = price_element.get_text(strip=True)
                price_parts = price.split('$')
                price = price_parts[0] + '$' + price_parts[1] if len(price_parts) > 2 else price
            else:
                price = "NA"

            url_element = listing.find('a', class_='LinkComponent_anchor__0C2xC')
            if url_element and url_element.has_attr('href'):
                url = url_element['href'].split('?')[0]
            else:
                url = "NA"


            data_list.append({
                "Title": title,
                "Price": price,
                "URL": url
            })

            time.sleep(1)

        df = pd.DataFrame(data_list)
        df.to_csv('realtor_data.csv', index=False)
        print("Data saved to realtor_data.csv")

base_url = 'https://www.realtor.com'
location = 'Los_Angeles_CA'  
scrape_realtor_data(base_url, location)