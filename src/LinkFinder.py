import Queue

import requests
from lxml import html


class LinkFinder:
    def __init__(self, base_url):
        self.base_url = base_url

    def find(self):
        queue = Queue.Queue()

        content = requests.get(self.base_url).content
        tree = html.fromstring(content)

        for link in tree.xpath('//a'):
            url = link.get('href')
            url = self.construct(url)

            if self.validate(url):
                queue.put(url)
                print 'found: %s ' % url

        return queue

    def construct(self, url):
        if url.startswith('http://'):
            return url
        else:
            if ('#' == url) | ('/' == url) | url.startswith('mailto:'):
                return url
            else:
                return self.base_url + '/' + url

    def validate(self, url):
        return url.startswith(self.base_url)


