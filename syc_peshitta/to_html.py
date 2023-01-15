from peshitta import peshitta_section
import sys


def format_word(line):
    ref, word, pointed, lemma, gloss, parse = line.split('\t', maxsplit=5)
    return ref, "<span onclick=\"showWord('" + lemma + "','" + gloss + "','" + parse.strip() + "'" + f')">{pointed}</span>'


HEADER = """<html>
<head>
<meta charset="utf-8">
<meta name="viewport"  content="width=device-width, initial-scale=1">
<!-- @import url(//fonts.googleapis.com/earlyaccess/notosanssyriacestrangela.css); -->
<!-- <link href="//db.onlinewebfonts.com/c/044bb9faf1f2b8000358d5a15419e296?family=Estrangelo+Edessa" rel="stylesheet" type="text/css"/> -->

</head>
<body>
<style>
@import url('https://fonts.googleapis.com/earlyaccess/notosanssyriacestrangela.css');
/*notosanssyriacwestern.css*/

p {
font-size: 1.45em;
}

#data {
position: fixed;
bottom: 0px;
background-color: white;
width:100%;
padding-left:8px;
border: 2px solid black;
font-family: 'Noto Sans Syriac Estrangela', sans-serif;
}
#viewer{
top:0px;
margin-bottom: 150px;
width:100%;
}

#viewer > p {
font-family: 'Noto Sans Syriac Estrangela', sans-serif;
}
</style>
<div id="viewer">"""

FOOTER = """</div>
<div id="data"></div>
<script>
function clearData() {
    var data = document.getElementById('data');
    data.innerHTML = '';
}

function showWord(lemma, parse, gloss){
  var data = document.getElementById('data');
  data.innerHTML = '<h2>' + lemma + "</h2>" + "<p>" + gloss + "</p>" + "<p>" + parse + "</p>";
  data.innerHTML = '<p><span onclick="clearData()">[close]</span></p>' + data.innerHTML;
}

</script>
</body>
</html>"""


def print_section(start, end, title=''):
    cur_verse = ''
    cur_line = []
    print(f"<h1>{title}</h1>")
    for ref, _ , pointed, lemma, gloss, parse in peshitta_section(start, end):
        data = "<span onclick=\"showWord('" + lemma + "','" + gloss + "','" + parse.strip() + "'" + f')">{pointed}</span>'
        if ref[:-2] == cur_verse:
            cur_line.append(data)
        else:
            print(f"<p>{cur_verse} {' '.join(cur_line)}</p>")
            cur_verse = ref[:-2]
            cur_line = [data]
    print(f"<p>{cur_verse} {' '.join(cur_line)}</p>")








print(HEADER)
counter = 0
max = 10
with open('reading_combined.txt', 'r') as f:
    for line in f:
        section, title, start, end = line.strip().split("\t", maxsplit=3)
        print_section(start, end, title)
        counter += 1
        if counter > max:
            break

print(FOOTER)
