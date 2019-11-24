This is a literate doctest.
Run ``python -m doctest -v examples2.rst`` to test.


>>> from collections import Counter
>>> import math

>>> from gnt_data import get_tokens, TokenType
>>> from calc import rank_with_ties


>>> gnt_lemmas = Counter(get_tokens(TokenType.lemma))


In `examples.rst` we built a ranking of lemmas like this:

>>> ranked_lemmas = {x[0]: i for i, x in enumerate(gnt_lemmas.most_common(), 1)}
>>> ranked_lemmas["λόγος"]
55

(in other words, λόγος is the 55th most frequent lemma in the GNT)

One characteristic of this approach is that lemmas occurring the same number of times will still have differing ranks.

Let's take as an example the 3001st and 3002nd ranked lemmas:

>>> gnt_lemmas.most_common()[2000], gnt_lemmas.most_common()[2100]
(('κινδυνεύω', 4), ('κατήγορος', 4))

you can see they both occur twice. They have the same frequency, but their ranking differs:

>>> ranked_lemmas["κινδυνεύω"], ranked_lemmas["κατήγορος"]
(2001, 2101)

For some applications, this is not a problem. But for others we might want to treat them the same.

If we want to treat ties as having the same ranking, we can use `rank_with_ties`:

>>> ranked_lemmas2 = rank_with_ties(gnt_lemmas)

>>> ranked_lemmas2["κινδυνεύω"], ranked_lemmas2["κατήγορος"]
(1859, 1859)

This can be interpreted as saying there are 1858 lemmas more frequent than the 4 times in the text κινδυνεύω or κατήγορος appear.
