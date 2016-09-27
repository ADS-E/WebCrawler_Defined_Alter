import requests
import threading

words = ['winkelwagen', 'winkelmandje']


class ProcessingThread(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        print("%s running" % self.name)

        while not self.queue.empty():
            url = self.queue.get()

            self.process(url)
            self.queue.task_done()

            print('%s items left in queue' % self.queue.qsize())

    def process(self, url):
        content = requests.get(url).content

        for word in words:
            count = content.count(word)
            print("%s found %s %s times in %s" % (self.name, word, count, url))
