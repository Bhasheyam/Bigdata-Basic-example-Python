from mrjob.job import MRJob

class Moviecount(MRJob):
    
    
    def mapper(self, _, line):
        (user,movieid,rate, timestamp) = line.split(',')
        yield user,1
        
    
    def combiner(self, user, movieid):
        yield user,sum(movieid)
    
    
    def reducer(self, user, moviesum):
        yield user,sum(moviesum)
        
if __name__ == '__main__':
    Moviecount.run()
