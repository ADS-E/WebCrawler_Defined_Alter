class CsvHelper():
    def __init__(self, file="default.csv"):
        """
        :param file: the path of the file which to write to/read from as string
        """
        self._file = file

    @property
    def getFile(self):
        """
        :return: the path of the current set file as string
        """
        return self._file

    def setFile(self, file):
        """
        :param file: path of the file which to write to/read from as string
        :return: self
        """
        self._file = file
        return self

    def save(self, input=[]):
        """
        :param input: list (including list of lists)(default [])
        :return: boolean (depending on success)
        """
        print("TODO")

    def saveToNew(self, input=[]):
        """
        :param input: list (including list of lists)(default [])
        :return: boolean (depending on succes)
        """
        print("TODO")

    def read(self):
        """
        :return: returns the entire csv as list of lists
        """
        print("TODO")