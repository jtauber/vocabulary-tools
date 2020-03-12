    This is a literate doctest.
    Run ``python -m doctest -v examples-gorman.rst`` to test.

Examples from Vanessa Gorman's Treebanks
========================================


>>> from gorman_data import get_counts
>>> from calc import tokens_for_coverage, print_tier_summary

>>> all_gorman = get_counts()
>>> lysias = get_counts("0540")
>>> eratosthenes = get_counts("0540:001")

>>> tokens_for_coverage(all_gorman, 0.5)
Counter({'ὁ': 68784, 'καί': 26518, 'δέ': 17990, 'εἰμί': 9976, 'αὐτός': 8093, 'οὗτος': 7951, 'μέν': 6715, 'οὐ': 5751, 'τε': 4978, 'εἰς': 4867, 'ὅς': 4670, 'ἐν': 4281, 'τις': 3935, 'γάρ': 3825, 'ἐπί': 3329, 'πρός': 3291, 'ἐγώ': 3139, 'γίγνομαι': 3082, 'ὡς': 3014, 'κατά': 2941, 'ἐκ': 2778, 'περί': 2755, 'ἔχω': 2493, 'πᾶς': 2316, 'μή': 2306, 'πολύς': 2268, 'ἀλλά': 2229, 'σύ': 2158, 'ποιέω': 2156, 'πόλις': 2118, 'ἄλλος': 2006, 'διά': 1981, 'ἄν1': 1800, 'εἰ': 1696, 'ἑαυτοῦ': 1626, 'λέγω3': 1599, 'μετά': 1592, 'φημί': 1586, 'παρά': 1576, 'ὑπό': 1563, 'ἤ1': 1423, 'ἀνήρ': 1335, 'οὖν': 1306, 'οὐδείς': 1298, 'ὅτι2': 1240, 'μέγας': 1148, 'ἐκεῖνος': 1122, 'ἀπό': 1120, 'δή': 1034})

>>> tokens_for_coverage(lysias, 0.5)
Counter({'ὁ': 2105, 'καί': 835, 'δέ': 596, 'εἰμί': 496, 'οὗτος': 411, 'αὐτός': 399, 'οὐ': 329, 'μέν': 302, 'σύ': 274, 'ἐγώ': 248, 'ὅς': 232, 'γάρ': 194, 'τε': 170, 'ἄν1': 162, 'ὅτι2': 159, 'εἰς': 154, 'τις': 154, 'γίγνομαι': 150, 'ὡς': 150, 'ἐκεῖνος': 147, 'ἀνήρ': 144, 'πολύς': 139, 'ἀλλά': 133, 'ἐν': 133, 'πόλις': 131, 'ἤ1': 128, 'ποιέω': 120, 'εἰ': 116, 'οὐδείς': 116, 'περί': 110, 'ὦ': 110, 'ἐκ': 101, 'ἐπί': 97, 'μή': 97, 'οὖν': 96, 'ὑπό': 96, 'ἔχω': 86, 'ἄλλος': 83})

>>> eratosthenes = get_counts("0540:001")
>>> tokens_for_coverage(eratosthenes, 0.5)
Counter({'ὁ': 283, 'καί': 99, 'ἐγώ': 77, 'δέ': 65, 'εἰμί': 55, 'οὗτος': 53, 'αὐτός': 45, 'μέν': 34, 'γάρ': 31, 'ἀνήρ': 27, 'σύ': 27, 'ἐκεῖνος': 27, 'ὦ': 25, 'ὅς': 25, 'εἰς': 23, 'ἄν1': 21, 'οὐ': 21, 'γυνή': 20, 'ὡς': 19, 'γίγνομαι': 18, 'ὅτι2': 18, 'πᾶς': 18, 'ἤ1': 18, 'νόμος': 18, 'τις': 18, 'περί': 17, 'οὕτως': 17, 'τοιοῦτος': 16, 'ἐπί': 15, 'οὐδείς': 15, 'ἐκ': 15, 'ποιέω': 14, 'ἀλλά': 14, 'ἐν': 14})

>>> print_tier_summary(
...    all_gorman,
...    [50, 80, 90, 95, 98],
...    [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000]
... )
The 50% point is reached at 49 lemmas (1034 occurrences at that point)
The 80% point is reached at 845 lemmas (62 occurrences at that point)
The 90% point is reached at 2397 lemmas (17 occurrences at that point)
The 95% point is reached at 4906 lemmas (6 occurrences at that point)
The 98% point is reached at 9545 lemmas (2 occurrences at that point)
---
The 74.46% point is reached at 500 lemmas (103 occurrences at that point)
The 81.78% point is reached at 1000 lemmas (52 occurrences at that point)
The 88.48% point is reached at 2000 lemmas (22 occurrences at that point)
The 91.77% point is reached at 3000 lemmas (12 occurrences at that point)
The 93.77% point is reached at 4000 lemmas (8 occurrences at that point)
The 95.11% point is reached at 5000 lemmas (6 occurrences at that point)
The 96.05% point is reached at 6000 lemmas (4 occurrences at that point)
The 96.76% point is reached at 7000 lemmas (3 occurrences at that point)
The 97.37% point is reached at 8000 lemmas (3 occurrences at that point)
The 97.78% point is reached at 9000 lemmas (2 occurrences at that point)
The 98.18% point is reached at 10000 lemmas (2 occurrences at that point)
The 98.73% point is reached at 12000 lemmas (1 occurrences at that point)
The 99.34% point is reached at 15000 lemmas (1 occurrences at that point)
495495 tokens

>>> from calc import cumulative_frequency
>>> for lemma, freq in cumulative_frequency(all_gorman, limit=10).items():
...    print(lemma, round(100 * freq, 2))
ὁ 13.88
καί 19.23
δέ 22.86
εἰμί 24.88
αὐτός 26.51
οὗτος 28.12
μέν 29.47
οὐ 30.63
τε 31.64
εἰς 32.62
>>> lysias_cumfreq = cumulative_frequency(lysias)
>>> lysias_cumfreq['μέν']
0.2832375925063396

What are the top ten lemmas in On the Murder of Eratosthenes that aren't in Plato's Apology?
============================================================================================

>>> plato_apology = get_counts("0059:002")
>>> missing = eratosthenes.keys() - plato_apology.keys()
>>> for k, v in [i for i in eratosthenes.most_common() if i[0] in missing][:10]:
...     print(k, v)
οὔτε 11
οἰκία 10
καὶ 8
θύρα 7
ζημία 6
Ἐρατοσθένης 6
θεράπαινα 6
μοιχός 6
γνώμη 5
ἀγρός 5

The fact καὶ appears here suggests an error in the lemmatisation.
