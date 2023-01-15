#!/usr/bin/env python3
import sys
from collections import Counter
from main import TokenType, ChunkType, get_tokens_by_chunk, get_tokens
from heb_lex_tools import HEBLEX

# Count lemmas in a book
def count_lemmas(book_id):
    return len(get_tokens_by_chunk(TokenType.lemma, ChunkType.book)[book_id])


def build_flashcard_spreadsheet(book_id, limit, output_name, glosser, lower_limit=0):
    lemmas = Counter(get_tokens_by_chunk(TokenType.lemma, ChunkType.book)[book_id])
    delim = '\t'
    total_items = 0
    with open(output_name, 'w', encoding="UTF-8") as f:
        for (lemma, count) in lemmas.most_common():
            if count <= limit and count >= lower_limit:
                total_items += 1
                print(delim.join([str(count), glosser.strongs_to_lemma(lemma),
                                  glosser.strongs_to_gloss(lemma)]), file=f)
        print('===========================', file=f)
        print(f"Total items in {book_id} below {limit} was {total_items}", file=f)


GLOSSER = HEBLEX()
HEB_LEMMAS = Counter(get_tokens(TokenType.lemma))

def get_hapax_in_book(book_id, total_counts, glosser):
    book_counts = Counter(get_tokens_by_chunk(TokenType.lemma, ChunkType.book)[book_id])
    with open(f"{book_id}_hapax.tab", 'w', encoding="UTF-8") as f:
        print('\t'.join(["Lemma", "Count in book", "Count in Hebrew Bible", "Gloss"]), file=f)
        for (lemma, count) in book_counts.most_common():
            if count == 1:
                print('\t'.join([glosser.strongs_to_lemma(lemma),
                                 str(count),
                                 str(total_counts[lemma]),
                                 glosser.strongs_to_gloss(lemma)]), file=f)


# build flachard spreadsheet including hapaxlegomena
build_flashcard_spreadsheet("Isa", 100, "Isa_vocab.tab", GLOSSER)

# buildi flashcard spreadsheet without hapaxlegomena.
build_flashcard_spreadsheet("Isa", 100, "Isa_vocab_no_hapax.tab", GLOSSER, 2)

# Get data on hapaxlegomena in book
get_hapax_in_book("Isa", HEB_LEMMAS, GLOSSER)
