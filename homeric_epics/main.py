from pathlib import Path
from collections import defaultdict
import enum


TokenType = enum.Enum('TokenType', 'text form lemma parse')
ChunkType = enum.Enum('TokenType', 'work book sentence line')


TOKEN_MAP = {
    TokenType.text: 'text', 
    TokenType.form: 'form', 
    TokenType.lemma: 'lemma', 
    TokenType.parse : 'parse'}

MYPATH = Path(__file__).parent
ILIAD_PATH = MYPATH / Path( 'texts/iliad.txt')
ODYSSEY_PATH = MYPATH / Path( 'texts/odyssey.txt')

PATHS = [('I', ILIAD_PATH), ('O', ODYSSEY_PATH)]

print(TokenType.text == 'text')

def get_tokens_by_line(token_type):
    output = {}
    target = TOKEN_MAP[token_type]
    for marker, p in PATHS:
        with open(p, 'r', encoding="UTF-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    ref, cons = line.strip().split(' ', maxsplit=1)
                    if ref.endswith(target):
                        output[ marker + '.' + ref.replace('.' + target, '')] = cons.split(' ')
                except:
                    print(marker, line)
                    exit()
    return output

def group_by_part_id(chunk_type, lines, include_line_breaks):
    output = defaultdict(list)
    for ref, words in lines.items():
        parts = ref.split('.')
        if chunk_type == ChunkType.work:
            output[parts[0]].extend(words)
            if include_line_breaks:
                output[parts[0]].append('//')

        if chunk_type == ChunkType.book:
            output['.'.join(parts[0:2])].extend(words)
            if include_line_breaks:
                output['.'.join(parts[0:2])].append('//')
        elif chunk_type == ChunkType.sentence:
            output['.'.join(parts[0:3])].extend(words)
            if include_line_breaks:
                output['.'.join(parts[0:3])].append('//')
    return output

def get_tokens_by_chunk(token_type, chunk_type, include_line_breaks=False):
    lines = get_tokens_by_line(token_type)
    if chunk_type == ChunkType.line:
        return lines
    return group_by_part_id(chunk_type, lines, include_line_breaks)


def get_tokens(token_type):
    output = []
    for xs in get_tokens_by_line(token_type).values():
        output.extend(xs)
    return output

if __name__ == '__main__':
    from collections import Counter
    c = Counter(get_tokens(TokenType.lemma))
    print(c.most_common(10))

    print("by chunk")
    books = get_tokens_by_chunk(TokenType.lemma, ChunkType.book)
    x = Counter(books['I.1'])
    print("10 most common lemmas in book 1 of Iliad")
    print(x.most_common(10))
    print("number of unique lemmas and total lemmas per book in Iliad")
    for key, words in [(k, val) for k, val in books.items() if 'I' in k]:
        unique = len(set(words))
        total = len(words)
        try:
            print(key, '\t', unique, '\t', total, round(total / unique, 2)) 
        except Exception as e:
            print(key, e)           
