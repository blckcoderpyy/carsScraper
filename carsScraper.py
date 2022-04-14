from bs4 import *
import requests
file=open("cars.txt","w",encoding="utf-8")
prices_ofCars=[]
for page in range(1,10):
    print("---------",page,"--------")
    url = str('https://www.cars.com/shopping/results/?page='+str(page)+'&page_size=20&list_price_max=&makes[]=volvo&maximum_distance=20&models[]=volvo-xc60&stock_type=cpo&zip=')
    rq=requests.get(url)
    print(url)
    soup=BeautifulSoup(rq.content,"html.parser")
    names=soup.find_all("h2",{"class":"title"})
    prices=soup.find_all("div",{"class":"price-section price-section-vehicle-card"})
    for price in prices:
       prices_ofCars.append(price.text)
    l=0
    for title in names:
        file.write(title.text+"\t"+prices_ofCars[l])
        l+=1