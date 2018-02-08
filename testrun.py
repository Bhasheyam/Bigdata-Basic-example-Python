from mrjob.job import MRJob
import re
import os

WORD_RE = re.compile(r"[\w']+")
WORD_RE_a_n = re.compile(r'\b[a-n]\w*')


class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
                if(word in WORD_RE_a_n.findall(line)):
                        yield "a_n", 1
                else:
                        yield "other", 1
    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    os.chdir("B:\MS\Spring2018\Big Data\Assigment- 3")
    MRWordCount.run()