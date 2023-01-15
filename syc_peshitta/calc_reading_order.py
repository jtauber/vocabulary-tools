from ordering import next_best
from peshitta import get_peshitta_pericopes_dir





def calc_path(fname, oname, name_map):
    pericope_map = {}
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            key, vals = line.split("\t", maxsplit=1)
            pericope_map[key] = vals
    with open(oname, 'w', encoding="UTF-8") as f:
        for section, _ in next_best(pericope_map):
            start, end, title = name_map[section]
            f.write(f"{section}\t{title}\t{start}\t{end}\n")

name_map = get_peshitta_pericopes_dir()
print("Calcing combined")
calc_path('analysis/pericope_combined_db.txt', 'reading_orders/reading_combined.txt', name_map)

print("calcing lemmas")
calc_path('analysis/pericope_lemma_db.txt', 'reading_orders/reading_lemmas.txt', name_map)

print("calcing forms")
calc_path('analysis/pericope_form_db.txt', 'reading_orders/reading_forms.txt', name_map)

print("Done")
