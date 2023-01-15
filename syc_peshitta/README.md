# README

# Introduction

This is a repo of tools for the analysis of the Syriac Peshitta based on George A. Kiraz SEDRA 3 database (see below). It relies on bits and pieces taken from other repos and my own code. See `Sources` for details.



# Data files

## `peshitta_list.txt`

This is a database file containing the data culled from the SEDRA database. It has the form of:

```
reference unpointed-form pointed-form lemma gloss parse
```

The reference is a number such that:

* 0-2 = book
* 2-4 = chapter
* 4-6 = verse
* 6-8 = word index

For example, take the number `520100101`. `52` is the book (Matthew in this case), `01` is the first chapter, `001` is verse 1, and `01` is the first word in the verse.


## `peshitta_sections.txt`

A list of pericope definitions in the following form:

```
pericope-key start end title
```

`start` and `end` are references in the same format as in `peshitta_list.txt`


# Code files

## `peshitta.py`

* `peshitta_section(start, end)` is an iterator over all the lines in the from `peshitta_list.txt` (see below) within the `start` and `end` reference numbers.

* `peshitta_pericopes()` returns an iterator over the pericopes for the Peshitta. This function relies on the definitions found in `peshitta_sections.txt` (see below). It returns a tuple of `(reference, start, end, title)`.

* `get_peshitta_pericopes_dir()` is a helper function that returns a dictionary for all pericopes. The section number is the key, with `(start, end, title)` as the value.


## `build_pericope_db.py`

Uses `peshitta.py` to build the three reading order databases found in the `analysis` folder. Each line of the database has the form of `pericope-key` and `items` separated by a tab (`\t`).


## `calc_reading_order.py`

This file builds three reading orders for the Peshitta using the `next_best` algorithm from `ordering.py`.

* `calc_path(fname, oname, name_map)` where `fname` is the file path to the database containing a map of pericopes to items to be learned. Each line of the database has the form of `pericope-key` and `items` separated by a tab (`\t`).

This file currently reads three database files found in the `analysis` folder and outputs three reading paths through the Syriac NT to the `reading_orders` folder.


## `to_html.py`

Builds a simple (very simple) html reader based on the reading order found in `reading_combined.txt`. This can be changed to use any of the other reading orders and it should still work fine.


## `sedra/convert_to_words.py`

This script builds `peshitta_list.txt` from the files in the `sedra` directory.

# Sources

`ordering.py` is from James Tauber's [vocabulary-tools](https://github.com/jtauber/vocabulary-tools).

This work makes use of the Syriac Electronic Data
Retrieval Archive (SEDRA) by George A. Kiraz, distributed
by the Syriac Computing Institute.


See this paper for more info:

G. Kiraz, `Automatic Concordance Generation of Syriac Texts',
in VI Symposium Syriacum 1992, ed. R. Lavenant, Orientalia
Christiana Analecta 247, Rome, 1994.

## SEDRA 3 License

> You are allowed to use SEDRA III for personal and academic
purposes provided that:
> 1. You do NOT redistribute any altered versions of the files.
> 2. You do NOT redistribute any files for any kind of profit.
> 3. You acknowledge in any publication whose results make use of
>  SEDRA III, by any means, using a formula similar to the
>  following:
> This work makes use of the Syriac Electronic Data
> Retrieval Archive (SEDRA) by George A. Kiraz, distributed
> by the Syriac Computing Institute.

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). Except for the SEDRA 3 data which is covered by the license cited above.
