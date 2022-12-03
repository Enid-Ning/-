
from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service

s=Service(r"C:\Users\enidl\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)


url = input('請輸入網址')

driver.get(url)
html=driver.page_source
#print(html)
soup=bs(html,'html.parser')

datas= soup.select('#Wmian > div.Wcontain > div.Wtitile')
for data in datas:
    name=data.text.split()

datas = soup.select('#Wmian > div.Wcontain > div.Wline.price-row.s2016-wd-cnt > span.Wvalue.Wprice')
for data in datas:
    price=data.text.split()

datas= soup.select('#Wmian > div.Wleft > div > img')
for data in datas:
    pic=data['src']

print('name: '+str(name))
print('prices: '+str(price))
print('picture: '+str(pic))
driver.quit
