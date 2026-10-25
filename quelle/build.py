import json,glob,re,sys
# Baut ../index.html neu aus den Kapitel-Dateien in kapitel/. Aufruf: cd quelle && python3 build.py
src=open("../index.html").read()
chs=[json.load(open(f)) for f in sorted(glob.glob('kapitel/k*.json'))]
chs.sort(key=lambda c:c['nr'])
for c in chs:
    c.setdefault('teil','')
data=json.dumps(chs,ensure_ascii=False).replace('</','<\\/')
m=re.search(r'(<script type="application/json" id="data">)(.*?)(</script>)',src,re.S)
out=src[:m.start(2)]+data+src[m.end(2):]
reps=[
('<title>Spanisch-Grammatik</title>','<title>Französisch-Grammatik</title>'),
('ein Schulheft ("cuaderno")','ein Schulheft ("cahier")'),
('--blue:#0d6a5f; --blue-soft:#e2f2ef; --red:#c8323a; --red-soft:#fbe9ea;','--blue:#1f4fa8; --blue-soft:#e6edfa; --red:#c8323a; --red-soft:#fbe9ea;'),
("esgr-progress","frgr-progress"),("esgr-last","frgr-last"),
('top.innerHTML=`<div class="t">Spanisch-Grammatik</div>`','top.innerHTML=`<div class="t">Französisch-Grammatik</div>`'),
('<h1>Gramática española</h1>','<h1>Grammaire française</h1>'),
('Merkblätter, Übungen und Lernkarten zu allen Kapiteln der spanischen Grammatik, von der Aussprache bis zum subjuntivo. Antippen, lernen, prüfen.','Merkblätter, Übungen und Lernkarten zu allen Kapiteln der französischen Grammatik, von der Aussprache bis zum subjonctif. Antippen, lernen, prüfen.'),
('placeholder="Suchen, z. B. por, subjuntivo, Uhrzeit"','placeholder="Suchen, z. B. en, subjonctif, Uhrzeit"'),
('¡Muy bien!','Très bien !'),
]
for a,b in reps:
    n=out.count(a)
    if n==0: continue
    out=out.replace(a,b)
# dark blue
out=out.replace('--blue:#6fd6c4; --blue-soft:#15302c;','--blue:#8fb3ff; --blue-soft:#1a2640;')
open("../index.html","w").write(out)
print(len(chs),'chapters',len(out)//1024,'KB')
