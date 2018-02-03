from mrjob.job import MRJob
import re
import os

WORD_RE = re.compile(r"[\w']+")


class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    os.chdir("B:\MS\Spring2018\Big Data\Assigment- 3")
    MRWordCount.run()
    


