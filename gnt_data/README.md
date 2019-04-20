# About the GNT Data

`tokens.txt` contains the MorphGNT SBLGNT tokens in the following columns:

- token id
- text of token
- normalised form of token
- part-of-speech
- morphological tag (old)
- morphological tag (new)
- lemma

Each of `verses.txt`, `sentences.txt`, `paragraphs.txt`, `pericopes.txt`
respectively maps verses, sentences, paragraphs and pericopes to a range of
tokens. The columns are:

- identifier
- start token id
- end token id
