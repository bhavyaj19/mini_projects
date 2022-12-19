from bs4 import BeautifulSoup
import requests
url='https://www.flipkart.com/samsung-galaxy-s21-fe-5g-graphite-128-gb/p/itm7be0f72fff180?pid=MOBGBPFZSPRG8GSU&lid=LSTMOBGBPFZSPRG8GSUYZCRY0&marketplace=FLIPKART&q=samsung+s21+fe&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=c54a60e0-9013-4b82-a89d-b48f5ade691d.MOBGBPFZSPRG8GSU.SEARCH&ppt=hp&ppn=homepage&ssid=kblrfc2svk0000001663430881217&qH=d97019d05293176c'
result=requests.get(url)
doc=BeautifulSoup(result.text,'html.parser')

# prices=doc.find_all(text='sometext')
prices=doc.find_all("div",{"class":"_30jeq3 _16Jk6d"}) 

print(prices[0].string)
