def peshitta_section(s, e):
    start = int(s)
    end = int(e)
    with open('peshitta_list.txt') as f:
        for line in f:
            r, word, pointed, lemma, gloss, parse = line.split('\t', maxsplit=5)
            ref = int(r)
            if ref >= start and ref <= end:
                yield (r, word, pointed, lemma, gloss, parse.strip())
            elif ref > end:
                break

def peshitta_pericopes():
    with open("peshitta_sections.txt", 'r') as f:
        for line in f:
            yield line.strip().split(" ", maxsplit=3)

def get_peshitta_pericopes_dir():
    out = {}
    for ref, start, end, title in peshitta_pericopes():
        out[ref] = (start, end, title)
    return out
