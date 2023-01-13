from unicodedata import normalize


CANTILLATION_MARKS = ['059' + x for x in '0123456789ABCDEF']
CANTILLATION_MARKS.append("05BD")  
CANTILLATION_MARKS = set([int(y, 16) for y in (CANTILLATION_MARKS + ['05A' + x for x in '0123456789ABCDEF'])])  


VOWEL_MARKS = set(map(lambda x: int(x, 16), ['05B' + x for x in '0123456789ABCDEF'] + ['05C7']))

CONSONANTS = set(map(lambda x: int(x, 16), ['05D' + x for x in '0123456789ABCDEF'] + ['05E' + x for x in '0123456789A'] + ['05F' + x for x in '012']))


def strip_marks(x, marks):
    return ''.join([
        c 
        for c in normalize('NFD', x)
        if  ord(c) not in marks])


def strip_cantillation(x):
    return strip_marks(x, CANTILLATION_MARKS)


def strip_vowels(x):
    return strip_marks(x, VOWEL_MARKS)


def only_consonants(x):
    return ''.join([
        ch 
        for ch in normalize('NFD', x)
        if ord(ch) in CONSONANTS
    ])


if __name__ == '__main__':
    TEST = "שָׁמַ֨רְנוּ֙"
    TEST2 = 'שְׁמַרְתֶּ֔ם'
    print(strip_cantillation(TEST2))
    print(strip_vowels(TEST))
    print(only_consonants(TEST))
