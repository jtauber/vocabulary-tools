from peshitta import *

forms_ps = open("analysis/pericope_form_db.txt", 'w', encoding="UTF-8")
lemmas_ps = open("analysis/pericope_lemma_db.txt", 'w', encoding="UTF-8")
combined_ps = open("analysis/pericope_combined_db.txt", 'w', encoding="UTF-8")
for num, start, end, title in peshitta_pericopes():
    forms = []
    lemmas = []
    combined = []
    for ref, word, pointed, lemma, gloss, parse in peshitta_section(start, end):
        forms.append(pointed)
        lemmas.append(lemma)
        combined.append(pointed)
        combined.append(parse)
    forms_ps.write(f"{num}\t {' '.join(set(forms))}\n")
    lemmas_ps.write(f"{num}\t {' '.join(set(lemmas))}\n")
    combined_ps.write(f"{num}\t {' '.join(set(combined))}\n")

forms_ps.close()
lemmas_ps.close()
combined_ps.close()

print("Done")
