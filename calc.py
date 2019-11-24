import collections
import math


def tokens_for_coverage(counter, limit):
    """
    Return a counter over the highest frequency tokens in the given `counter`
    until the total coverage exceeds the proportion given by `limit`.

    For example,
    `tokens_for_coverage(Counter(get_tokens(TokenType.lemma)), 0.5)`
    will return the Core 50% GNT Vocabulary (by lemma).
    """

    total_item_count = sum(counter.values())
    count_limit = total_item_count * limit

    cumulative_count = 0
    min_count = 0

    sub_counter = collections.Counter()

    for token, count in counter.most_common():
        if count < min_count:
            break
        sub_counter[token] += count
        cumulative_count += count
        if cumulative_count > count_limit:
            min_count = count

    return sub_counter


def print_coverage_table(overall_items, items_by_target, COVERAGE, ITEM_COUNTS):
    ranked_items = {x[0]: i for i, x in enumerate(overall_items.most_common(), 1)}

    rank_list_per_chunk = {
        target: sorted([ranked_items[item] for item in items])
        for target, items in items_by_target.items()
    }

    lowest_rank_needed = {}
    for coverage in COVERAGE:
        lowest_rank_needed[coverage] = {
            target:rank_list[math.ceil(coverage * len(rank_list)) - 1]
            for target, rank_list in rank_list_per_chunk.items()
        }

    print("{:7s}".format(""), end="")
    for coverage in COVERAGE:
        print("{:10.2%}".format(coverage), end="")
    print()
    print("-" * (7 + 10 * len(COVERAGE)))

    for item_count in ITEM_COUNTS:
        print("{:7d}".format(item_count), end="")
        for coverage in COVERAGE:
            num = len([freq for freq in lowest_rank_needed[coverage].values() if freq <= item_count])
            print("{:10.2%}".format(num / len(rank_list_per_chunk)), end="")
        print()

    print("{:>7s}".format("ALL"), end="")
    for coverage in COVERAGE:
        num = len([freq for freq in lowest_rank_needed[coverage].values() if freq <= len(ranked_items)])
        print("{:10.2%}".format(num / len(rank_list_per_chunk)), end="")
    print()


def rank_with_ties(counter):
    """
    given given a Counter build dictionary mapping each item to its rank.

    e.g. {'ὁ': 1, 'καί': 2, 'αὐτός': 3, 'ἐγώ': 4, 'λέγω': 5, ...}

    Note that items occuring the same number of times will have the same rank
    and it will always be 1 more than the number of more frequency items so
    ranks are skipped if there are ties (you might get 1, 2, 2, 4 for example).
    """

    item_rank = {}
    prev_count = math.inf  # == no previous
    inc1 = 0  # this goes up with each item
    inc2 = 0  # this is set to inc1 whenever the next item has a lower count

    for count, item in sorted(((count, item) for item, count in counter.items()), reverse=True):
        inc1 += 1
        if count < prev_count:
            inc2 = inc1
            prev_count = count
        item_rank[item] = inc2

    return item_rank
