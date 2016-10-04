import re

import requests
import threading

import CsvHelper


class Spider(threading.Thread):
    """"Class used for scanning urls on containing certain words."""

    def __init__(self, name, queue, result):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.result = result
        self.words = CsvHelper.read_file('words.csv')

    def run(self):
        """"Get an url from the queue, process the url and notify the queue the task on the retrieved item is done.
        Continue this process while the queue has items"""
        print("%s running" % self.name)

        while not self.queue.empty():
            url = self.queue.get()

            self.process(url)
            self.queue.task_done()

    def process(self, url):
        """Count for every word that needs to be checked the amount of times it's found in the page content.
        Add this result to the UrlResult as a key and value pair."""

        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        content = requests.get(url).text

        for word in self.words:
            count = len(re.findall(re.compile(word, re.IGNORECASE), content))
            self.result.put(word, count)
