import CsvHelper
from Crawler import Crawler
from LinkFinder import LinkFinder

for url in CsvHelper.read_file('webshops.csv'):
    print("Processing: %s" % url)

    queue = LinkFinder(url).find()
    result = Crawler(queue).run()
    result.seturl(url)

    CsvHelper.write_results(result)

    print("Done")

    for key, value in result.all().items():
        print('Found %s %s times' % (key, value))
