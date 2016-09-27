from Crawler import Crawler
from LinkFinder import LinkFinder

url = 'http://www.mediamarkt.nl'

queue = LinkFinder(url).find()
result = Crawler(queue).run()
result.seturl(url)

print "Done"

for key, value in result.all().iteritems():
    print 'Found %s %s times' % (key, value)


