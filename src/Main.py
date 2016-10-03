from CsvHelper import CsvHelper
from UrlResult import UrlResult

csvHelper = CsvHelper()
result = UrlResult("urlurl")
result.put("lelel", 5)
result.put("ziek", 8)
csvHelper.save(result)


# for url in csvHelper.read():
#    print("Processing: %s" % url)
#    print(sys.version)

# queue = LinkFinder(url).find()
# result = Crawler(queue).run()
# result.seturl(url)

#    result = UrlResult("urlurl")
#    result.put("lelel", 5)
#    result.put("ziek", 8)
#    csvHelper.save(result)

#    print("Done")

# for key, value in result.all().iteritems():
#    print('Found %s %s times' % (key, value))
