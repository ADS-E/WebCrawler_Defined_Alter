import requests
import threading

words = ['winkelwagen', 'winkelmandje']


class Spider(threading.Thread):
    """"Class used for scanning urls on containing certain words."""

    def __init__(self, name, queue, result):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.result = result

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

        content = requests.get(url).content

        for word in words:
            count = content.count(word)
            self.result.put(word, count)
