import collections


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
