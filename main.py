import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def main():
    df = pd.DataFrame(pd.read_excel("covid.xlsx"))
    print(df)

    url = 'https://www.kanzencolor.shop/faq'
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    soup.findAll('a')
    line_count = 1
    for one_a_tag in soup.findAll('a')[1]:
        if line_count >= 36:
            link = one_a_tag['href']
            download_url = 'https://www.kanzencolor.shop/faq' + link
            urllib.request.urlretrieve(download_url, './' + link[link.find('/sizing') + 1:])
            time.sleep(1)
        line_count += 1


if __name__ == "__main__":
    main()
