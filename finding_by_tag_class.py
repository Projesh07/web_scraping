from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError

# url='http://shawarmatime.com/mmmmmmmmmm' ## This gives http error
# url='http://shawarmatime.commm/' ## This gives url error 

class FindTag:
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

	def check_tag(bs4,search_tag,search_class):
		try:
			tag=bs4.findAll(search_tag,{"class":search_class})
		except AttributeError as e:
			return None
		return tag

	connect=check_ok(url)

	if connect:

		tag=check_tag(connect,'div','item')
		if tag:
			for item in tag:
				print(item.get_text())
		else:
			print("tag not found")
	else:
		print("error in request")





	# bsobject=bs(html)

	# print(bsobject.img)
