import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize


# Set the startingpoint for the spider and initialize 
# the a mechanize browser object
url = "http://www.gpeasynet.com/"
br = mechanize.Browser()

# create lists for the urls in que and visited urls
urls = [url]
visited = [url]


# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
while len(urls)>0:

    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url)
            # print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                # print newurl
    except:
        print "error"
        urls.pop(0)
       
# print visited


for url in visited:
    print url