# Homeric Vocabulary Tools

This repository is modeled on James's Tauber's [`vocabulary-tools`](https://github.com/jtauber/vocabulary-tools) module for the Greek New Testament, but is for Homer's _Iliad_ and _Odyssey_. It provides a similar API as well. 

Each line in the data has a reference id in the following schema: `work.book.sentence.line`. The Iliad is `I` and the Odyssey is `O`. Thus `O.1.1.1` would refer to the first poetic line in the first sentence in the first book of the Odyssey and `I.1.1.1` would be the same line but in the Iliad. 

There are four `TokenType`s: 

* text
* form
* lemma 
* parse 

There are four `ChunkType`s:

* work
* book
* sentence
* line

The difference between `text` and `form` is that, `text` includes punctuation. So by asking for the text and then using `' '.join(chunks)` should give a nice readable line of whatever chunk (work, book, sentence, line). 

One difference between this a `vocab_tools` is that `get_tokens_by_chunk` includes an optional argument `include_line_breaks` that defaults to `False`. If it is `True`, then it will add `//` after each line if the `ChunkType` is not `line` so that the poetic lines are visible even when working with other ChunkTypes. Note that this will throw off counts as the `//`s will be counted as tokens.

The `main.py` shows some examples of how the code can be used. 

# Data Sources

The Greek data was taken from the [Ancient Greek and Latin Dependency Treebank](https://perseusdl.github.io/treebank_data/) which is released under a [CC By-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/us/) license.

* Iliad source file is tlg0012.tlg001.perseus-grc1.tb
* Oddyssey source file is tlg0012.tlg002.perseus-grc1.tb

# License

Because of the licensing of the source data and because I hope this can be freely used and furher developed, this repo is released under a a [CC By-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/us/) license.