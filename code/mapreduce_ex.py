from mrjob.job import MRJob
from mrjob.step import MRStep


def reducer_count_ratings(key, values):
    yield key, sum(values)


def mapper_get_ratings(_, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield movieID, 1


class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=mapper_get_ratings,
                   reducer=reducer_count_ratings)
        ]


if __name__ == '__main__':
    RatingsBreakdown.run()
