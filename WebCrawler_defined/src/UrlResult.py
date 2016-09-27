class UrlResult():
    def __init__(self, url):
        self._results = {}
        self._url = url

    def addResult(self, key, value):
        if key in self._results:
            self._results[key] += value
        else:
            self._results[key] = value
        return self

    @property
    def getUrl(self):
        return self._url

    @property
    def getResults(self):
        return self._results
