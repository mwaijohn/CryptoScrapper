import requests
from bs4 import BeautifulSoup

r = requests.get("https://litecoin.com/")
r_bitcoin = requests.get("https://www.coingecko.com/en")
r_etherum = requests.get("https://ethereumprice.org/")
r_ripple = requests.get("https://coinranking.com/coin/ripple-xrp")
#print(r.content)

soup = BeautifulSoup(r.content)
soup_bitcoin = BeautifulSoup(r_bitcoin.content)
soup_etherum = BeautifulSoup(r_etherum.content)
soup_ripple = BeautifulSoup(r_ripple.content)
price_list = []

#get prices
get_data = soup.find_all("div",{"class":"price"})
get_bitcoin_price = soup_bitcoin.find("span",{"data-price-btc":"1.0"})
get_eth_price = soup_etherum.find("span",{"id":"ep-price"})
get_ripple_price = soup_ripple.find("span",{"class":"coin-page__price-number"})

#print prices
for item in get_data:
    litcoin_price = item.text.strip('$\r\n\t\t\t\t\t\t')
    print(litcoin_price + " litcoin")

print(get_bitcoin_price.text.strip(",\n$\n").replace(",","") + " bitcoin")
print(get_eth_price.text + " etherum")
#print(get_ripple_price.text + " xrp")

