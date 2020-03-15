import collections
import os.path


class LemmaCounts:
    def __init__(self):
        self.all = collections.Counter()
        self.by_author = collections.defaultdict(collections.Counter)
        self.by_work = collections.defaultdict(collections.Counter)

    def load(self, filename):
        with open(filename) as f:
            for line in f:
                work_id, lemma, count = line.strip().split()
                author_id, _ = work_id.split(":")
                count = int(count)
                self.all[lemma] += count
                self.by_author[author_id][lemma] += count
                self.by_work[work_id][lemma] += count

    def get_counts(self, prefix=None):
        """
        no prefix returns a Counter of all lemmas
        author prefix like `0540` will return Counter of lemmas in that author
        work prefix like `0540:001` will return Counter of lemmas in that work
        """
        if prefix is None:
            return self.all
        elif ":" not in prefix:
            return self.by_author.get(prefix, collections.Counter())
        else:
            return self.by_work.get(prefix, collections.Counter())
