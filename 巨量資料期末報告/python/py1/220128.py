import requests,re
import urllib.request as req
from bs4 import BeautifulSoup
url ="https://udn.com/news/index"
html= requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

route_code="body > main > div > section.main-index__focus > div.udn-tab > div:nth-child(2) > div > a:nth-child(1) > span.tab-link__title"
anss = soup.select(route_code)
#find(class_='page-product')
print(anss)

"""for ans in anss:
    try:
      print(ans)
      a=ans.text  
      

    except:
        pass
s="a"
print(type(s))"""