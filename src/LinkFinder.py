import Queue
import requests

from lxml import html

maxSize = 1000 # To prevent DDOS recognition


class LinkFinder:
    def __init__(self, base_url):
        self.base_url = base_url
        self.links = []
        self.links.append(base_url)

    def find(self):
        queue = Queue.Queue()

        index = 0
        for url in self.links:
            print 'Index %s of size %s' % (index, len(self.links))
            # print 'Scanning URL: %s' % url

            if len(self.links) > maxSize:
                break

            content = requests.get(url).content
            tree = html.fromstring(content)

            for link in tree.xpath('//a'):
                value = link.get('href')
                value = self.construct(value)

                if self.validate(value):
                    if value not in self.links:
                        self.links.append(value)
                        # print 'found: %s ' % value
            index += 1

        for url in self.links:
            queue.put(url)

        return queue

    def construct(self, url):
        if url is None:
            return ''
        elif url.startswith('http://'):
            return url
        else:
            if ('#' == url) | ('/' == url) | url.startswith('mailto:'):
                return url
            else:
                return self.base_url + '/' + url

    def validate(self, url):
        return url.startswith(self.base_url)
