from mrjob.job import MRJob
import re
import string

WORD_RE = re.compile(r"[\w']+")
class MRWordCount(MRJob):

    def mapper(self, _, line):
        start = 'a'
        end = 'n'
        letters = string.ascii_lowercase
        allowed = letters[letters.index(start):letters.index(end)+1]
        for word in WORD_RE.findall(line):
            if any(word.lower().startswith(x) for x in allowed):
                yield "a to n", 1
            else:
                yield "other", 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordCount.run()


