from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

# url='http://shawarmatime.com/mmmmmmmmmm' ## This gives http error
# url='http://shawarmatime.commm/' ## This gives url error 
url='http://shawarmatime.com/' #Working url


try:
	html=urlopen(url)
except HTTPError as e:
	print("HTTP error {}".format(e))
except URLError as e:
	print("URL error {}".format(e))	
else:

	print("It worked")
	

# bsobject=bs(html)

# print(bsobject.img)
