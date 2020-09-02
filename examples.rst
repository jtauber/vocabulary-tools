    This is a literate doctest.
    Run ``python -m doctest -v examples.rst`` to test.


>>> from collections import Counter
>>> import math

>>> from gnt_data import get_tokens, get_tokens_by_chunk, TokenType, ChunkType
>>> from calc import tokens_for_coverage, print_coverage_table


10 most common lemmas in GNT
============================

>>> gnt_lemmas = Counter(get_tokens(TokenType.lemma))
>>> gnt_lemmas.most_common(10)
[('ὁ', 19769), ('καί', 8973), ('αὐτός', 5546), ('σύ', 2894), ('δέ', 2766), ('ἐν', 2733), ('ἐγώ', 2572), ('εἰμί', 2456), ('λέγω', 2345), ('εἰς', 1754)]


10 most common forms in John's Gospel
=====================================

>>> john_forms = Counter(get_tokens(TokenType.form, ChunkType.book, "64"))
>>> john_forms.most_common(10)
[('καί', 813), ('ὁ', 557), ('οὐ', 279), ('ὅτι', 270), ('τοῦ', 242), ('τόν', 240), ('ἐν', 220), ('δέ', 201), ('οὖν', 197), ('Ἰησοῦς', 193)]


Core 50% GNT Vocabulary
=======================

>>> tokens_for_coverage(gnt_lemmas, 0.5)
Counter({'ὁ': 19769, 'καί': 8973, 'αὐτός': 5546, 'σύ': 2894, 'δέ': 2766, 'ἐν': 2733, 'ἐγώ': 2572, 'εἰμί': 2456, 'λέγω': 2345, 'εἰς': 1754, 'οὐ': 1605, 'ὅς': 1408, 'οὗτος': 1385, 'θεός': 1307, 'ὅτι': 1294, 'πᾶς': 1244, 'γάρ': 1039, 'μή': 1036, 'ἐκ': 913, 'Ἰησοῦς': 906, 'ἐπί': 885, 'κύριος': 713, 'ἔχω': 706, 'πρός': 696, 'γίνομαι': 667, 'διά': 666, 'ἵνα': 662})


Core 70% Vocabulary for the Wedding at Cana pericope
====================================================

>>> cana_lemmas = Counter(get_tokens(TokenType.lemma, ChunkType.pericope, "04§05"))
>>> tokens_for_coverage(cana_lemmas, 0.7)
Counter({'ὁ': 35, 'καί': 15, 'αὐτός': 11, 'λέγω': 7, 'Ἰησοῦς': 6, 'δέ': 5, 'οἶνος': 5, 'εἰμί': 3, 'μήτηρ': 3, 'σύ': 3, 'ὕδωρ': 3, 'ἀρχιτρίκλινος': 3, 'γάμος': 2, 'γίνομαι': 2, 'ἐν': 2, 'Κανά': 2, 'Γαλιλαία': 2, 'ἐκεῖ': 2, 'μαθητής': 2, 'εἰς': 2, 'οὐ': 2, 'ἐγώ': 2, 'διάκονος': 2, 'ποιέω': 2, 'ὑδρία': 2, 'γεμίζω': 2, 'ἕως': 2, 'ἀντλέω': 2, 'φέρω': 2, 'οἶδα': 2, 'καλός': 2})


Words in the Wedding at Cana pericope not in the 80% Vocabulary for John's Gospel
=================================================================================

>>> john_lemmas = Counter(get_tokens(TokenType.lemma, ChunkType.book, "64"))
>>> john80 = tokens_for_coverage(john_lemmas, 0.8)
>>> sorted(cana_lemmas.keys() - john80.keys())
['Κανά', 'γάμος', 'γεμίζω', 'γεύομαι', 'διάκονος', 'δύο', 'καθαρισμός', 'καλέω', 'καλός', 'κατά', 'κεῖμαι', 'λίθινος', 'μήτηρ', 'μεθύω', 'μετρητής', 'νυμφίος', 'οἶνος', 'οὔπω', 'πρῶτος', 'πόθεν', 'τρίτος', 'τρεῖς', 'φανερόω', 'φωνέω', 'χωρέω', 'ἀνά', 'ἀντλέω', 'ἀρχή', 'ἀρχιτρίκλινος', 'ἄνω', 'ἄρτι', 'ἐλάσσων', 'ἕξ', 'ἕως', 'ἤ', 'ἥκω', 'ὑδρία', 'ὑστερέω']


What is left from the Core 80% GNT Vocabulary if you've read the Johannine Epistles and Gospel?
===============================================================================================

>>> johannine_lemmas = Counter(get_tokens(TokenType.lemma, ChunkType.book, "64")) + Counter(get_tokens(TokenType.lemma, ChunkType.book, "83")) + Counter(get_tokens(TokenType.lemma, ChunkType.book, "84")) + Counter(get_tokens(TokenType.lemma, ChunkType.book, "85"))
>>> gnt80 = tokens_for_coverage(gnt_lemmas, 0.8)
>>> sorted(gnt80.keys() - johannine_lemmas.keys())
['Παῦλος', 'γραμματεύς', 'διό', 'δύναμις', 'εἴτε', 'εὐαγγέλιον', 'εὐαγγελίζω', 'θρόνος', 'κηρύσσω', 'λοιπός', 'παραβολή', 'παρακαλέω', 'προσεύχομαι', 'πρόσωπον', 'σοφία', 'ἀποδίδωμι', 'ἄρα', 'ἑπτά', 'Ἰερουσαλήμ', 'ὑπάρχω']


How many words appear at least 10 times in the Johannine Epistles and Gospel?
=============================================================================

>>> johannine_at_least_10 = Counter({token:count for token, count in johannine_lemmas.items() if count >= 10})
>>> len(johannine_at_least_10)
231

And how much of those texts is that?
====================================

>>> sum(johannine_at_least_10.values())
16004

>>> sum(johannine_lemmas.values())
18039

>>> round(sum(johannine_at_least_10.values()) / sum(johannine_lemmas.values()), 3)
0.887

(i.e. 88.7% by token)

By token, what coverage will the top 10 lemmas in the entire GNT give me?
=========================================================================

>>> round(sum(count for token, count in gnt_lemmas.most_common(10)) / sum(gnt_lemmas.values()), 3)
0.377

(i.e. 37.7%)

And the top 100 lemmas?
=======================

>>> round(sum(count for token, count in gnt_lemmas.most_common(100)) / sum(gnt_lemmas.values()), 3)
0.662

(i.e. 66.2%)

Let's improve this by looking at actual verse coverage
======================================================

First we build a mapping of lemmas to their frequency rank:

>>> ranked_lemmas = {x[0]: i for i, x in enumerate(gnt_lemmas.most_common(), 1)}
>>> ranked_lemmas["λόγος"]
55

(in other words, λόγος is the 55th most frequent lemma in the GNT)

Then for each verse, we generate a sorted list of frequency ranks for the lemmas:

>>> rank_list_per_verse = {
...     verse: sorted([ranked_lemmas[lemma] for lemma in lemmas])
...     for verse, lemmas in get_tokens_by_chunk(TokenType.lemma, ChunkType.verse).items()
... }
>>> rank_list_per_verse["640316"]
[1, 1, 1, 1, 1, 3, 10, 14, 16, 17, 18, 23, 27, 29, 44, 48, 64, 78, 85, 119, 128, 191, 204, 239, 1189]

In other words, John 3.16 contains the most frequent lemma (5 times), the 3rd
most frequent lemma, the 10th most frequent lemma, and so on.

Now let's say we wanted to have 80% coverage of lemmas in each verse. We build
this new dictionary for each verse:

>>> coverage = 0.8
>>> lowest_rank_needed = {
...     target:rank_list[math.ceil(coverage * len(rank_list)) - 1]
...     for target, rank_list in rank_list_per_verse.items()
... }
>>> lowest_rank_needed["640316"]
119

This tells us that to reach 80% coverage of John 3.16, assuming we learn lemmas
in frequency order, we need to learn up to rank 119.

So if we want to know what proportion of verses would be readable at an 80%
coverage level with the 100 most frequent lemmas, we need to count how many
verses have a `lowest_rank_needed` of less-than-or-equal to 100.

>>> len([freq for freq in lowest_rank_needed.values() if freq <= 100])
1049

which as a proportion is:

>>> round(len([freq for freq in lowest_rank_needed.values() if freq <= 100]) / len(rank_list_per_verse), 3)
0.132

or 13.2%.

Print a nice coverage table
===========================

As seen in various blog posts and conferences presentations by yours truly.

>>> print_coverage_table(
...     gnt_lemmas,
...     get_tokens_by_chunk(TokenType.lemma, ChunkType.verse),
...     [0.50, 0.80, 0.90, 0.95, 0.98, 1.00],
...     [100, 200, 500, 1000, 2000, 5000]
... )
           50.00%    80.00%    90.00%    95.00%    98.00%   100.00%
-------------------------------------------------------------------
    100    91.07%    13.23%     2.14%     0.66%     0.49%     0.49%
    200    96.85%    35.12%     9.87%     3.47%     2.56%     2.56%
    500    99.13%    70.88%    36.75%    17.86%    13.85%    13.84%
   1000    99.72%    88.39%    62.68%    37.30%    30.04%    30.01%
   2000    99.91%    96.61%    84.98%    65.86%    57.01%    56.97%
   5000   100.00%    99.82%    99.03%    96.86%    96.09%    96.06%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%   100.00%

What about targets other than verses?
=====================================

One of the things we can now do for the first time is apply this analysis to
other chunking systems such as sentences, paragraphs, or pericopes.

Here is a table for sentences:

>>> print_coverage_table(
...     gnt_lemmas,
...     get_tokens_by_chunk(TokenType.lemma, ChunkType.sentence),
...     [0.50, 0.80, 0.90, 0.95, 0.98, 1.00],
...     [100, 200, 500, 1000, 2000, 5000]
... )
           50.00%    80.00%    90.00%    95.00%    98.00%   100.00%
-------------------------------------------------------------------
    100    91.13%    15.56%     3.68%     2.08%     1.99%     1.99%
    200    96.65%    37.94%    12.25%     6.32%     5.72%     5.72%
    500    99.10%    72.73%    39.60%    23.42%    20.05%    20.04%
   1000    99.77%    89.38%    64.20%    43.72%    37.73%    37.60%
   2000    99.95%    96.95%    85.96%    71.07%    62.58%    62.17%
   5000   100.00%    99.82%    99.12%    97.79%    96.63%    96.53%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%   100.00%

Or pericopes:

>>> print_coverage_table(
...     gnt_lemmas,
...     get_tokens_by_chunk(TokenType.lemma, ChunkType.pericope),
...     [0.50, 0.80, 0.90, 0.95, 0.98, 1.00],
...     [100, 200, 500, 1000, 2000, 5000]
... )
           50.00%    80.00%    90.00%    95.00%    98.00%   100.00%
-------------------------------------------------------------------
    100    98.13%     1.53%     0.00%     0.00%     0.00%     0.00%
    200    99.66%    18.68%     0.68%     0.00%     0.00%     0.00%
    500   100.00%    78.78%    17.66%     5.26%     0.34%     0.00%
   1000   100.00%    94.74%    64.86%    18.51%     5.09%     1.19%
   2000   100.00%    99.15%    92.02%    67.23%    25.81%     5.43%
   5000   100.00%   100.00%   100.00%    97.96%    91.17%    85.91%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%   100.00%

Obviously frequency order is not the most efficient way to get enough
vocabulary to read an entire pericope.

What about those easier to read sentences?
==========================================

Above we saw that 1.99% of sentences are completely readable with the 100
most frequent lemmas. But what sentences are they?

It's fairly straightforward to work out. Recall that the numbers in the cells
of the tables were achieved by narrowing down the chunks to just those that had
a `lowest_rank_needed` of less than the rank learned and then counting the
chunks? Well now we don't want to just count them, we want to list them!

>>> rank_list_per_sentence = {
...     sentence: sorted([ranked_lemmas[lemma] for lemma in lemmas])
...     for sentence, lemmas in get_tokens_by_chunk(TokenType.lemma, ChunkType.sentence).items()
... }

>>> coverage = 1.0
>>> lowest_rank_needed = {
...     sentence:rank_list[math.ceil(coverage * len(rank_list)) - 1]
...     for sentence, rank_list in rank_list_per_sentence.items()
... }

>>> sentences = [sentence for sentence, freq in lowest_rank_needed.items() if freq <= 100]
>>> len(sentences)
159

Remarkably, even just the top 20 most frequent lemmas give us 5 sentences.

>>> sentences = [sentence for sentence, freq in lowest_rank_needed.items() if freq <= 20]
>>> len(sentences)
5

>>> sentences
['610995', '640021', '640855', '830054', '830094']

>>> for sentence in sentences:
...     print(" ".join(token for token in get_tokens(TokenType.text, ChunkType.sentence, sentence)))
λέγει αὐτῷ· Σὺ εἶπας.
καὶ λέγει· Οὐκ εἰμί.
λέγει αὐτοῖς· Ἐγώ εἰμι.
καὶ ἐσμέν.
ἡμεῖς ἐκ τοῦ θεοῦ ἐσμεν·

What about by forms?
====================

I've talked a lot elsewhere about lemmas vs forms as the item focus. What do
some of these stats looks like by form? We'll stick with sentences.

where

>>> gnt_forms = Counter(get_tokens(TokenType.form))
>>> print_coverage_table(
...     gnt_forms,
...     get_tokens_by_chunk(TokenType.form, ChunkType.sentence),
...     [0.50, 0.80, 0.90, 0.95, 0.98, 1.00],
...     [100, 200, 500, 1000, 2000, 5000, 10000]
... )
           50.00%    80.00%    90.00%    95.00%    98.00%   100.00%
-------------------------------------------------------------------
    100    58.73%     0.78%     0.10%     0.08%     0.08%     0.08%
    200    79.62%     4.18%     0.70%     0.44%     0.44%     0.44%
    500    92.98%    16.29%     3.38%     1.84%     1.79%     1.79%
   1000    96.77%    35.65%    10.11%     5.19%     4.85%     4.85%
   2000    98.55%    59.51%    24.26%    12.07%    10.73%    10.73%
   5000    99.69%    84.31%    54.60%    34.45%    28.97%    28.91%
  10000    99.91%    94.10%    78.25%    64.54%    59.29%    59.21%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%   100.00%

>>> ranked_forms = {x[0]: i for i, x in enumerate(gnt_forms.most_common(), 1)}
>>> form_rank_list_per_sentence = {
...     sentence: sorted([ranked_forms[form] for form in forms])
...     for sentence, forms in get_tokens_by_chunk(TokenType.form, ChunkType.sentence).items()
... }

>>> coverage = 1.0
>>> lowest_rank_needed = {
...     sentence:rank_list[math.ceil(coverage * len(rank_list)) - 1]
...     for sentence, rank_list in form_rank_list_per_sentence.items()
... }

With forms, the top 100 only gives us 6 sentences.

>>> sentences = [sentence for sentence, freq in lowest_rank_needed.items() if freq <= 100]
>>> len(sentences)
6

>>> for sentence in sentences:
...     print(" ".join(token for token in get_tokens(TokenType.text, ChunkType.sentence, sentence)))
τί οὖν ἐστιν;
Τί οὖν;
ὅτι ἐξ αὐτοῦ καὶ δι’ αὐτοῦ καὶ εἰς αὐτὸν τὰ πάντα·
τί οὖν ἐστιν;
ὁ δὲ κύριος τὸ πνεῦμά ἐστιν·
τί γάρ;

But this sets us up for the next step: what if we order by something other than
straight frequency?
