#Downloads the html available on the specified page
import urllib.request

import time

import cracker


def fetchpage(url):
	try:
		print("downloading page " + url)
		return str(urllib.request.urlopen(url).read())
		
		#The following is for testing purposes only
		#return """<a href="content/nextpage/example.test" class="navi navi-next" title="Next">Next</a>"""

	except urllib.error.URLError as e:
		print(e)
		return None
def fetchpageretry(url):
	for i in range (10):
		pagefeed = fetchpage(url)
		if pagefeed != None:
			return pagefeed
		else:
			print("Download failed on try %d, retrying" % i)
			time.sleep((i))
	return None 

def fetchcomic(comicdef, download_directory):
	""" 
	Precondition: 	comicdef is a list containing [name, startpage, nextregex, imgregex] 
			download_directory is a string 	
	"""
	#Sets the first page to be the start page
	current_page_url = comicdef[1]

	#As long as there is a next page to get, get that page
	while current_page_url != None:
		#get the current pages contents
		pagefeed = fetchpageretry(current_page_url)
		
		
		#find and download the image from said page
		img_url = cracker.findelement(pagefeed, comicdef[3])
		print("downloading image " + img_url)
		urllib.request.urlretrieve(img_url, download_directory + comicdef[0] + img_url.split("/")[-1])

		
		#fetch the next page
		current_page_url = cracker.findelement(pagefeed, comicdef[2])
	print("Finished downloading " + comicdef[0])

