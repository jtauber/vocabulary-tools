#!/usr/bin/env python3

from collections import Counter

from lemma_counts import LemmaCounts

from gnt_data import get_tokens, TokenType
from calc import tokens_for_coverage


def perc(n, d):
    return f"{round(100 * n / d, 2)}%"

# load GNT lemma counts
gnt_lemmas = Counter(get_tokens(TokenType.lemma))

# GNT lemmas to 90% level
gnt_lemmas_90 = tokens_for_coverage(gnt_lemmas, 0.9)

# GNT lemmas to 80% level
gnt_lemmas_80 = tokens_for_coverage(gnt_lemmas, 0.8)

diorisis = LemmaCounts()
diorisis.load("diorisis_data/lemma_counts.txt")

titles = {}  # titles by tlgId
lemma_counters = {}  # lemma Counters by tlgId

## populate titles and lemma_counts with Plato counts from Diorisis

with open("diorisis_data/catalog.tsv") as f:
    f.readline()  # header
    for line in f:
        parts = line.strip().split("\t")
        title, tlgAuthor, tlgId = parts[1:4]
        if tlgAuthor == "0059":  # Plato
            titles[tlgId] = title
            lemma_counters[tlgId] = diorisis.get_counts(f"0059:{tlgId}")

## calculate and print table

print("id", "title", "lemmas", "tokens", "GNT lemmas", "GNT tokens", "% GNT lemmas", "% GNT tokens", sep="\t")

for tlgId in sorted(titles.keys()):
    a = len(lemma_counters[tlgId])
    b = sum(lemma_counters[tlgId].values())
    c = sum(1 for lemma in gnt_lemmas if lemma in lemma_counters[tlgId])
    d = sum(lemma_counters[tlgId][lemma] for lemma in gnt_lemmas)

    print(tlgId, titles[tlgId], a, b, c, d, perc(c, a), perc(d, b), sep="\t")
