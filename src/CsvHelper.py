import csv

class CsvHelper():

    @staticmethod
    def save(urlResult):
        """
        :param: filepath where to write the result to
        :param: list (including list of lists)(default [])
        :return: boolean (depending on success)
        """
        with open('results.csv', "a+") as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            values = urlResult.values()
            writer.writerow(urlResult.geturl() + urlResult.values)

    @staticmethod
    def read(filepath):
        """
        :param: takes the filepath as input for which file to read
        :return: returns the entire csv as list of lists
        """
        result = []
        with open(filepath) as csvfile:
            data = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in data:
                result.append(row[0])
        return result

    @staticmethod
    def getWordsToCount():
        """
        :return: returns all the words which to crawl
        """
        result = []
        with open('wordlist.csv') as csvfile:
            data = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in data:
                result.append(row)
        return [item for sublist in result for item in sublist]