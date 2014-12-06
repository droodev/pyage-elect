
class Votes(object):
    def __init__(self, votes, candidate):
        self.votes = [list(h) for h in votes]
        self.fitness = None
        self.candidate = candidate

    def __str__(self):
        return "{0}\nfitness: {1} HASH: {2}".format(self.votes, self.fitness, self.__hash__())
        
