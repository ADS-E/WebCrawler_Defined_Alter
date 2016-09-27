from Crawler import Crawler
from LinkFinder import LinkFinder

url = 'http://mediamarkt.com'

queue = LinkFinder(url).find()
Crawler(queue)

print "Done"
