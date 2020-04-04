import collections

class graph:

    def __init__(self, edges, directed = True):

        self.mapping = collections.defaultdict(list)
        # if directed, assumes u->v
        for u, v in edges:
            self.mapping[u].append(v)
            if not directed:
                self.mapping[v].append(u)
