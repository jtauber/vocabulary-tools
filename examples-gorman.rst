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
Counter({'ὁ': 65557, 'καί': 25878, 'δέ': 15623, 'εἰμί': 9486, 'αὐτός': 7869, 'οὗτος': 7644, 'μέν': 6632, 'οὐ': 5582, 'τε': 4862, 'εἰς': 4829, 'ὅς': 4205, 'ἐν': 4177, 'τις': 3879, 'γάρ': 3777, 'πρός': 3262, 'γίγνομαι': 3050, 'ἐγώ': 3002, 'ἐπί': 2976, 'ὡς': 2912, 'ἐκ': 2748, 'περί': 2721, 'κατά': 2596, 'ἔχω': 2420, 'πᾶς': 2273, 'πολύς': 2251, 'ὁ': 2247, 'μή': 2242, 'ποιέω': 2122, 'πόλις': 2092, 'δέ': 2069, 'σύ': 2046, 'ἄλλος': 1935, 'ἀλλά': 1795, 'ἄν1': 1789, 'διά': 1778, 'εἰ': 1654, 'ἑαυτοῦ': 1578, 'λέγω3': 1546, 'φημί': 1531, 'ἤ1': 1403, 'μετά': 1370, 'ὑπό': 1357, 'ἀνήρ': 1295, 'οὖν': 1289, 'οὐδείς': 1285, 'ὅτι2': 1234, 'παρά': 1139, 'μέγας': 1114, 'ἀπό': 1031, 'δή': 1030, 'ἐκεῖνος': 997, 'οὕτως': 926, 'δοκέω': 925, 'λαμβάνω': 921, 'ἐπεί': 834})

>>> tokens_for_coverage(lysias, 0.5)
Counter({'ὁ': 2080, 'καί': 823, 'δέ': 495, 'εἰμί': 495, 'οὗτος': 403, 'αὐτός': 396, 'οὐ': 329, 'μέν': 302, 'σύ': 274, 'ἐγώ': 246, 'ὅς': 229, 'γάρ': 194, 'τε': 169, 'ἄν1': 162, 'ὅτι2': 159, 'εἰς': 154, 'τις': 154, 'γίγνομαι': 150, 'ὡς': 149, 'ἀνήρ': 143, 'ἐκεῖνος': 140, 'πολύς': 139, 'ἐν': 133, 'πόλις': 131, 'ἤ1': 128, 'ποιέω': 118, 'οὐδείς': 116, 'εἰ': 115, 'ὦ': 110, 'περί': 110, 'ἐκ': 101, 'δέ': 98, 'μή': 96, 'οὖν': 96, 'ἀλλά': 91, 'ἔχω': 86, 'ἐπί': 81, 'ἑαυτοῦ': 81, 'πᾶς': 80, 'ἄλλος': 80, 'δικαστής': 79})

>>> eratosthenes = get_counts("0540:001")
>>> tokens_for_coverage(eratosthenes, 0.5)
Counter({'ὁ': 282, 'καί': 93, 'ἐγώ': 76, 'εἰμί': 55, 'οὗτος': 52, 'δέ': 48, 'αὐτός': 45, 'μέν': 34, 'γάρ': 31, 'σύ': 27, 'ἀνήρ': 27, 'ὦ': 25, 'ὅς': 25, 'ἐκεῖνος': 24, 'εἰς': 23, 'οὐ': 21, 'ἄν1': 21, 'γυνή': 20, 'ὡς': 19, 'ἤ1': 18, 'πᾶς': 18, 'τις': 18, 'ὅτι2': 18, 'νόμος': 18, 'γίγνομαι': 18, 'δέ': 17, 'περί': 17, 'οὕτως': 17, 'τοιοῦτος': 16, 'ἐκ': 15, 'οὐδείς': 15, 'ἐν': 14, 'ποιέω': 14, 'εἰ': 13, 'τε': 13, 'ἔχω': 13, 'κελεύω': 13, 'ἡγέομαι': 13})

>>> print_tier_summary(
...    all_gorman,
...    [50, 80, 90, 95, 98],
...    [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000]
... )
The 50% point is reached at 55 lemmas (834 occurrences at that point)
The 80% point is reached at 916 lemmas (58 occurrences at that point)
The 90% point is reached at 2582 lemmas (16 occurrences at that point)
The 95% point is reached at 5323 lemmas (5 occurrences at that point)
The 98% point is reached at 10318 lemmas (2 occurrences at that point)
---
The 73.52% point is reached at 500 lemmas (104 occurrences at that point)
The 80.96% point is reached at 1000 lemmas (52 occurrences at that point)
The 87.82% point is reached at 2000 lemmas (22 occurrences at that point)
The 91.20% point is reached at 3000 lemmas (13 occurrences at that point)
The 93.26% point is reached at 4000 lemmas (8 occurrences at that point)
The 94.65% point is reached at 5000 lemmas (6 occurrences at that point)
The 95.64% point is reached at 6000 lemmas (4 occurrences at that point)
The 96.39% point is reached at 7000 lemmas (3 occurrences at that point)
The 97.01% point is reached at 8000 lemmas (3 occurrences at that point)
The 97.46% point is reached at 9000 lemmas (2 occurrences at that point)
The 97.87% point is reached at 10000 lemmas (2 occurrences at that point)
The 98.50% point is reached at 12000 lemmas (1 occurrences at that point)
The 99.11% point is reached at 15000 lemmas (1 occurrences at that point)
489437 tokens

>>> from calc import cumulative_frequency
>>> for lemma, freq in cumulative_frequency(all_gorman, limit=10).items():
...    print(lemma, round(100 * freq, 2))
ὁ 13.39
καί 18.68
δέ 21.87
εἰμί 23.81
αὐτός 25.42
οὗτος 26.98
μέν 28.34
οὐ 29.48
τε 30.47
εἰς 31.46
>>> lysias_cumfreq = cumulative_frequency(lysias)
>>> lysias_cumfreq['μέν']
0.2759031773181983

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
μοιχός 6
θεράπαινα 6
Ἐρατοσθένης 6
γνώμη 5
ἀγρός 5

The fact καὶ appears here suggests an error in the lemmatisation.
