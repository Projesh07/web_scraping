from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPerror
from urllib.error import URLerror

url='http://shawarmatime.com/'

try:
	html=urlopen(url)
except HTTPerror as e:
	print(e)
except URLerror as e:
	print(e)	
else:

	print("It worked")
	

# bsobject=bs(html)

# print(bsobject.img)
