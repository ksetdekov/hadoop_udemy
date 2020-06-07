from mrjob.job import MRJob
from mrjob.step import MRStep


def reducer_count_ratings(key, values):
    yield None, (sum(values), key)


def mapper_get_ratings(_, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield movieID, 1


def sorter(_, counts):
    for key, count in sorted(counts, reverse=True):
        yield int(count), key


class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=mapper_get_ratings,
                   reducer=reducer_count_ratings),
            MRStep(reducer=sorter)
        ]


if __name__ == '__main__':
    RatingsBreakdown.run()
