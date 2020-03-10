import collections
import os.path


ALL = collections.Counter()
BY_AUTHOR = collections.defaultdict(collections.Counter)
BY_WORK = collections.defaultdict(collections.Counter)

def load_data():
    with open(os.path.join(os.path.dirname(__file__), "lemma_counts.txt")) as f:
        for line in f:
            work_id, lemma, count = line.strip().split()
            author_id, _ = work_id.split(":")
            count = int(count)
            ALL[lemma] += count
            BY_AUTHOR[author_id][lemma] += count
            BY_WORK[work_id][lemma] += count


def get_counts(prefix=None):
    """
    no prefix returns a Counter of all lemmas
    an author prefix like `0540` will return a Counter of lemmas in that author
    a work prefix like `0540:001` will return a Counter of lemmas in that work
    """
    if prefix is None:
        return ALL
    elif ":" not in prefix:
        return BY_AUTHOR.get(prefix, collections.Counter())
    else:
        return BY_WORK.get(prefix, collections.Counter())


load_data()

# for quick testing
if __name__ == "__main__":
    all_lemmas = get_counts()
    lysias_lemmas = get_counts("0540")
    eratosthenes_lemmas = get_counts("0540:001")

    print(len(all_lemmas), [k for k, v in all_lemmas.most_common(10)])
    print(len(lysias_lemmas), [k for k, v in lysias_lemmas.most_common(10)])
    print(len(eratosthenes_lemmas), [k for k, v in eratosthenes_lemmas.most_common(10)])
