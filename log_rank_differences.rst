This is a literate doctest.
Run ``python -m doctest -v log_rank_differences.rst`` to test.

Let's first of all grab Vanessa Gorman's lemmatisation of parts of Thucydides
and Xenophon.

>>> from lemma_counts import LemmaCounts

>>> gorman = LemmaCounts()
>>> gorman.load("gorman_data/lemma_counts.txt")

>>> thucydides = gorman.get_counts("0003")
>>> xenophon = gorman.get_counts("0032")

We can easily see the most common lemmas in each:

>>> thucydides.most_common(10)
[('ὁ', 3672), ('καί', 1836), ('δέ', 959), ('τε', 608), ('εἰμί', 593), ('αὐτός', 593), ('οὐ', 452), ('μέν', 337), ('εἰς', 329), ('ὅς', 312)]

>>> xenophon.most_common(10)
[('ὁ', 6236), ('καί', 3101), ('δέ', 2325), ('εἰμί', 1303), ('οὗτος', 1031), ('αὐτός', 1026), ('μέν', 771), ('τε', 563), ('οὐ', 562), ('τις', 536)]

But what if we were interested in lemmas that were common in one but not the
other. We can easily compare the rank of any given lemma in each subcorpus:

>>> from calc import rank_with_ties

>>> r_thuc = rank_with_ties(thucydides)
>>> r_xeno = rank_with_ties(xenophon)

>>> r_thuc["Κῦρος"], r_xeno["Κῦρος"]
(885, 30)

>>> r_thuc["δράω"], r_xeno["δράω"]
(196, 2345)

In other words, Κῦρος is rank 30 in Xenophon but only rank 885 in Thucydides.
δράω is rank 196 in Thucydides but only rank 2345 in Xenophon.

What if we wanted a list of all the lemmas in both sorted by how far their
ranks differ? This is where `log_rank_differences` comes in.

>>> from calc import log_rank_differences

>>> log_rank_diff = log_rank_differences(thucydides, xenophon)

>>> for lemma, log_diff in sorted(log_rank_diff.items(), key=lambda i: i[1], reverse=True)[:10]:
...     print(lemma, round(log_diff, 3))
Κῦρος 4.883
Μυτιληναῖοι 4.537
Κορίνθιος 3.964
Ἀττική 3.919
ἀμύνω 3.713
σοι 3.637
δράω 3.581
Πελοπόννησος 3.565
ἐπιμελέομαι 3.56
θύω1 3.268

As well as comparing authors (or works) we can compare different lemmatisations
of the same subcorpus.

Let's load counts for the subcorpus of Gorman and Diorisis that overlaps.

>>> gorman_overlap = LemmaCounts()
>>> gorman_overlap.load("gorman_data/lemma_counts_GD.txt")
>>> diorisis_overlap = LemmaCounts()
>>> diorisis_overlap.load("diorisis_data/lemma_counts_GD.txt")

>>> overlap_log_rank_diff = log_rank_differences(gorman_overlap.get_counts(), diorisis_overlap.get_counts())
>>> for lemma, log_diff in sorted(overlap_log_rank_diff.items(), key=lambda i: i[1], reverse=True)[:10]:
...     print(lemma, round(log_diff, 3))
λέγω 5.974
Ἀθήναια 5.159
ἔπειμι 4.507
εὐθύς 4.487
ἡδονή 4.356
πρόσειμι 4.326
πάρειμι 4.323
τίς 4.309
ποτός 4.265
ὁδός 4.201

If the texts were identically lemmatised, they'd have log diffs of zero.

But this can be used to help find systemic differences in lemmatisation.
