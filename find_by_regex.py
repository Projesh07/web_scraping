from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError
import re

	# url='http://shawarmatime.com/mmmmmmmmmm' ## This gives http error
	# url='http://shawarmatime.commm/' ## This gives url error 
	url='http://shawarmatime.com/' #Working url

class FindRegx:
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

	def check_tag(bs4,search_tag,search_class):
		try:
			tag=bs4.findAll(search_tag,{"class":search_class})
		except AttributeError as e:
			return None
		return tag

	connect=check_ok(url)

	if connect:

		tag=check_tag(connect,'div','images')
		regx=re.compile("\.jpg")

		if tag:
			for item in tag:
				for i in item.findAll('img',{'src':regx}):
					print(i['src'])
		else:
			print("tag not found")
	else:
		print("error in request")



		

# bsobject=bs(html)

# print(bsobject.img)
