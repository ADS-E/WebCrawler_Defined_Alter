import multiprocessing

from Processor import ProcessingThread

threads = []


class Crawler:
    """"Class responsible for crawling urls. Urls are provided to this class in a queue."""

    def __init__(self, queue):
        """"Assign the queue and create the necessary threads.
        Wait until the queue is empty and join all the running threads"""

        self.queue = queue
        self.create_threads()

        while not self.queue.empty():
            pass
        for t in threads:
            t.join()

    def create_threads(self):
        """Create, start and add threads to a list. Threads run an instance of ProcessingThread.
        The amount of threads created depends on the amount of cores found in the system."""

        for i in xrange(multiprocessing.cpu_count()):
            name = "Thread-%s" % i
            thread = ProcessingThread(name, self.queue)
            thread.start()
            threads.append(thread)
