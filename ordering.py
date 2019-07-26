import collections


def frequency(target_items):
    """
    Orders the learning of items based purely on frequency. Targets ordered by
    when they are achieved.

    The input `target_items` is a dictionary mapping targets to the
    prerequisite items.

    This is a generator that yields the target along with a set of the items
    for that target that have not yet been seen (plus any others of higher
    frequency, even if they aren't needed by the target)
    """

    # a dictionary mapping targets to a set of items still not learnt
    MISSING_IN_TARGET = {}

    # a dictionary mapping items to a set of targets the items are needed for
    # and are missing from
    TARGETS_MISSING = collections.defaultdict(set)

    c = collections.Counter()

    for target, items in target_items.items():
        c.update(items)

        MISSING_IN_TARGET[target] = set(items)
        for item in items:
            TARGETS_MISSING[item].add(target)

    ITEMS_TO_LEARN = set()

    for next_item, count in c.most_common():

        ITEMS_TO_LEARN.add(next_item)

        # for each target missing that item, remove the item
        for target in TARGETS_MISSING[next_item]:
            MISSING_IN_TARGET[target].remove(next_item)

            # if the target is now missing no items...
            if len(MISSING_IN_TARGET[target]) == 0:

                yield target, ITEMS_TO_LEARN

                # remove from missing in that target
                del MISSING_IN_TARGET[target]

                # reset items to learn
                ITEMS_TO_LEARN = set()

        # remove the item from all targets requiring it
        del TARGETS_MISSING[next_item]


def frequency_optimised(target_items):
    """
    Orders the learning of targets by firstly ordering items by frequency but
    then only requiring learning of those items required by the targets
    achievable by the frequency ordering.

    The input `target_items` is a dictionary mapping targets to the
    prerequisite items.

    This is a generator that yields the target along with a set of the items
    for that target that have not yet been seen.
    """

    # track the set of all items already learnt
    ALREADY_LEARNT = set()

    # a dictionary mapping targets to the set of prerequisite items
    IN_TARGET = {}

    # a dictionary mapping targets to a set of items still not learnt
    MISSING_IN_TARGET = {}

    # a dictionary mapping items to a set of targets the items are needed for
    # and are missing from
    TARGETS_MISSING = collections.defaultdict(set)

    c = collections.Counter()

    for target, items in target_items.items():
        c.update(items)

        IN_TARGET[target] = set(items)
        MISSING_IN_TARGET[target] = set(items)
        for item in items:
            TARGETS_MISSING[item].add(target)

    for next_item, count in c.most_common():

        # for each target missing that item, remove the item
        for target in TARGETS_MISSING[next_item]:
            MISSING_IN_TARGET[target].remove(next_item)

            # if the target is now missing no items...
            if len(MISSING_IN_TARGET[target]) == 0:

                # calculate what is new to learn for that target
                items_to_learn = IN_TARGET[target] - ALREADY_LEARNT

                yield target, items_to_learn

                # remove from missing in that target
                del MISSING_IN_TARGET[target]

                # add to items already learnt
                ALREADY_LEARNT.update(items_to_learn)

        # remove the item from all targets requiring it
        del TARGETS_MISSING[next_item]


def next_best(target_items):
    """
    Orders the learning of targets based on, at each step, assigning a score to
    each unknown item and prioritising the highest scoring item next before
    recalculating the scores all over again with the remaining items.

    The score is currently the sum of

        1 / 2 ** number_of_items_missing_from_target

    for each target in which the item is missing.

    Therefore, at each step, it favours a next item that is the only missing
    item (or one of only a few missing items) from lots of targets.

    Once all the prerequisite items in a target have come up as the next item,
    that target is yielded along with a set of the items for that target that
    have not yet been seen.

    The input `target_items` is a dictionary mapping targets to the
    prerequisite items.
    """

    # track the set of all items already learnt
    ALREADY_LEARNT = set()

    # a dictionary mapping targets to the set of prerequisite items
    IN_TARGET = {}

    # a dictionary mapping targets to a set of items still not learnt
    MISSING_IN_TARGET = {}

    # a dictionary mapping items to a set of targets the items are needed for
    # and are missing from
    TARGETS_MISSING = collections.defaultdict(set)

    ## fill the dictionaries with initial data based on the input

    for target, items in target_items.items():
        IN_TARGET[target] = set(items)
        MISSING_IN_TARGET[target] = set(items)
        for item in items:
            TARGETS_MISSING[item].add(target)

    while True:

        # for each item, a score of how bad it is that it is missing
        MISSING_ITEMS = collections.defaultdict(int)

        for missing in MISSING_IN_TARGET.values():
            for item in missing:
                # if item is only missing item for a target, add 1/2 to its score
                # if item is 1 of 2 missing items for a target, add 1/4
                # if item is 1 of 3 missing items for a target, add 1/8
                # and so on...
                MISSING_ITEMS[item] += 1. / (2 ** len(missing))

        # stop if there are no missing items
        if not MISSING_ITEMS:
            break

        # otherwise the next item to learn is the one with the highest score
        next_item = sorted(MISSING_ITEMS, key=MISSING_ITEMS.get)[-1]

        # for each target missing that item, remove the item
        for target in TARGETS_MISSING[next_item]:
            MISSING_IN_TARGET[target].remove(next_item)

            # if the target is now missing no items...
            if len(MISSING_IN_TARGET[target]) == 0:

                # calculate what is new to learn for that target
                items_to_learn = IN_TARGET[target] - ALREADY_LEARNT

                yield target, items_to_learn

                # remove from missing in that target
                del MISSING_IN_TARGET[target]

                # add to items already learnt
                ALREADY_LEARNT.update(items_to_learn)

        # remove the item from all targets requiring it
        del TARGETS_MISSING[next_item]
