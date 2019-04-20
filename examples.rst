    This is a literate doctest.
    Run ``python -m doctest -v examples.rst`` to test.


>>> from collections import Counter

>>> from gnt_data import get_tokens, TokenType, ChunkType
>>> from calc import tokens_for_coverage


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
============================================================================

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
