from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

# url='http://shawarmatime.com/mmmmmmmmmm' ## This gives http error
# url='http://shawarmatime.commm/' ## This gives url error 

class ErrorHandle:
	
	url='http://shawarmatime.com/' #Working url


	def check_ok(url):

		try:
			html=urlopen(url)
		except HTTPError as e:
			return None
		except URLError as e:
			return None	
		else:
			bs4object=bs(html.read(),'html.parser')
		return bs4object

	def check_tag(bs4,ser):
		try:
			tag=bs4.find(ser)
			print(dir(tag))
			print(tag)
		except AttributeError as e:
			return None
		return tag

	connect=check_ok(url)

	if connect:

		tag=check_tag(connect,'img')
		if tag:
			print(tag)
		else:
			print("tag not found")
	else:
		print("error in request")





	# bsobject=bs(html)

	# print(bsobject.img)
