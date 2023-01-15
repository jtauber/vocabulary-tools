import enum
import sys
import os.path

TokenType = enum.Enum("TokenType", "form lemma parse morph_lemma all")
ChunkType = enum.Enum("ChunkType", "book chapter verse paragraph pericope")

chunk_data_filename = {
    ChunkType.book: "books.txt",
    ChunkType.chapter: "chapters.txt",
    ChunkType.verse: "verses.txt",
    ChunkType.paragraph: "paragraphs.txt",
    ChunkType.pericope: "pericopes.txt"
}


chunk_ids = {}
chunk_data = {}


def load_chunk_data():
    for chunk_type, filename in chunk_data_filename.items():
        chunk_ids[chunk_type] = []
        print(f'loading {filename}', file=sys.stderr)
        with open(os.path.join(os.path.dirname(__file__), filename), encoding="UTF-8") as f:
            for line in f:
                try:
                    chunk_id, token_start, token_end = line.strip().split(maxsplit=2)
                    chunk_data[(chunk_type, chunk_id)] = (
                        int(token_start), int(token_end)
                    )
                    chunk_ids[chunk_type].append(chunk_id)
                except:
                    print(line)
                    sys.exit()


def load_wlc():
    with open(os.path.join(os.path.dirname(__file__), "tokens.txt"), 'r', encoding="UTF-8") as f:
        for line in f:
            yield line.replace('\n','').split('\t', maxsplit=4)


token_data = {}


def load_tokens():
    for token_type in TokenType:
        token_data[token_type] = []
    for token_id, ref, form, lemma, parse in load_wlc():
        token_data[token_type.form].append(form)
        token_data[token_type.lemma].append(lemma)
        token_data[token_type.morph_lemma].append((parse, lemma))
        token_data[token_type.parse].append(parse)
        token_data[token_type.all].append((form, lemma, parse))


load_tokens()
load_chunk_data()


def get_tokens(token_type, chunk_type=None, chunk_id=None):
    if chunk_type and chunk_id:
        start, end = chunk_data[(chunk_type, chunk_id)]
        return token_data[token_type][start - 1:end]
    elif chunk_type is None and chunk_id is None:
        return token_data[token_type]
    else:
        raise ValueError(
            "either both or neigher of chunk_type and chunk_id"
            "must be provided"
        )


def get_tokens_by_chunk(token_type, chunk_type):
    return {
        chunk_id: get_tokens(token_type, chunk_type, chunk_id)
        for chunk_id in chunk_ids[chunk_type]
    }


def get_chunk_ids(chunk_type):
    return chunk_ids[chunk_type]


def pprint_text(items):
    return ' '.join(items).replace(' ׃', '׃').replace(' ־ ', '־').replace(' /', '').replace('/', '')


def load_pericope_verse_map():
    data = {}
    with open(os.path.join(os.path.dirname(__file__),'pericope_verse_map.txt'), 'r', encoding="UTF-8") as f:
        for line in f:
            pid, start, end = line.strip().split(" ", maxsplit=2)
            data[pid] = (start, end)
    return data


if __name__ == "__main__":
    from heb_lex_tools import HEBLEX
    glosser = HEBLEX()
    for token in get_tokens(TokenType.lemma, ChunkType.verse, "Gen.1.1"):
        print(f"{token}: '{glosser.strongs_to_gloss(token)}'")

    with open('test.txt', 'w', encoding="UTF-8") as f:
        print(pprint_text(get_tokens_by_chunk(TokenType.form, ChunkType.verse)["Gen.1.1"]), file=f)
