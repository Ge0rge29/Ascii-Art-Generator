# Generarea de Arta ASCII prin Algoritmi Genetici

Acest proiect isi propune sa exploreze o abordare evolutiva pentru conversia imaginilor in arta ASCII, utilizand un algoritm genetic. Proiectul este implementat in limbajul Python si foloseste biblioteci standard pentru procesare de imagini, manipulare numerica si vizualizare.

## Descriere generala

Arta ASCII presupune reprezentarea unei imagini folosind doar caractere text, fiecare caracter corespunzand unui anumit nivel de luminozitate. In mod traditional, aceasta conversie este realizata prin maparea directa a valorilor de intensitate ale pixelilor la caracterele ASCII corespunzatoare. In acest proiect, insa, se exploreaza o alternativa evolutiva, in care imaginea ASCII este generata printr-un proces de optimizare iterativa inspirat din evolutia naturala.

Imaginea initiala este convertita intr-o versiune grayscale si redimensionata pentru a reduce complexitatea. Fiecare individ din populatie reprezinta o varianta posibila a acelei imagini, construita ca o matrice de caractere ASCII selectate aleator. Scopul algoritmului genetic este de a evolua o astfel de populatie pana cand unul dintre indivizi reproduce cat mai fidel distributia de ton a imaginii sursa.

## Algoritmul genetic

Procesul evolutiv este compus din urmatoarele etape fundamentale:

- **Initializare**: Se genereaza o populatie de indivizi (imagini ASCII) aleatori.
- **Evaluare (fitness)**: Fiecare individ este evaluat printr-o functie de fitness care compara valorile de luminozitate ale caracterelor ASCII cu valorile corespunzatoare ale pixelilor din imaginea grayscale.
- **Selectie**: Se aplica selectia prin turneu, o metoda care favorizeaza indivizii mai buni fara a elimina complet diversitatea populatiei.
- **Crossover**: Se implementeaza un mecanism de incrucisare care combina indivizi parinti pentru a produce descendenti, prin schimb de sectiuni orizontale ale matricelor.
- **Mutatie**: Pentru a mentine variatia genetica, fiecare caracter are o probabilitate definita de a fi inlocuit cu altul aleatoriu.

Procesul se repeta pentru un numar definit de generatii, iar evolutia valorilor de fitness este urmarita si salvata sub forma de grafic.

## Implementare tehnica

Proiectul este implementat in Python, folosind urmatoarele biblioteci:

- `Pillow (PIL)` pentru incarcarea si prelucrarea imaginilor.
- `NumPy` pentru reprezentarea eficienta a matricelor si vectorilor.
- `Matplotlib` pentru generarea graficului evolutiei fitness-ului.

Imaginea de intrare este asteptata intr-un fisier numit `input.png`, iar setul de caractere ASCII utilizat este citit din `ascii_chars.txt`, un fisier text care trebuie sa contina caracterele dorite, ordonate crescator dupa intensitate vizuala (de la cele mai "inchise" la cele mai "deschise").

Dupa executia programului, rezultatul final — imaginea ASCII considerata cea mai apropiata de original din punct de vedere vizual — este salvat intr-un fisier `.txt`, iar graficul progresului algoritmului este exportat ca imagine `.png`.

## Rezultate si observatii

Algoritmul reuseste sa genereze in mod eficient solutii vizual consistente, capabile sa redea structura imaginii initiale intr-o forma simbolica expresiva. Evolutia acestora este usor de urmarit datorita graficelor generate, care reflecta progresul algoritmic de la o generatie la alta. 

![fitness_evolution](https://github.com/user-attachments/assets/1828fa4e-4040-48a8-8076-d1e2c5c0607d)

Performanta sistemului depinde in mod direct de dimensiunea imaginii de intrare, de setul de caractere ASCII utilizat si de parametrii genetici alesi: marimea populatiei, numarul de generatii, rata de mutatie si probabilitatea de crossover. Cu setari corespunzatoare, algoritmul poate genera rezultate surprinzator de expresive, chiar si pentru imagini complexe.

Algoritmul poate fi extins in viitor pentru a lucra si cu imagini color, fie prin procesarea separata a canalelor RGB, fie prin utilizarea de caractere colorate in terminale moderne sau in fisiere HTML.

## Concluzii

Proiectul demonstreaza aplicabilitatea tehnicilor evolutive in domeniul procesarii imaginilor si este capabil sa genereze rezultate intr-un mod complet automatizat si adaptiv. Totodata, subliniaza valoarea algoritmilor genetici ca instrumente creative, nu doar ca metode de cautare sau rezolvare a problemelor traditionale.
