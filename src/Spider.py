import re
from lxml import etree
from nltk.stem.snowball import DutchStemmer

import requests
import threading
import lxml.html

import CsvHelper
from nltk.stem.snowball import DutchStemmer

class Spider(threading.Thread):
    """"Class used for scanning urls on containing certain words."""

    def __init__(self, name, queue, result):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.result = result
        self.words = CsvHelper.read_file('words.csv')
        self.stemmed_words = CsvHelper.read_file('stemmed-words.csv')

    def run(self):
        """"Get an url from the queue, process the url and notify the queue the task on the retrieved item is done.
        Continue this process while the queue has items"""
        print("%s running" % self.name)

        while not self.queue.empty():
            url = self.queue.get()

            self.process(url)
            self.queue.task_done()

    def process(self, url, stem = False):
        """Count for every word that needs to be checked the amount of times it's found in the page content.
        Add this result to the UrlResult as a key and value pair."""

        try:
            html = requests.get(url).text
            document = lxml.html.document_fromstring(html)

            if(stem):
                stemmer = DutchStemmer()
                content = "\n".join(stemmer.stem(etree.XPath("//text()")(document)))
                for word in self.stemmed_words:
                    count = len(re.findall(re.compile(word, re.IGNORECASE), content))
                    self.result.put(word, count)
            else:
                content = "\n".join(etree.XPath("//text()")(document))
                for word in self.words:
                    count = len(re.findall(re.compile(word, re.IGNORECASE), content))
                    self.result.put(word, count)

            word_count = len(content.split())
            self.result.set_word_count(word_count)
        except Exception as e:
            print(e)


