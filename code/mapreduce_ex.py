def mapper_get_ratings(self, _, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield rating, 1

def reducer_count_ratings(self, key, value):
    yield key, sum(value)

from mrjob.job import