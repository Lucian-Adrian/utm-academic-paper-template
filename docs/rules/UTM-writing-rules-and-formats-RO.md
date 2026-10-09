# Reguli și formate UTM pentru rezumat, articol și teză/proiect

Pentru rapoarte se aplică modelul obligatoriu ELSE: margini sus/jos/stânga de 2 cm, dreapta de 1 cm, capitole centrate cu majuscule la 13 pt, cod Courier New 10 pt și numere ascunse pe paginile preliminare. Vezi [regulile pentru rapoarte ELSE](ELSE-report-template.md). Regulile de conferință și licență de mai jos se aplică documentelor respective.

Document consolidat din:

- `Abstract_template-Conf-UTM-2026-rom.docx`;
- `Paper_template-Conf-SMD-UTM-2026-rom.docx`;
- `sustinereTezeLicenta.pdf`;
- verificarea folderelor vechi `UTM Latex Template` și `Thesis_Report_Template_EN`.

Scopul documentului este să ofere o referință practică pentru redactare, verificare și recreare în LaTeX a unui articol academic UTM. Pentru articole se aplică în primul rând modelul `Paper_template-Conf-SMD-UTM-2026-rom.docx`; regulile de teză/proiect se folosesc numai pentru documente de licență sau pentru pagini opționale cerute separat.

## Regula de prioritate

Dacă regulile diferă, se alege tipul documentului înainte de redactare:

- rezumat de conferință: se aplică `Abstract_template-Conf-UTM-2026-rom.docx`;
- articol/lucrare de conferință: se aplică `Paper_template-Conf-SMD-UTM-2026-rom.docx`;
- teză/proiect de licență: se aplică `sustinereTezeLicenta.pdf`;
- cerință mai strictă de la profesor, coordonator, catedră sau comisie: se aplică cerință mai strictă și se notează abaterea față de model.

Nu se combină limită de 12 000 caractere pentru articol cu limită de 60-80 pagini pentru teză.

## Regula profesorului pentru enumerări

La enumerări:

- fraza introductivă se termină cu două puncte;
- fiecare element începe cu literă mică;
- fiecare element se termină cu punct și virgulă;
- ultima intrare păstrează punctul și virgula dacă profesorul a cerut explicit uniformitate;
- regula nu se aplică listei bibliografice numerotate, unde intrările bibliografice se termină conform stilului de referințe.

Exemplu corect:

```text
Contribuțiile principale ale lucrării sunt:
a) elaborarea modelului de analiză;
b) validarea rezultatelor obținute;
c) formularea recomandărilor finale;
```

## Reguli academice generale

- lucrarea trebuie să fie originală;
- toate sursele pentru idei, texte, figuri, tabele, scheme, formule, imagini scanate sau materiale adaptate trebuie citate;
- plagiatul include și preluarea figurilor, tabelelor sau schemelor fără citare;
- autorul răspunde pentru exactitatea și veridicitatea rezultatelor;
- titlul trebuie să fie scurt, precis, fără acronime neconsacrate și inteligibil pentru nespecialiști;
- prescurtările se explică la prima apariție;
- simbolurile și notațiile se explică la prima apariție, dacă nu există lista de notatii;
- stilul trebuie să fie impersonal, fără persoana I;
- limbajul trebuie să fie clar, direct, logic și coerent;
- in română se folosesc diacritice;
- se evită formulările vagi, ambigue și afirmațiile nesusținute.

## Integritate academică și IA generativă

Politica UTM din 2026 interzice folosirea IA generative pentru teme sau evaluări dacă profesorul nu permite clar acest lucru. Utilizarea neautorizată este tratată ca fraudă și/sau plagiat. Dacă disciplina permite folosirea IA, procedura UTM cere declararea explicită a utilizării, iar IA nu poate înlocui contribuția intelectuală a autorului. Respectați formularea și locul declarației stabilite de profesor sau departament. Documentele nu oferă o formulare universală. Verificați personal sursele, afirmațiile, calculele și rezultatele.

## Setări comune pentru modelele de conferință

Pentru rezumat și articol:

- format hârtie: A4;
- orientare: portret;
- margine sus: 2.0 cm;
- margine jos: 2.0 cm;
- margine dreapta: 2.0 cm;
- margine stângă: 2.5 cm;
- distanță antet: 1.0 cm;
- distanță subsol: 1.25 cm;
- font principal: Times New Roman;
- text principal: 12 pt;
- aliniere text principal: justificată.

## Rezumat de conferință

Ordinea elementelor:

1. titlul lucrării;
2. autorii;
3. afilierile;
4. autorul corespondent;
5. îndrumătorul/coordonatorul științific;
6. rezumatul;
7. cuvintele cheie.

Titlul:

- se scrie cu majuscule;
- se centreaza;
- se scrie cu Times New Roman, 14 pt;
- se scrie cu caractere aldine;
- se foloseste spatiere la un rand.

Autorii:

- format: `Prenumele NUMELE`;
- se centreaza;
- Times New Roman, 12 pt;
- aldine;
- fiecare autor are indicator numeric pentru afiliere;
- autorul corespondent se marcheaza cu `*`.

Afilierile:

- includ departament, grupa, facultate, universitate, oras, tara;
- se centreaza;
- 10 pt;
- italic;
- fiecare afiliere începe cu indicatorul numeric corespunzator.

Autorul corespondent:

- începe cu `*Autorul corespondent:`;
- include prenume, nume și e-mail;
- se centreaza;
- 10 pt;
- stil normal.

Indrumatorul/coordonatorul științific:

- include numele, titlul științific și afilierea;
- se centreaza;
- 10 pt;
- eticheta și numele sunt aldine in model.

Rezumatul:

- începe cu `Rezumat.`;
- eticheta este bold italic;
- corpul este italic;
- Times New Roman, 12 pt;
- aliniere justificată;
- lungime aproximativa: jumatate de pagină;
- include scopul cercetării, metodologia, rezultatele principale și concluziile relevante;
- evidentiaza noutatea lucrării;
- evită generalitatile, ambiguitatea și prescurtările neexplicate.

Cuvintele cheie:

- incep cu `Cuvinte cheie:`;
- eticheta este bold italic;
- corpul este italic;
- Times New Roman, 12 pt;
- aliniere justificată;
- intre 4 și 6 cuvinte cheie;
- litere mici;
- separate prin virgule;
- evită repetarea termenilor din titlu.

## Articol/lucrare de conferință

Structura normala:

1. titlu;
2. autori;
3. afilieri;
4. autor corespondent;
5. indrumator/coordonator științific;
6. rezumat;
7. cuvinte cheie;
8. introducere și formularea problemei;
9. parte experimentala sau metodologica;
10. rezultate și discutii;
11. concluzii;
12. mulțumiri, dacă este cazul;
13. referințe;
14. declarație de originalitate și asumare a responsabilității.

Limite:

- articolul are maximum 12 000 caractere cu spatii;
- rezumatul are 150-200 cuvinte;
- in rezumat nu se introduc citări bibliografice.

Textul principal:

- Times New Roman;
- 12 pt;
- justificat;
- paragrafele noi trebuie să fie vizibile;
- se foloseste numerotarea automata a paginilor.

Sectiunile:

- titlurile din model sunt Times New Roman, 12 pt, aldine;
- se folosesc titluri scurte și paralele;
- secțiuni tipice: `Introducere`, parte metodologica/experimentala, `Rezultate și discuții`, `Concluzii`, `Mulțumiri`, `Referințe`.

Cerinte științifice:

- lucrarile originale și comunicarile scurte trebuie să contina constatari originale;
- detaliile trebuie să permita reproducerea experimentelor;
- articolele de sinteza trebuie să ofere informatie noua și unificare de idei, nu doar rezumate ale lucrarilor anterioare.

Tabele:

- se centreaza;
- trebuie să ocupe toata latimea paginii, cand este posibil;
- dacă se continuă pe pagină urmatoare, se marcheaza continuarea și se repeta rubricile;
- textul din tabel: 10 pt, spatiere la un rand;
- antetele coloanelor sunt explicative, aldine și includ unitati de masura unde este cazul;
- se numeroteaza in ordinea aparitiei: `Tabelul 1`, `Tabelul 2`;
- se citeaza in text ca `Tab. 1`, `Tab. 2`;
- titlul tabelului apare deasupra tabelului;
- titlul tabelului este 11 pt și aldine.

Figuri:

- se centreaza;
- se plaseaza cat mai aproape de prima mentiune in text;
- se numeroteaza in ordinea aparitiei: `Figura 1`, `Figura 2`;
- se citeaza in text ca `Fig. 1`, `Fig. 2`;
- au legenda scurta și exacta;
- legenda începe cu `Figura` și numarul, cu caractere aldine;
- legenda se centreaza;
- legenda are 11 pt;
- imaginile trebuie să aiba rezolutie buna, fără fișiere disproportionat de mari.

Ecuatii și formule:

- se foloseste Equation Editor, MathType sau echivalent LaTeX corect;
- ecuațiile se centreaza;
- se numeroteaza consecutiv cu cifre arabe in paranteze rotunde;
- numarul se plaseaza la marginea dreapta;
- in text se citeaza ca `Ec. (1)`, `Ec. (2)`.

Simboluri, notatii și unitati:

- simbolurile se scriu italic, 12 pt;
- vectorii se scriu aldine;
- functiile standard, precum `log`, `ln`, `exp`, se scriu cu font normal;
- se folosesc simboluri internationale acceptate;
- se recomanda unitatile SI;
- pentru litru se foloseste `L` mare;
- pentru kilogram se foloseste `k`, nu `K`;
- numerele zecimale se scriu cu punct, nu cu virgulă;
- formulele și schemele mari se prezinta ca figuri.

Referințe:

- in text se folosesc numere arabe in paranteze pătrate;
- referintele se numeroteaza in ordinea citarii;
- citarea se plaseaza inaintea semnului de punctuație;
- forme acceptate: `[1]`, `[1-4]`, `[1,3]`;
- toate referintele citate trebuie să existe in lista și invers;
- numele complet al revistei se scrie integral, fără abrevieri;
- lista de referințe este Times New Roman, 12 pt;
- se recomanda Zotero, EndNote, Mendeley sau ReferenceManager.

Modele de referințe:

```text
1. AUTOR 1, A.B.; AUTOR 2, C.D. Titlul lucrării. Numele revistei Anul, Volumul, pp. 154-196, doi:
2. AUTOR 1, A.; AUTOR 2, B. Titlul cartii, 3rd ed.; Editura: Locatia editurii, Tara, An; pp. 154-196.
3. AUTOR 1, A.B. Titlul tezei. Nivelul tezei, Universitatea, Localitatea, Data sustinerii.
4. Titlul site-ului. Disponibil online: URL (accesat la data de Ziua Luna Anul).
```

Declaratia:

- se include la final pentru articolul din model;
- autorul corespondent declara originalitatea lucrării;
- se confirma citarea corecta a tuturor surselor;
- se include nume/prenume, semnatura și data.

## Teza/proiect de licență

Pentru formatare, folosiți fișierul de curs FCIM `PAPER FORMATTING GUIDELINES.pdf` și pagina ELSE `Reguli de redactare`. Ghidul UTM pentru elaborarea tezelor de licență, publicat pe pagina instituțională în 2019, stabilește structura și succesiunea componentelor. Cerințele mai stricte ale departamentului sau coordonatorului au prioritate.

Volum și proportii:

- memoriu explicativ: se recomandă 50-80 pagini fără anexe; departamentul stabilește limita exactă;
- partea teoretică: aproximativ 30-40% și nu peste 40%;
- partea aplicativa/practică: aproximativ 60-70%;
- figurile și graficele nu depasesc 30% din volum.

Structura:

1. coperta;
2. pagină de titlu;
3. sarcina/caietul de sarcini;
4. pagină de dedicatii și mulțumiri, optional;
5. declarația studentului;
6. avizul coordonatorului, completat de coordonator;
7. rezumatul;
8. cuprinsul;
9. lista tabelelor, optional;
10. lista figurilor/graficelor/diagramelor/schemelor, optional;
11. lista abrevierilor, necesară dacă lucrarea folosește abrevieri sau termeni din afara limbii de instruire;
12. introducerea;
13. conținutul pe capitole;
14. concluziile;
15. bibliografia;
16. anexele, dacă este cazul.

Redactare:

- limba acceptată: română, engleză, franceză sau rusă;
- A4, Times New Roman 12 pt, negru, aliniere justify, spațiere 1,5 și alineat inițial de 1,25 cm;
- margini: sus, jos și stânga 2 cm; dreapta 1 cm;
- teza se tipărește pe o singură față;
- capitolele încep pe pagină nouă, cu majuscule, aldine, centrate, 13 pt;
- subcapitolele folosesc font aldin de 12 pt, aliniere la stânga și alineat de 1,25 cm;
- Introducerea și Concluziile nu se numerotează; capitolele și subcapitolele folosesc cifre arabe, până la trei niveluri;
- paginile preliminare se numără, dar nu afișează numărul; numerotarea centrată jos începe la Introducere și nu se resetează;
- codul sursă folosește Courier New 10 pt, spațiere simplă; codul care depășește jumătate de pagină se mută într-o anexă și se citează în text;
- simbolurile din formule se explică sub formulă; fiecare formulă, figură și tabel se citează înainte de apariție;
- figurile și tabelele care ocupă peste 75% din pagină se mută în anexă; elementele peisaj se plasează în anexe;
- fiecare anexă începe pe pagină nouă, cu titlul centrat sub eticheta `Anexa A`.

Rezumatul tezei:

- prezinta ideile principale, rezultatele și concluziile;
- include numarul de capitole, pagini, figuri, tabele și surse bibliografice;
- fiecare versiune necesară are 300-500 de cuvinte și până la cinci cuvinte-cheie pe un rând separat;
- includeți versiuni în română și într-o limbă internațională; dacă teza este scrisă în altă limbă, adăugați și adnotarea în limba originală, conform ghidului UTM.

Bibliografia tezei:

- contine toate sursele utilizate;
- poate include carti, monografii, lucrari de conferință, articole, teze, rapoarte, standarde, norme, ghiduri, pagini web și rapoarte interne;
- bibliografia se pregătește în Zotero cu stilul IEEE;
- citările sunt numerice, în ordinea primei apariții, între paranteze pătrate, de exemplu `[1]` și `[8, p. 231]`;
- anul se scrie cu cifre arabe;
- dacă sunt mai mult de trei autori, se poate folosi `et. al.` după autorii indicati.

Pagina de titlu se prezintă în limba tezei și în română dacă teza este scrisă în altă limbă. Declarația studentului se scrie de mână în exemplarul final. Caietul de sarcini aprobat și avizul coordonatorului trebuie să vină de la departament și coordonator; nu recreați aprobări sau semnături.

IA generativă poate fi utilizată numai dacă profesorul permite clar acest lucru. Dacă este permisă, declarați explicit utilizarea conform cerințelor disciplinei și păstrați contribuția intelectuală proprie. Regulile nu oferă un model universal de declarație.

Sustinerea:

- durata prezentarii: pana la 10-15 minute;
- se prezinta tema, scopul, sarcinile, variantele de solutionare, rezultatele, argumentarea, calculele tehnico-economice, masurile de securitate/protectie și concluziile;
- afirmațiile importante trebuie sustinute prin date, grafice, diagrame, tabele, scheme, formule, simulari sau rezultate software;
- raspunsurile la intrebari trebuie să fie scurte, clare și directe;
- cu o saptamana înainte se recomanda mai multe sustineri preliminare.

## LaTeX recomandat pentru articol

Template-ul modern creat in acest repo este:

- `templates/article/utmconf.cls`;
- `templates/article/main.tex`;
- `tools/check.py`;
- `templates/article/titlepage-demo.tex`, doar pentru pagină de titlu UTM optionala.

Reguli LaTeX:

- pentru articolul de conferință se foloseste `utmconf.cls`;
- logo-ul UTM este inclus ca `utm-logo.png`, dar nu este activ implicit deoarece modelul oficial de articol nu cere logo;
- dacă profesorul cere antet cu logo, se activeaza `\UTMShowLogotrue`;
- pentru diacritice se compilează cu Tectonic/XeTeX și Times New Roman;
- rezumatul se scrie in mediul `rezumat`;
- cuvintele cheie se scriu cu `\cuvintecheie{...}`;
- tabelele se eticheteaza cu `\utmtablecaption{...}`;
- figurile se eticheteaza cu `\utmfigurecaption{...}`;
- enumerarile de conținut folosesc mediul `utmenumerate` și fiecare `\item` se termină cu punct și virgulă.

Comenzi de verificare:

```powershell
python tools\check.py
cd templates\article
tectonic main.tex
tectonic titlepage-demo.tex
```

## Checklist final

- tipul documentului este ales corect;
- structura corespunde tipului documentului;
- formatul paginii și marginile sunt corecte;
- fontul, dimensiunea și alinierea sunt corecte;
- rezumatul respecta lungimea ceruta;
- cuvintele cheie sunt 4-6, cu litere mici, separate prin virgule;
- enumerarile respecta regula profesorului;
- tabelele, figurile și ecuațiile sunt numerotate și citate in text;
- referintele sunt citate in text și apar in lista;
- nu există citări in rezumatul articolului;
- toate materialele preluate sunt citate;
- textul romanesc are diacritice;
- declarația este inclusa cand modelul o cere.

