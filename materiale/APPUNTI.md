# Appunti Python — Progetti 42

Ogni esercizio è raccontato **nell'ordine in cui si esegue il codice**: si parte dal main (o dalla chiamata) e si segue il flusso passo per passo. Poi codice, poi teoria.

---

# p00 — Growing Code (Fondamenta Python)

## ex0 — ft_hello_garden — la prima funzione

**Cosa fa in concreto:** stampa la scritta "Hello, Garden Community!" sullo schermo. Niente input, niente calcoli: una stampa e fine.

**★ PRIME VOLTE qui:** `print()`, `def` (la prima funzione)

**Cosa chiede:** funzione `ft_hello_garden()` che stampa `Hello, Garden Community!`.

**Esecuzione:** l'evaluator importa la funzione e la chiama → `ft_hello_garden()` → entra nel corpo → `print("Hello, Garden Community!")` → stampa → la funzione finisce. Fine.

**Codice:**
```python
def ft_hello_garden():
	print("Hello, Garden Community!")
```

**Teoria:**
- `print()` = il printf di Python. Va a capo da solo, non serve `\n`
- Il testo va SEMPRE tra virgolette: `print(Hello)` senza virgolette → SyntaxError
- In Python non serve `main()`: il file si esegue dall'alto in basso

## ex1 — ft_garden_name — input

**Cosa fa in concreto:** chiede all'utente di scrivere il nome del giardino, poi stampa tre righe: il nome ricevuto e due messaggi fissi.

**★ PRIME VOLTE qui:** `input()`

**Cosa chiede:** chiedere il nome del giardino e stamparlo con un messaggio fisso.

**Esecuzione:** chiamata `ft_garden_name()` → riga 1: `input()` stampa la domanda e ASPETTA l'utente → l'utente scrive "Community Garden" → il valore finisce in `name` → riga 2: `print("Garden: " + name)` concatena e stampa → riga 3: stampa "Status: Growing well!" → fine.

**Codice:**
```python
def ft_garden_name():
	name = input("Enter garden name: ")
	print("Garden: " + name)
	print("Status: Growing well!")
```

**Teoria:**
- `input("domanda")` stampa la domanda, aspetta l'utente, restituisce SEMPRE una stringa
- `+` tra stringhe = concatenazione. `+` tra stringa e numero = TypeError

## ex2 — ft_plot_area — int() e f-string

**Cosa fa in concreto:** chiede due numeri (lunghezza e larghezza), li moltiplica tra loro e stampa il prodotto. Tutto qui: niente area reale da disegnare — solo una moltiplicazione.

**★ PRIME VOLTE qui:** `int()` (conversione), f-string

**Cosa chiede:** chiedere lunghezza e larghezza, stampare l'area (prodotto).

**Esecuzione:** chiamata `ft_plot_area()` → riga 1: input → l'utente scrive "5" (stringa!) → `int("5")` la converte in numero 5 → salvato in `length` → riga 2: stesso per width=3 → riga 3: `print(f"Plot area: {length * width}")` calcola 5*3=15 e stampa → fine.

**Codice:**
```python
def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	print(f"Plot area: {length * width}")
```

**Teoria:**
- `input()` dà una stringa anche se scrivi un numero → serve `int()` per calcolare
- `int(x)` RESTITUISCE il valore convertito, non modifica x: serve `x = int(x)`
- f-string: `f"testo {variabile}"` — le graffe vengono sostituite col valore. È il `printf("%d", x)` di Python
- `print("a", 5)` con la virgola stampa `a 5` — accetta tipi misti (il `+` no)

## ex3 — ft_harvest_total — somma di 3 input

**Cosa fa in concreto:** chiede tre numeri (i raccolti di tre giorni), li somma e stampa il totale.

**★ NIENTE di nuovo:** consolidamento di ex2

**Cosa chiede:** 3 input numerici, stampare la somma.

**Esecuzione:** chiamata → 3 volte: input → int() → salva in day1, day2, day3 → print della somma → fine.

**Codice:**
```python
def ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	print(f"Total harvest: {day1 + day2 + day3}")
```

## ex4 — ft_plant_age — if/else

**Cosa fa in concreto:** chiede un numero (l'età della pianta in giorni) e stampa UNA delle due frasi: sopra 60 "ready to harvest", altrimenti "needs more time".

**★ PRIME VOLTE qui:** `if`/`else` (condizionali in Python)

**Cosa chiede:** se l'età > 60 stampa "ready to harvest", altrimenti "needs more time".

**Esecuzione:** chiamata → input "75" → `int()` → 75 in `age` → `if age > 60:` → 75 > 60 è VERO → si entra nel blocco if → stampa "Plant is ready to harvest!" → l'else viene SALTATO → fine. (Con "45": 45 > 60 è FALSO → si salta l'if → si entra nell'else → stampa "needs more time".)

**Codice:**
```python
def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
```

**Teoria:**
- Niente parentesi tonde: `if age > 60:` non `if (age > 60)`
- Niente graffe: il blocco è l'INDENTAZIONE (tab)
- DUE PUNTI dopo la condizione e dopo `else`
- `elif` = il `else if` del C

## ex5 — ft_water_reminder — if/else bis

**Cosa fa in concreto:** chiede un numero (giorni dall'ultima annaffiatura) e stampa UNA delle due frasi: sopra 2 "Water the plants!", altrimenti "Plants are fine".

**★ NIENTE di nuovo:** consolidamento di ex4

**Cosa chiede:** se i giorni > 2 stampa "Water the plants!", altrimenti "Plants are fine".

**Esecuzione:** identica a ex4: input → int → confronto → un ramo solo dei due viene eseguito.

**Attenzione:** il subject scrive `Plants are fine` SENZA punto esclamativo.

## ex6 — ft_count_harvest — for e ricorsione

**Cosa fa in concreto:** chiede un numero N e stampa un conteggio da "Day 1" a "Day N", poi "Harvest time!" — in DUE versioni: una col ciclo for, una con la ricorsione.

**★ PRIME VOLTE qui:** `for`, `range()`, ricorsione con funzione helper

**Cosa chiede:** due funzioni (iterativa e ricorsiva) che contano da 1 a N e stampano "Harvest time!".

### Iterativa — esecuzione con N=5:
1. Chiamata → input "5" → `days = 5`
2. `range(1, 6)` genera la sequenza 1, 2, 3, 4, 5
3. Giro 1: `i = 1` → stampa "Day 1" → torna su
4. Giro 2: `i = 2` → "Day 2" → ... fino a "Day 5"
5. Il loop finisce → scende sotto → stampa "Harvest time!" → fine

```python
def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print(f"Day {i}")
	print("Harvest time!")
```

### Ricorsiva — esecuzione con N=5:
1. Chiamata → input "5" → `print_days(1, 5)`
2. `print_days(1, 5)`: 1 > 5? NO → stampa "Day 1" → chiama `print_days(2, 5)`
3. `print_days(2, 5)`: 2 > 5? NO → stampa "Day 2" → chiama `print_days(3, 5)`
4. ... fino a `print_days(6, 5)`: 6 > 5? SÌ → stampa "Harvest time!" → risale e tutti finiscono

```python
def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	print_days(1, days)

def print_days(day, total):
	if day > total:
		print("Harvest time!")
	else:
		print(f"Day {day}")
		print_days(day + 1, total)
```

**Teoria:**
- `range(1, days + 1)` genera 1, 2, ..., days (l'ultimo ESCLUSO, per questo il +1)
- `for i in range(...)` = "per ogni numero della sequenza". È un foreach, NON il for del C: niente `i++`
- Ricorsione: la funzione esterna legge l'input UNA volta sola, poi la ricorsione lavora sui numeri. Si conta in AVANTI (1 → N) e si stampa PRIMA della chiamata ricorsiva, così "Harvest time!" esce per ultimo

## ex7 — ft_seed_inventory — type hints

**Cosa fa in concreto:** riceve tre valori (nome del seme, quantità, unità di misura) e stampa una frase diversa a seconda dell'unità: "packets", "grams", "area", o "Unknown unit type" per tutto il resto. Il nome viene stampato con la prima lettera maiuscola.

**★ PRIME VOLTE qui:** type hints, `elif`, `.capitalize()`

**Cosa chiede:** funzione con firma OBBLIGATA `def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:` che stampa in base all'unità ("packets", "grams", "area", altro → "Unknown unit type"). Nome del seme con la maiuscola.

**Esecuzione:** l'evaluator chiama `ft_seed_inventory("tomato", 15, "packets")` → i 3 valori entrano nei parametri → riga 1: `"tomato".capitalize()` → `"Tomato"` in `name` → la catena if/elif: `unit == "packets"`? SÌ → stampa "Tomato seeds: 15 packets available" → fine. (Con "liters": nessun if scatta → else → "Unknown unit type".)

**Codice:**
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	name = seed_type.capitalize()
	if unit == "packets":
		print(f"{name} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{name} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{name} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
```

**Teoria:**
- Type hints = etichette informative: `: str`, `: int`, `-> None` (= void). Non bloccano niente a runtime, mypy le controlla
- `"tomato".capitalize()` → `"Tomato"` — metodo delle stringhe
- La funzione riceve i parametri dall'esterno — NON usa input()

---

# p01 — Code Cultivation (OOP)

## ex0 — ft_garden_intro — il main di Python

**Cosa fa in concreto:** stampa un blocco di testo fisso: tre dati su una pianta (nome, altezza, età) tra due righe di intestazione. Nessun input: tutto è scritto nel codice.

**★ PRIME VOLTE qui:** `if __name__ == "__main__":`

**Cosa chiede:** primo programma completo con variabili e print, eseguito direttamente.

**Esecuzione:** `python3 ft_garden_intro.py` → Python legge il file dall'alto → riga `if __name__ == "__main__":` → il file è stato eseguito direttamente, quindi `__name__` vale `"__main__"` → la condizione è VERA → si esegue il blocco: 3 assegnazioni (name, height, age) → 5 print in ordine → fine.

**Codice:**
```python
if __name__ == "__main__":
	name = "Rose"
	height = "25cm"
	age = "30 days"
	print("=== Welcome to My Garden ===")
	print(f"Plant: {name}")
	print(f"Height: {height}")
	print(f"Age: {age}")
	print("=== End of Program ===")
```

**Teoria:**
- Python esegue il file riga per riga — non esiste main() come in C
- `__name__` è un'etichetta automatica: vale `"__main__"` se esegui il file direttamente, altrimenti vale il nome del modulo
- Il blocco `if __name__ == "__main__":` gira SOLO se il file è eseguito direttamente, NON se viene importato
- Doppio underscore = "dunder", nomi riservati di Python
- Non è una protezione: è un interruttore "eseguito direttamente o importato?"

## ex1 — ft_garden_data — la prima classe

**Cosa fa in concreto:** crea 3 "schede pianta" (oggetti) ognuna con nome, altezza ed età, e le stampa una per una con un metodo. Nessun input: i dati sono scritti nel main.

**★ PRIME VOLTE qui:** `class`, oggetto, `__init__`, `self`, metodo, attributo

**Cosa chiede:** classe `Plant` con attributi name/height/age e metodo `show()`. Creare 3 piante e mostrarle.

**Esecuzione — dall'inizio alla fine:**
1. Si esegue il file → `if __name__ == "__main__":` è vero → si entra nel main
2. `rose = Plant("Rose", 25, 30)` → Python crea una scatola vuota e chiama `__init__` con self=scatola, name="Rose", height=25, age=30
3. Dentro `__init__`: i 3 valori vengono incollati nella scatola (`self.name = name`, ecc.). Il costruttore finisce, la scatola pronta viene restituita e salvata in `rose`
4. Stessa cosa per `sunflower` e `cactus`
5. `print("=== Garden Plant Registry ===")`
6. `rose.show()` → Python cerca `show` nella classe di rose → la trova → la esegue con self=rose → dentro: `print(f"{self.name}: ...")` → self.name è "Rose" → stampa la riga della rosa
7. `sunflower.show()` → stessa cosa con i dati del girasole
8. `cactus.show()` → idem → fine

**Codice:**
```python
class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age_days = age

	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)
	print("=== Garden Plant Registry ===")
	rose.show()
	sunflower.show()
	cactus.show()
```

**Teoria:**
- **Classe** = il progetto (la struct del C + funzioni dentro). **Oggetto** = la cosa concreta (la variabile)
- Analogia giardino: classe = specie "Rosa" (concetto); oggetto = la rosa concreta nel vaso
- **`__init__`** = il costruttore: gira da solo quando crei l'oggetto, inizializza i dati
- **`self`** = l'oggetto stesso ("io, questa pianta qui"). Come `p` in `p->name`
- **`self.name = name`** = incolla il valore del parametro NELL'oggetto. Il parametro muore alla fine, l'attributo vive
- **Metodo** = funzione che vive nella classe e riceve self automaticamente. `rose.show()` = "prendi rose, esegui la SUA show"
- REGOLA: attributo e metodo NON possono avere lo stesso nome (l'attributo vince → TypeError: not callable)

## ex2 — ft_plant_growth — metodi che modificano

**Cosa fa in concreto:** simula una settimana di vita di una pianta: per 7 giorni la fa crescere di 0.8cm e invecchiare di 1 giorno, stampando la scheda dopo ogni giorno e la crescita totale alla fine.

**★ PRIME VOLTE qui:** `round()`

**Cosa chiede:** metodi `grow()` e `age()` che modificano la pianta. Simulare una settimana.

**Esecuzione:**
1. Main: `rose = Plant("Rose", 25, 30)` → costruttore come ex1
2. `rose.show()` → stampa "Rose: 25cm, 30 days old"
3. Loop: giro 1 → `rose.grow()` → dentro grow: `self.height = round(25 + 0.8, 1)` → self.height diventa 25.8 → il dato è cambiato DENTRO la rosa per sempre
4. `rose.age()` → `self.age_days += 1` → 31
5. `rose.show()` → stampa "Rose: 25.8cm, 31 days old"
6. ... per 7 giri → alla fine "Growth this week: 5.6cm"

```python
class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age_days = age

	def grow(self):
		self.height = round(self.height + 0.8, 1)

	def age(self):
		self.age_days += 1

	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")
```

**Teoria:**
- `self.height = ...` modifica il dato DENTRO l'oggetto — permanente. Una variabile locale `height = ...` morirebbe a fine funzione senza cambiare niente
- Un metodo che modifica l'oggetto DEVE avere `self` come primo parametro
- `round(x, 1)` = arrotonda a 1 decimale (l'equivalente di `%.1f`). Necessario perché i float sono imprecisi: 0.8+0.8 può dare 1.6000000000001

## ex3 — ft_plant_factory — lista di oggetti

**Cosa fa in concreto:** crea 5 schede pianta con dati diversi, le mette in una lista e le stampa tutte in sequenza con un ciclo for.

**★ PRIME VOLTE qui:** lista di oggetti, `end=" "`

**Cosa chiede:** creare 5 piante con caratteristiche diverse e mostrarle tutte.

**Esecuzione:**
1. Main → `plants = [...]` crea la lista e, per ogni elemento, chiama il costruttore → 5 oggetti dentro la lista
2. `print("=== Plant Factory Output ===")`
3. Loop `for p in plants:` → giro 1: `p` = la rosa → `print("Created:", end=" ")` (resta sulla riga) → `p.show()` stampa i dati della rosa sulla stessa riga
4. Giro 2: `p` = la quercia → idem ... fino al quinto

```python
if __name__ == "__main__":
	plants = [
		Plant("Rose", 25.0, 30),
		Plant("Oak", 200.0, 365),
		Plant("Cactus", 5.0, 90),
		Plant("Sunflower", 80.0, 45),
		Plant("Fern", 15.0, 120),
	]
	print("=== Plant Factory Output ===")
	for p in plants:
		print("Created:", end=" ")
		p.show()
```

**Teoria:**
- `[...]` crea una lista (l'array di Python). Può contenere oggetti
- `for p in plants:` — a ogni giro `p` È una pianta diversa della lista (non l'indice, l'ELEMENTO). Come `for i in C` ma senza `plants[i]`
- `print("Created:", end=" ")` — `end` sostituisce il "vai a capo" di default: la riga continua
- `25.0` invece di `25` → il valore è float e si stampa con il decimale

## ex4 — ft_garden_security — incapsulamento

**Cosa fa in concreto:** simula un sistema di sicurezza sui dati della pianta: i metodi set_height/set_age RIFIUTANO i valori negativi (stampano l'errore e non cambiano niente), mentre accettano quelli validi. Alla fine mostra lo stato della pianta.

**★ PRIME VOLTE qui:** incapsulamento con `_`, getter/setter, `return`

**Cosa chiede:** proteggere i dati: attributi con underscore, getter, setter con validazione (niente valori negativi).

**Esecuzione:**
1. Main: `rose = Plant("Rose", 15.0, 10)` → costruttore: `self._height = 15.0`, `self._age_days = 10`
2. `rose.show()` → stampa la pianta
3. `rose.set_height(25)` → dentro il setter: `25 < 0`? NO → `self._height = 25` → salvato. "Height updated: 25cm"
4. `rose.set_age(30)` → idem → 30
5. `rose.set_height(-5)` → dentro il setter: `-5 < 0`? SÌ → stampa l'errore → NON salva → la pianta resta a 25
6. `rose.set_age(-10)` → idem, rifiutato
7. `rose.show()` → "Current state: Rose: 25.0cm, 30 days old" — i tentativi negativi non hanno cambiato niente

```python
class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self._height = height
		self._age_days = age

	def get_height(self):
		return self._height

	def get_age(self):
		return self._age_days

	def set_height(self, new_height):
		if new_height < 0:
			print(f"{self.name}: Error, height can't be negative")
		else:
			self._height = new_height

	def set_age(self, new_age):
		if new_age < 0:
			print(f"{self.name}: Error, age can't be negative")
		else:
			self._age_days = new_age
```

**Teoria:**
- **`_` davanti** = post-it "privato, non toccare direttamente". NON blocca nulla (rose._height = -999 funziona), è un segnale per gli umani. Il lucchetto vero è il setter
- **Getter** = sportello di lettura: `return self._height` restituisce il valore
- **Setter** = sportello di scrittura CON controllo: valuta prima di salvare. Valore invalido → messaggio d'errore, dato INTATTO
- Perché `_age_days` e non `age`: c'è il metodo `age()` — attributo e metodo non possono avere lo stesso nome

## ex5 — ft_plant_types — ereditarietà

**Cosa fa in concreto:** crea 3 tipi di piante specializzate (fiore con colore e fioritura, albero con diametro e ombra, verdura con stagione e valore nutrizionale) riusando la classe base, e le fa agire: fiorire, fare ombra, crescere per 20 giorni.

**★ PRIME VOLTE qui:** ereditarietà, `super()`

**Cosa chiede:** Flower (color, bloom), Tree (trunk_diameter, produce_shade), Vegetable (harvest_season, nutritional_value) che EREDITANO da Plant usando `super()`.

**Esecuzione (es. la rosa):**
1. Main: `rose = Flower("Rose", 15.0, 10, "red")` → Python chiama `Flower.__init__`
2. Dentro `Flower.__init__`: prima riga `super().__init__(name, height, age)` → salta SU a `Plant.__init__` → esegue le 3 righe comuni (name, _height, _age_days) → torna giù in Flower
3. Seconda riga: `self.color = "red"` → l'attributo extra del fiore
4. `rose.show()` → Python cerca `show` in Flower → lo trova → lo esegue: prima `super().show()` → esegue `Plant.show` (stampa nome, altezza, età) → torna giù → stampa "Color: red"
5. `rose.bloom()` → esiste solo in Flower → stampa "Rose is blooming beautifully!"

```python
class Plant:
	# nome, altezza, età + grow/age/show (le cose comuni)

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)   # il genitore fa la parte comune
		self.color = color                    # la figlia aggiunge la sua

	def bloom(self):
		print(f"{self.name} is blooming beautifully!")

	def show(self):
		super().show()                        # il genitore stampa la parte comune
		print(f"Color: {self.color}")         # poi la parte specifica
```

**Teoria:**
- `class Flower(Plant):` = "Flower È UNA Plant con qualcosa in più". La figlia riceve TUTTI i metodi e attributi del genitore
- **`super()`** = "la classe genitore". Funziona con QUALSIASI metodo: `super().__init__(...)`, `super().show()`, `super().grow()`
- Perché super(): niente duplicazione. La parte comune vive UNA volta nel genitore; se la cambi, tutte le figlie si aggiornano
- La figlia può ESTENDERE un metodo: chiama super() e poi aggiunge le sue righe
- Ricerca dei metodi: Python cerca dal basso (la classe vera dell'oggetto) e sale (genitore, poi object). Il primo trovato vince
- I metodi generici di Plant servono sia alle piante semplici sia alle figlie (ereditati o estesi con super)

## ex6 — ft_garden_analytics — metodi speciali e classi annidate

**Cosa fa in concreto:** aggiunge a ogni pianta un CONTATORE che tiene traccia di quante volte viene fatta crescere, invecchiare e mostrare; più due funzioni "di classe": una risponde se un'età supera un anno, l'altra crea una pianta anonima. Alla fine mostra le statistiche di ogni pianta.

**★ PRIME VOLTE qui:** `@staticmethod`, `@classmethod`, classe annidata

**Cosa chiede:** staticmethod, classmethod, classe Seed, classe annidata Stats (contatori), TreeStats esteso, funzione esterna display_stats.

**Esecuzione (i pezzi principali):**
1. Main: `print(f"... {Plant.is_older_than_year(30)}")` → chiama il metodo STATICO sulla CLASSE (non su un oggetto) → dentro: `30 > 365` → False → stampato
2. `rose = Flower(...)` → costruttore come ex5, MA il costruttore di Plant ora crea anche il contatore: `self.stats = self.Stats()` → un oggetto contatore (grows=0, ages=0, shows=0) attaccato alla pianta
3. `rose.show()` → dentro show: stampa e poi `self.stats.shows += 1` → segna sul contatore "mostrata 1 volta"
4. `display_stats(rose)` (funzione ESTERNA) → stampa l'intestazione → `plant.stats.display()` → entra nel contatore della rosa → stampa "Stats: 0 grow, 0 age, 1 show"
5. `rose.grow()` → dentro: cresce + `self.stats.grows += 1` → il contatore sale
6. `unknown = Plant.create_anonymous()` → chiama il metodo di CLASSE sulla classe Plant → dentro, `cls` È Plant → `return cls("Unknown plant", 0.0, 0)` crea una pianta nuova e la restituisce → salvata in `unknown`
7. Per la quercia: il costruttore di Tree usa `self.stats = self.TreeStats()` → contatore esteso con il contatore `shades` in più → `produce_shade()` fa `self.stats.shades += 1`

```python
class Plant:
	class Stats:                       # classe annidata: vive dentro Plant
		def __init__(self):            # costruttore senza parametri
			self.grows = 0
			self.ages = 0
			self.shows = 0

		def display(self):
			print(f"Stats: {self.grows} grow, {self.ages} age, {self.shows} show")

	def __init__(self, name, height, age):
		...
		self.stats = self.Stats()      # crea il contatore e attaccalo alla pianta

	def grow(self):
		self._height = round(self._height + 0.8, 1)
		self.stats.grows += 1          # segna sul contatore

	@staticmethod
	def is_older_than_year(age):
		return age > 365

	@classmethod
	def create_anonymous(cls):
		return cls("Unknown plant", 0.0, 0)
```

**Teoria:**
- **Il punto = "vai dentro"** (come un percorso di file, da sinistra a destra):
  - `self.stats.grows` = dentro la pianta → dentro il contatore → prendi grows
  - `plant.stats.display()` = prendi il contatore della pianta → esegui display
- **`self.Stats()`** = crea un contatore nuovo (parentesi vuote: il costruttore non chiede parametri). `Stats` = la classe, `stats` = l'attributo dove salvi il contatore
- **`self.stats: "Plant.Stats" = self.Stats()`** si legge da destra: crea un contatore, salvalo in stats. Il pezzo `"Plant.Stats"` tra virgolette è l'etichetta per mypy, a runtime ignorata
- **@staticmethod**: funzione normale che vive nella classe, NON ha self. Si chiama sulla classe: `Plant.is_older_than_year(30)`
- **@classmethod**: riceve `cls` (la classe) invece di `self` (l'oggetto). `cls(...)` crea un oggetto nuovo. `cls` si adatta all'ereditarietà
- **Classe annidata** = classe dentro classe: "questa cosa serve solo a Plant". Ogni pianta ha il SUO contatore
- **TreeStats(Plant.Stats)** = eredità tra classi annidate: riusa i 3 contatori, aggiunge `shades`

---

# p02 — Garden Guardian (Eccezioni)

## ex0 — ft_first_exception — try/except

**Cosa fa in concreto:** testa una funzione che converte una stringa in numero, prima con un input buono ("25") e poi con uno cattivo ("abc") — e dimostra che col try/except il programma NON crasha.

**★ PRIME VOLTE qui:** `import`, `try`/`except`, `as e`, `Exception`

**Cosa chiede:** `input_temperature(temp_str)` che converte stringa→intero; `test_temperature()` che prova input valido ("25") e invalido ("abc") senza far crashare il programma.

**Esecuzione:**
1. Main → `test_temperature()` → stampa l'intestazione
2. `input_temperature("25")` FUORI dal try (sappiamo che funziona) → `int("25")` → 25 → `return 25` → salvato → stampato
3. `print("Input data is 'abc'")` → poi il try: `input_temperature("abc")` → dentro, `int("abc")` ESPLODE (ValueError) → la funzione muore → Python salta nell'`except Exception as e` → `e` = il messaggio "invalid literal for int() with base 10: 'abc'" → stampato
4. L'esecuzione CONTINUA → stampa "All tests completed - program didn't crash!" → fine

```python
def input_temperature(temp_str: str) -> int:
	return int(temp_str)

def test_temperature() -> None:
	print("=== Garden Temperature ===")
	print("Input data is '25'")
	temperature = input_temperature("25")
	print(f"Temperature is now {temperature}°C")

	print("Input data is 'abc'")
	try:
		input_temperature("abc")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")

	print("All tests completed - program didn't crash!")
```

**Teoria:**
- In C controlli gli errori a mano (`if (fd == -1)`). In Python, quando qualcosa esplode viene LANCIATA un'eccezione
- Eccezione NON catturata = crash: traceback stampato, programma morto, righe dopo non eseguite
- **`try:`** = "prova a eseguire questo blocco". Se esplode qualcosa → salta IMMEDIATAMENTE nell'except (le righe rimaste nel try vengono saltate)
- **`except Exception as e:`** = la rete di salvataggio. `Exception` cattura qualsiasi errore. `as e` salva il messaggio nella variabile `e`
- Dopo l'except, il programma CONTINUA — non muore
- Analogia: il trapezista (try) e la rete (except). L'analogia C: try/except sostituisce `if (x == -1) return error`
- Regola d'oro: ogni operazione che può fallire (`int()` su input, `open()` di file...) va nel try. "Your programs must never crash"
- `temp_str` è solo il NOME del parametro: alla chiamata il valore ("25") finisce in quella variabile locale, che muore a fine funzione

## ex1 — ft_raise_exception — raise

**Cosa fa in concreto:** come ex0, ma la funzione ora RIFIUTA anche le temperature fuori da 0-40: le lancia lei stessa come errore, e il programma le cattura e continua.

**★ PRIME VOLTE qui:** `raise`

**Cosa chiede:** in `input_temperature`, dopo la conversione, se la temperatura è fuori da 0–40 lancia un'eccezione TU con `raise`. Test con "100" e "-50".

**Esecuzione (con "100"):**
1. `input_temperature("100")` → `int("100")` → 100 → la conversione FUNZIONA
2. `if temperature > 40:` → 100 > 40 VERO → **`raise ValueError("100°C is too hot...")`** → la funzione muore QUI, il `return` non si raggiunge
3. L'eccezione vola al try di `test_temperature` → `except Exception as e` → `e` = il messaggio → stampato
4. Il programma continua col test successivo

```python
def input_temperature(temp_str: str) -> int:
	temperature = int(temp_str)
	if temperature > 40:
		raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
	if temperature < 0:
		raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
	return temperature
```

**Teoria:**
- **`raise`** = "lancia un'eccezione ADESSO". Dopo il raise, la funzione muore lì — Python salta al except più vicino
- `raise` e `if` sono cose SEPARATE: l'if è la condizione che decide QUANDO lanciare. Potresti lanciare anche senza if
- `ValueError` = il tipo di eccezione ("il valore non va bene"). Ce ne sono tanti (TypeError, ZeroDivisionError, FileNotFoundError...)
- **Tra parentesi = il MESSAGGIO, non un print.** `raise` NON stampa niente: crea l'oggetto-errore col messaggio e lo lancia. La STAMPA la fa chi cattura
- Flusso: raise crea l'errore → vola via → except lo afferra → e = messaggio → print lo mostra
- Ex0 vs Ex1: in ex0 gli errori esplodono da soli (incidenti); in ex1 sei TU il guardiano che suona l'allarme

## ex2 — ft_different_errors — i tipi di errore

**Cosa fa in concreto:** mostra 4 errori diversi fatti esplodere A COMANDO (conversione sbagliata, divisione per zero, file inesistente, tipi mescolati) e li cattura uno a uno col loro tipo specifico, dimostrando che il programma sopravvive a tutti.

**★ PRIME VOLTE qui:** tipi di errore specifici (ValueError ecc.), `else` del try

**Cosa chiede:** `garden_operations(n)` con 4 bombe diverse (una per tipo di errore); `test_error_types()` che le fa esplodere tutte e le cattura ognuna col SUO except specifico. Dimostrare il catch multiplo e l'`else`.

**Esecuzione:**
1. Main → `test_error_types()` → stampa l'intestazione
2. "Testing operation 0..." → try: `garden_operations(0)` → dentro, `0 == 0` VERO → `int("abc")` esplode con ValueError → vola su → `except ValueError as e` lo cattura (le etichette combaciano) → stampato
3. "Testing operation 1..." → `garden_operations(1)` → `1 == 0`? NO → `1 == 1`? SÌ → `1 / 0` esplode con ZeroDivisionError → `except ZeroDivisionError` lo cattura
4. "Testing operation 2..." → `open("/non/existent/file")` esplode con FileNotFoundError → `except FileNotFoundError` lo cattura
5. "Testing operation 3..." → `"garden" + 42` esplode con TypeError → `except TypeError` lo cattura
6. "Testing operation 4..." → `garden_operations(4)` → nessun if scatta (4 non è 0,1,2,3) → la funzione finisce SENZA errori → l'except viene saltato → si va nell'`else` → "Operation completed successfully"
7. "All error types tested successfully!" → fine

```python
def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
		int("abc")                     # ValueError
	elif operation_number == 1:
		result = 1 / 0                 # ZeroDivisionError
	elif operation_number == 2:
		open("/non/existent/file")     # FileNotFoundError
	elif operation_number == 3:
		result = "garden" + 42         # TypeError
	# altri valori: nessun if scatta → nessun errore

def test_error_types() -> None:
	print("=== Garden Error Types Demo ===")
	print("Testing operation 0...")
	try:
		garden_operations(0)
	except ValueError as e:
		print(f"Caught ValueError: {e}")
	# ... idem per 1 (ZeroDivisionError), 2 (FileNotFoundError), 3 (TypeError)

	print("Testing operation 4...")
	try:
		garden_operations(4)
	except Exception as e:
		print(f"Caught error: {e}")
	else:
		print("Operation completed successfully")
```

**Teoria:**
- In `garden_operations` NON c'è try: gli errori DEVONO esplodere, è il loro lavoro. Le righe sono normalissime righe che falliscono da sole (sono i 4 errori classici che ogni programmatore commette)
- **Chi decide il tipo dell'errore? La funzione che fallisce.** `int()` lancia SEMPRE ValueError, `open()` SEMPRE FileNotFoundError — è scritto nel loro codice interno. L'except non indovina: confronta l'etichetta dell'oggetto esploso con la classe richiesta. Etichetta diversa → l'errore vola oltre → crash
- **`except ValueError`** cattura SOLO ValueError: rete con i buchi della misura giusta
- **`else` del try** = l'opposto dell'except: gira SOLO se NON è esploso niente
- **Perché tipi diversi di errori?** Per reagire in modo diverso: file mancante → segnala e prosegui; TypeError → è un bug tuo. Se tutto fosse "errore generico" non sapresti mai cosa è successo
- **Catch multiplo con un try solo** — due modi: più `except` in fila, oppure `except (ValueError, ZeroDivisionError, TypeError) as e:`
- Ex0 vs Ex2: ex0 = primo contatto, un errore solo, except generico. Ex2 = il catalogo dei tipi, ognuno col suo except
- Crash Python ≠ segfault C: il segfault è il SO che ti uccide senza messaggi e senza recupero; l'eccezione Python è catturabile PRIMA che uccida il programma
- **Built-in vs nostre: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError` NON sono nomi che abbiamo dato noi.** Sono CLASSI GIÀ PRONTE dentro Python (come print, int, range). I nomi li assegni TU solo quando CREI un'eccezione (ex3)
- Il riconoscimento: ogni eccezione è un OGGETTO di una CLASSE. L'except fa un controllo di tipo (come isinstance). `except Exception` prende tutto perché OGNI errore eredita da Exception

## ex3 — ft_custom_errors — eccezioni personalizzate

**Cosa fa in concreto:** crea 3 tipi di errore PERSONALIZZATI (giardino, pianta, acqua) come classi, li lancia e li cattura — dimostrando che catturare l'errore-genitore (GardenError) prende anche le figlie.

**★ PRIME VOLTE qui:** eccezione custom `class X(Exception)`, parametro con valore di default

**Cosa chiede:** classi `GardenError(Exception)`, `PlantError(GardenError)`, `WaterError(GardenError)` con messaggi di default. Dimostrare che `except GardenError` cattura tutte le figlie.

**Esecuzione:**
1. Main → `test_custom_errors()` → intestazione
2. try: `raise PlantError("The tomato plant is wilting!")` → Python crea l'oggetto errore: chiama `PlantError.__init__(message)` → dentro: `super().__init__(message)` → chiama `GardenError.__init__(message)` → dentro: `super().__init__(message)` → chiama `Exception.__init__(message)` che conserva il messaggio → l'oggetto è pronto → viene LANCIATO
3. `except PlantError as e` → etichetta combacia → `e` = il messaggio → stampato
4. Stessa cosa con WaterError
5. Test finale: `raise PlantError(...)` ma questa volta `except GardenError as e` → le etichette NON combaciano direttamente... MA PlantError È UN GardenError (eredita) → la rete GardenError lo prende comunque → stampato. Idem per WaterError

```python
class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message: str = "Unknown water error"):
		super().__init__(message)

try:
	raise PlantError("The tomato plant is wilting!")
except GardenError as e:
	print(f"Caught GardenError: {e}")
```

**Teoria:**
- **Un'eccezione è una classe che eredita da Exception** — `Exception` è la classe madre di TUTTI gli errori
- La nostra classe è un PASSAMANO: riceve il messaggio e lo inoltra a Exception con `super().__init__(message)`. È Exception che sa conservare e mostrare il messaggio
- La catena dei costruttori: PlantError.__init__ → super() → GardenError.__init__ → super() → Exception.__init__. Tre costruttori in fila, il lavoro vero lo fa l'ultimo
- `message: str = "Unknown garden error"` = parametro con VALORE DI DEFAULT: se chiami `GardenError()` senza messaggio, usa quello
- **In `super().__init__(message)` NON si scrive self**: si passa solo `message`. Come sempre, quando chiami un metodo Python riempie self da solo (è lo stesso motivo per cui scrivi `rose.show()` e non `rose.show(rose)`)
- **`except GardenError` cattura anche PlantError e WaterError** perché le figlie SONO GardenError (come Flower È UNA Plant)
- Quando creare errori propri: quando i built-in non descrivono bene il tuo problema. Due livelli di precisione: WaterError (solo acqua) o GardenError (tutto il giardino)
- L'eccezione custom ha UN solo parametro oltre a self: il messaggio. Flusso: raise crea l'errore → except `as e` lo afferra → print lo mostra

## ex4 — ft_finally_block — finally

**Cosa fa in concreto:** simula un impianto d'irrigazione: "apre il rubinetto", annaffia alcune piante (solo quelle col nome maiuscolo, le altre scatenano errore) e CHIUDE SEMPRE il rubinetto — anche quando scoppia l'errore a metà.

**★ PRIME VOLTE qui:** `finally`, indicizzazione `stringa[0]`, `.isupper()`

**Cosa chiede:** `water_plant(plant_name)` che annaffia solo nomi con la maiuscola (altrimenti lancia la NOSTRA PlantError); `test_watering_system()` che apre/chiude il sistema con try/except/finally. La chiusura deve avvenire SEMPRE, anche con errori.

**Esecuzione:**
1. Main → `test_watering_system()` → intestazione
2. "Testing valid plants..." → try: "Opening watering system" → `water_plant("Tomato")` → `"Tomato"[0]` è 'T' → `.isupper()` True → stampa "Watering Tomato: [OK]" → idem per Lettuce e Carrots
3. Il try finisce SENZA errori → l'except (non c'è) viene saltato → **il finally gira COMUNQUE** → "Closing watering system"
4. "Testing invalid plants..." → try: "Opening watering system" → `water_plant("Tomato")` → [OK] → `water_plant("lettuce")` → `"lettuce"[0]` è 'l' → `.isupper()` False → **`raise PlantError("Invalid plant name to water: 'lettuce'")`** → il try muore qui
5. `except PlantError as e` → stampa "Caught PlantError: ..." e ".. ending tests and returning to main"
6. **Il finally gira comunque** → "Closing watering system"
7. Si continua → "Cleanup always happens, even with errors!" → fine

```python
def water_plant(plant_name: str) -> None:
	if plant_name[0].isupper():
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_system() -> None:
	try:
		print("Opening watering system")
		water_plant("Tomato")
		water_plant("lettuce")       # BOOM: PlantError
	except PlantError as e:
		print(f"Caught PlantError: {e}")
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system")   # gira SEMPRE
```

**Teoria (nell'ordine in cui le cose accadono):**
- **Le stringhe si indicizzano come gli array del C**: ogni carattere ha una posizione, la prima è 0. `"Tomato"[0]` → 'T', `"lettuce"[0]` → 'l'. Perché 0 e non 1? Per convenzione storica dei computer (stessa ragione del C): la posizione si conta a partire da 0
- **`.isupper()` è un METODO delle stringhe GIÀ PRONTO in Python**: una funzione che vive dentro il tipo `str` — non l'hai creata, non l'hai importata, esiste da sempre, come print() e int(). La differenza con le funzioni libere: i metodi vivono DENTRO il tipo e ci arrivi col punto
  ```python
  print("CIAO")          # funzione libera: la chiami direttamente
  "CIAO".isupper()       # metodo: vive dentro il tipo str, ci arrivi col punto
  ```
  `isupper` funziona su OGNI stringa perché è attaccato al tipo `str` — come `show()` e `grow()` erano attaccati alla TUA classe Plant in p01. I metodi scritti da noi e i metodi built-in funzionano allo stesso identico modo: il punto "va dentro" l'oggetto e chiama la funzione che ci vive
- La cassetta degli attrezzi delle stringhe: `.isupper()` (tutto maiuscolo?), `.islower()` (tutto minuscolo?), `.capitalize()` (prima lettera maiuscola — usato in p00 ex7), `.startswith(...)` (inizia con...?)
- Il punto è il solito "vai dentro": `plant_name[0].isupper()` = vai nella stringa → prendi il carattere 0 → chiedigli se è maiuscolo
- La condizione `if plant_name[0].isupper():` → True: annaffia e stampa [OK]; False: `raise PlantError(...)` — il metodo muore lì, l'errore vola su
- **`finally` = il blocco che gira SEMPRE**, sia che il try riesca sia che esploda. È la garanzia di pulizia: file aperti, sistemi accesi vanno chiusi comunque. In C: il `fclose()` che metteresti in ogni ramo d'errore — qui lo scrivi UNA volta
- | Blocco | Quando gira |
  |---|---|
  | `try` | sempre, finché non esplode |
  | `except` | SOLO se è esploso |
  | `finally` | SEMPRE, esploso o no |
- Ordine con errore: try esplode → except gestisce → **finally pulisce** → il programma continua
- **Nomi nuovi in questo esercizio**: `plant_name` (parametro, nome scelto da noi), `[0]` (indicizzazione, sintassi di Python), `isupper` (metodo built-in delle stringhe), `finally` (parola chiave del linguaggio), `PlantError` (classe NOSTRA di ex3)

---

# p03 — Data Quest (Collezioni)

Il cuore del modulo: le **collezioni** di Python — i contenitori di dati. Sono 4, ognuna con il suo superpotere:

| Collezione | Come si scrive | Superpotere | Analogo C |
|---|---|---|---|
| **lista** | `[1, 2, 3]` | ordinata, indicizzata, modificabile, cresce da sola | array |
| **tupla** | `(1, 2, 3)` | come la lista ma IMMUTABILE (scritta nella pietra) | array const |
| **set** | `{1, 2, 3}` | elementi UNICI, non ordinati | — |
| **dizionario** | `{"chiave": valore}` | coppie chiave→valore, ricerca istantanea | tabella/hash |

Più avanti: generatori (ex5) e comprehensions (ex6), che sono la sintassi "condensata" per creare collezioni.

Il modulo ha una regola nuova: **niente file I/O**. Tutti i dati arrivano da riga di comando (`sys.argv`) o da input.

## ex0 — ft_command_quest — sys.argv (la lista dei parametri)

**Cosa fa in concreto:** stampa gli argomenti che gli passi da riga di comando, numerati; se non ne passi nessuno stampa "No arguments provided!".

**★ PRIME VOLTE qui:** `sys`, `sys.argv`, `len()`, lista

**Cosa chiede:** script che mostra i parametri ricevuti da riga di comando. Senza argomenti → messaggio dedicato. Con argomenti → numerati da 1. "Total arguments" conta TUTTO, compreso il nome del programma.

**Obiettivo:** incontrare la prima lista di Python senza costruirla: `sys.argv` è una lista già pronta fatta da Python quando lanci il programma. È l'argc/argv del C.

**Come testare:**
```bash
cd python/p03/ex0
python3 ft_command_quest.py                     # caso senza argomenti
python3 ft_command_quest.py hello world 42      # caso con 3 argomenti
python3 ft_command_quest.py "Data Quest"        # argomento con spazio (tra virgolette)
```

**Output atteso:**
```
$> python3 ft_command_quest.py
=== Command Quest ===
Program name: ft_command_quest.py
No arguments provided!
Total arguments: 1
$> python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4
```

**Esecuzione:**
1. `import sys` — carica il modulo `sys`. **`sys` è un MODULO di Python** (si legge "system"): una scatola di strumenti GIÀ PRONTA che riguarda il sistema (il terminale, il programma in esecuzione). Non l'abbiamo creata noi: esiste già dentro Python, ma non è caricata di default — per questo serve `import sys` in cima: è come il `#include <...>` del C, dice a Python "vai a prendermi quella libreria". Dopo l'import, tutti gli strumenti della scatola si raggiungono col punto: `sys.argv`, `sys.stdin`, ecc.
2. `if __name__ == "__main__":` vero → chiama `main()`
3. `sys.argv` è la lista di TUTTO ciò che hai scritto dopo `python3`, separato dagli spazi. "argv" = argument vector, come in C:
   ```
   sys.argv = ["ft_command_quest.py", "hello", "world", "42"]
                ↑ posizione 0         ↑ 1       ↑ 2     ↑ 3
   ```
   - `sys.argv[0]` = il nome del programma (come in C)
   - `len(sys.argv)` = quanti elementi (4)
4. **`len()` è una FUNZIONE già pronta di Python** (built-in) — non l'abbiamo definita noi, non serve importarla: esiste da sempre, come print() e int(). Fa UNA cosa: conta gli elementi di una collezione e restituisce il numero. `len("ciao")` → 4, `len([1,2,3])` → 3, `len(sys.argv)` → quanti argomenti. In C questa funzione non esiste: tenevi il conto a mano o usavi strlen
5. `print(f"Program name: {sys.argv[0]}")` → "ft_command_quest.py"
6. `if len(sys.argv) == 1:` → la lista ha UN solo elemento = nessun argomento passato (c'è solo il nome) → "No arguments provided!"
7. Altrimenti (else): `len(sys.argv) - 1` = gli argomenti senza il nome (3) → loop `for i in range(1, len(sys.argv)):` parte da 1 per saltare il nome → stampa "Argument 1: hello", ecc.
8. `Total arguments: {len(sys.argv)}` → conta anche il nome: 4

**Codice:**
```python
import sys

def main() -> None:
	print("=== Command Quest ===")
	print(f"Program name: {sys.argv[0]}")

	if len(sys.argv) == 1:
		print("No arguments provided!")
	else:
		print(f"Arguments received: {len(sys.argv) - 1}")
		for i in range(1, len(sys.argv)):
			print(f"Argument {i}: {sys.argv[i]}")

	print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
	main()
```

**Teoria:**
- **Lista** = il contenitore base di Python, come l'array del C ma: cresce da sola (non dichiari la dimensione), `len(lista)` per la lunghezza, può contenere tipi misti
- **Chi è cosa in questo esercizio:**
  - `sys` → modulo PREDEFINITO di Python (importato da noi col `import`)
  - `argv` → attributo/lista GIÀ PRONTA dentro sys
  - `len()` → funzione PREDEFINITA di Python (built-in)
  - `print()`, `range()` → funzioni PREDEFINITE (built-in)
  - `main()` → funzione DEFINITA DA NOI
  - `ft_command_quest.py` → il file (nome imposto dal subject)
  - `i` → variabile del loop, nome scelto da noi
- `sys.argv[i]` si legge come `argv[i]` in C; `len(sys.argv)` è l'`argc`
- `range(1, len(sys.argv))` parte da 1 e NON da 0 per saltare il nome del programma
- Un argomento con spazi va messo tra virgolette nel terminale: `"Data Quest"` diventa UN solo argomento
- **Domanda da evaluation** ("come evitare di stampare il nome del programma con gli argomenti?"): con lo **slicing** `sys.argv[1:]` — significa "la lista dal secondo elemento in poi". (Lo si vede nei prossimi esercizi)
- `import sys` sta in cima al file, fuori da tutto — come gli `#include` del C

---

## ex1 — ft_score_analytics — lista di numeri + try/except

**Cosa fa in concreto:** prende punteggi da riga di comando, scarta quelli non numerici (con messaggio), e sui validi calcola: quanti sono, totale, media, massimo, minimo e range.

**★ PRIME VOLTE qui:** `.append()`, `sum()`/`max()`/`min()`, slicing `[1:]`, `return` senza valore

**Cosa chiede:** prendere i punteggi da riga di comando, scartare quelli non numerici con un messaggio, e calcolare: numero, totale, media, massimo, minimo, range. Senza punteggi validi → messaggio di usage.

**Obiettivo:** costruire la TUA prima lista (con `.append()`), usare le funzioni built-in `sum()`, `max()`, `min()`, e applicare il try/except di p02 su input reali.

**Come testare:**
```bash
cd python/p03/ex1
python3 ft_score_analytics.py 1500 2300 1800 2100 1950   # caso completo
python3 ft_score_analytics.py                            # nessun argomento
python3 ft_score_analytics.py ab ac                      # solo argomenti invalidi
python3 ft_score_analytics.py 1500 ab 2300               # misto: scarta 'ab', tiene 2
```

**Esecuzione (caso 1500 2300 1800 2100 1950):**
1. Main → `main()` → stampa l'intestazione
2. `scores = []` → crea una LISTA VUOTA — la scatola che riempiremo. `[]` = "lista senza niente dentro"
3. `for arg in sys.argv[1:]:` → **lo slicing**: `sys.argv[1:]` significa "la lista dal secondo elemento in poi" (salta il nome del programma). A ogni giro `arg` è UN argomento: "1500", "2300", ... È la risposta alla domanda da evaluation di ex0!
4. Dentro il loop, il try: `int(arg)` converte "1500" → 1500 → `scores.append(1500)` → **append aggiunge l'elemento IN CODA alla lista**. La lista cresce da sola: [1500] → [1500, 2300] → ... In C avresti dovuto allocare l'array della dimensione giusta
5. Se `int(arg)` fallisce (es. "ab") → il except stampa "Invalid parameter: 'ab'" e si passa all'argomento dopo — il programma non muore (p02!)
6. `if len(scores) == 0:` → nessun punteggio valido → stampa l'usage e **`return`**: la funzione finisce QUI, il resto sotto non gira. `return` senza valore = "esci dalla funzione" (come return; in C)
7. `sum(scores)` → 9650 (built-in: somma tutti gli elementi della lista)
8. `sum(scores) / len(scores)` → 9650 / 5 = **1930.0** — in Python la divisione `/` dà SEMPRE un float con la virgola
9. `max(scores)` → 2300, `min(scores)` → 1500 (built-in)
10. `max(scores) - min(scores)` → il range: 800

**Codice:**
```python
import sys

def main() -> None:
	print("=== Player Score Analytics ===")

	scores = []
	for arg in sys.argv[1:]:
		try:
			scores.append(int(arg))
		except ValueError:
			print(f"Invalid parameter: '{arg}'")

	if len(scores) == 0:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return

	print(f"Scores processed: {scores}")
	print(f"Total players: {len(scores)}")
	print(f"Total score: {sum(scores)}")
	print(f"Average score: {sum(scores) / len(scores)}")
	print(f"High score: {max(scores)}")
	print(f"Low score: {min(scores)}")
	print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
	main()
```

**Teoria:**
- **Chi è cosa:** `sys` → modulo predefinito; `argv` → attributo pronto dentro sys; `[]` → sintassi per creare una lista; `.append()` → METODO delle liste (built-in): aggiunge in coda; `int()`, `len()`, `sum()`, `max()`, `min()`, `print()` → funzioni built-in; `main()` → funzione nostra; `scores`, `arg` → variabili nostre
- **Lista vuota + append = il pattern base:** parti da `[]` e riempi col loop
- **Traccia di `scores.append(int(arg))` giro per giro:** `[]` → append(1500) → `[1500]` → append(2300) → `[1500, 2300]` → ... sempre in CODA, nell'ordine di arrivo. I tre pezzi: `int(arg)` converte la stringa del giro → `.append(...)` è il METODO delle liste (built-in) = "aggiungi in coda" → `scores.append(...)` = "prendi la MIA lista scores e aggiungici questo". `append` in inglese = aggiungere in fondo, come appendere un foglio a una pila
- **Differenza col C:** in C dovevi sapere `n` prima e fare `malloc(n * sizeof(int))` + gestire l'indice; la lista Python cresce da sola — niente dimensione, niente indice, niente realloc
- **ValueError in breve:** errore già pronto in Python (classe built-in, come FileNotFoundError) che scatta quando una funzione riceve un valore del tipo giusto ma dal CONTENUTO sbagliato: `int("abc")` — stringa (tipo giusto) senza un numero dentro (contenuto sbagliato). Il nome dice tutto: errore di VALORE. Lo lancia `int()` da sola, e il nostro `except ValueError` la cattura per tipo (rete con i buchi giusti, p02 ex2)
- **Slicing `sys.argv[1:]`** = "dal secondo in poi". La sintassi `[inizio:fine]` taglia le liste: `[1:]` = da posizione 1 fino alla fine, `[:3]` = dall'inizio fino a posizione 3 (esclusa)
- **La divisione `/` dà sempre un float** (1930.0, non 1930). Se vuoi la divisione intera: `//`
- `return` da solo = "esci subito dalla funzione" — le righe dopo non girano
- La regola del subject: se ci sono validi e invalidi, si scartano gli invalidi e si prosegue coi validi; solo se non ne resta nessuno → usage

---

## ex2 — ft_coordinate_system — tuple e distanza 3D

**★ PRIME VOLTE qui:** tupla, `math.sqrt()`, `.split()`, `float()`, unpacking, `while True`, `**`, `continue`/`break`

**Cosa fa DAVVERO il programma (prima cosa da capire):** NON calcola nessun centro e nessuna area. Ci sono solo **DUE PUNTI nello spazio 3D**. Pensa a Minecraft: ogni posizione nel mondo è fatta di 3 numeri — x (est/ovest), y (altezza), z (nord/sud). Un punto = 3 numeri. Il programma fa solo due cose:
1. Chiede dove sei → punto 1 → calcola quanto disti dal **centro del mondo**, che è il punto FISSO (0, 0, 0) — dove si incrociano gli assi. Il centro NON viene calcolato dai tuoi numeri: è già lì, è l'origine.
2. Chiede dove sei adesso (ti sei mosso) → punto 2 → calcola quanto distano i due punti tra loro.

La matematica è sempre la stessa, Pitagora in 3D: `radice((x2-x1)² + (y2-y1)² + (z2-z1)²)`. Per il centro, x2=y2=z2=0 → si semplifica in `radice(x² + y² + z²)`.

**Cosa chiede:** funzione `get_player_pos()` che chiede coordinate `x,y,z`, gestisce gli errori, ritenta finché non sono valide, e RESTITUISCE una **tupla** con le 3 coordinate. Poi il main fa i due calcoli sopra.

**Come testare:**
```bash
cd python/p03/ex2
python3 ft_coordinate_system.py
# prova:  hello world        → Invalid syntax
#        1.0 , 2.5, 3.0      → distanza dal centro 4.0311
#        4,abc,5             → errore sul parametro 'abc'
#        4,5,6               → distanza tra i punti 4.9244
```

**La tupla in una riga:** è una collezione come la lista MA **immutabile** — si crea con le parentesi TONDE `(a, b, c)` invece delle quadre, e non ha `append`. Non la cambi: "scritta nella pietra". Analogia: la lista è una SCATOLA a cui continui ad aggiungere fogli (append); la tupla è una BUSTA SIGILLATA con esattamente 3 numeri scritti sopra — non puoi aggiungere, togliere o modificare niente. Un punto 3D è per natura esattamente 3 numeri → la busta sigillata è il contenitore giusto: nessun codice potrà mai aggiungere un 4° numero per sbaglio.

**Il `while True` in una riga:** significa "ripeti per sempre". Da solo non finirebbe MAI: si esce solo con `return` o `break`. Analogia: la porta di un locale con la parola d'ordine — chiede, se sbagli chiede di nuovo, non si stanca mai; si apre solo quando dici quella giusta. Qui non sappiamo QUANTE volte l'utente sbaglierà (0, 1, 5?) → "chiedi finché la risposta non è buona". I due modi in cui il giro finisce: `continue` = "risposta sbagliata, torna in cima e richiedi" (skip del resto del giro); `return` = "risposta buona, esci dalla funzione e consegna il risultato" (UNICA uscita normale).

**Esecuzione di `get_player_pos()` riga per riga:**

1. `user_input = input(...)` — chiede e salva TUTTO il testo digitato in UNA stringa. Es. l'utente scrive `1.0 , 2.5, 3.0`
2. `pieces = user_input.split(",")` — **split** spezza la stringa a ogni virgola → lista `["1.0 ", " 2.5", " 3.0"]`. Se l'utente scrive "hello world" (nessuna virgola) → `["hello world"]` (lista con 1 pezzo)
3. `if len(pieces) != 3:` — se i pezzi non sono esattamente 3 (virgole mancanti o di troppo) → "Invalid syntax" → `continue` → si ricomincia dall'input
4. `numbers = []` e `all_valid = True` — si prepara la scatola vuota dei numeri convertiti e la BANDIERINA "tutto valido finché non si dimostra il contrario"
5. Loop `for piece in pieces:` — un pezzo alla volta:
   - `float("1.0 ")` → 1.0 → append in `numbers` (float ignora gli spazi ai bordi)
   - `float(" 2.5")` → 2.5 → append
   - `float("abc")` → BOOM ValueError → except stampa `Error on parameter 'abc': ...` → `all_valid = False` (bandierina giù) → `break` (si esce subito dal for, tanto è inutile continuare)
6. `if all_valid:` — se la bandierina è ancora su (tutte e 3 le conversioni riuscite) → `return (numbers[0], numbers[1], numbers[2])` → crea la TUPLA e la restituisce → la funzione FINISCE (il while muore col return)
7. Se la bandierina è giù → l'if è saltato → si arriva in fondo al while → NUOVO GIRO → si richiede tutto da capo (i vecchi numeri finiscono nella spazzatura)

**Il main poi:**
1. `x1, y1, z1 = get_player_pos()` — **unpacking**: la tupla restituita si apre e i 3 valori vanno nelle 3 variabili, in ordine (come distribuire 3 carte da un mazzo)
2. `math.sqrt(x1*x1 + y1*y1 + z1*z1)` — distanza dal centro (0,0,0). `math.sqrt()` = radice quadrata, funzione PREDEFINITA del modulo `math` (importato in cima, come `#include <math.h>` in C). `round(d, 4)` = arrotonda a 4 decimali → 4.0311
3. Secondo punto → distanza tra i due con la formula completa: `sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)`

**Codice (variabili con nomi che spiegano da sole cosa contengono):**
```python
import math

def get_player_pos() -> tuple[float, float, float]:
	while True:
		user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
		pieces = user_input.split(",")
		if len(pieces) != 3:
			print("Invalid syntax")
			continue
		numbers = []
		all_valid = True
		for piece in pieces:
			try:
				numbers.append(float(piece))
			except ValueError as e:
				print(f"Error on parameter '{piece}': {e}")
				all_valid = False
				break
		if all_valid:
			return (numbers[0], numbers[1], numbers[2])

def main() -> None:
	print("=== Game Coordinate System ===")

	print("Get a first set of coordinates")
	x1, y1, z1 = get_player_pos()
	print(f"Got a first tuple: {(x1, y1, z1)}")
	print(f"It includes: X={x1}, Y={y1}, Z={z1}")

	distance = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
	print(f"Distance to center: {round(distance, 4)}")

	print("Get a second set of coordinates")
	x2, y2, z2 = get_player_pos()

	distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
	print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
	main()
```

**Teoria:**
- **Chi è cosa:** `math` → modulo predefinito (importato); `math.sqrt()` → funzione predefinita del modulo math; `split()` → METODO built-in delle stringhe; `float()` → CLASSE built-in; `append()` → metodo built-in delle liste; `continue`/`break`/`while`/`True`/`return` → parole chiave del linguaggio; `(a, b, c)` → sintassi tupla; `x1, y1, z1 = ...` → unpacking; `**` → operatore potenza; `user_input`, `pieces`, `numbers`, `all_valid`, `piece` → variabili NOSTRE coi nomi che spiegano il contenuto; `get_player_pos()`, `main()` → funzioni nostre
- **Tonde vs quadre (domanda classica da evaluation):** `(1.0, 2.5, 3.0)` con le TONDE CREA la tupla con i VALORI (la busta sigillata vera). `tuple[float, float, float]` con le QUADRE DESCRIVE il TIPO (l'etichetta "busta che contiene 3 decimali") — non crea nulla, è solo annotazione per mypy, a runtime ignorata. Regola tascabile: VALORI dentro → parentesi del contenitore (tonde per tupla, quadre per lista); TIPI dentro → sempre quadre (`tuple[...]`, `list[...]`). In C l'avevi già visto: `int arr[3]` — le quadre descrivono la struttura
- **La virgola SEPARA, il punto DEI decimali:** non si mischiano. `1,0 ,2.0 ,3,5` → split a ogni virgola → 5 pezzi → "Invalid syntax". Per Python "1,0" è DUE coordinate (x=1, y=0), non "uno virgola zero". Il modo giusto: `1.0, 2.0, 3.5` (3 pezzi, decimali col punto). Gli spazi ai bordi non danno problemi: `float(" 2.0       ")` funziona
- **`while True:` + `continue` = il pattern "ritenta finché non va"**: loop infinito, unica uscita normale il `return`. `continue` = salta il resto del giro e torna in cima
- **La bandierina `all_valid`**: parte True, diventa False alla PRIMA conversione fallita. È il modo semplice di dire "ricordati se qualcosa è andato storto lungo il giro". In C: una variabile `int ok = 1;` che metti a 0 sull'errore
- **`float("4")`** funziona ("4" → 4.0): float accetta anche interi scritti come stringa. **Precisazione:** float NON ripulisce — ignora gli spazi ai bordi e poi prova a convertire tutto il resto: `float(" 1.4 ")` → 1.4 ✓; `float("1.4n")` → ValueError `could not convert string to float: '1.4n'` (la "n" non è un numero) → l'except cattura, bandierina giù, break, si richiede
- **Unpacking** funziona con tuple E liste: il numero di variabili a sinistra DEVE combaciare col numero di elementi
- **`a ** 2`** = a elevato a 2 (a²). In C: `pow(a, 2)`
- Perché la tupla e non la lista: il punto DEVE restare 3 numeri, per sempre. La lista ha append (si allarga), la tupla no — garanzia di sicurezza

---

## ex3 — ft_achievement_tracker — i set

**★ PRIME VOLTE qui:** set, `random.randint()`, `random.sample()`, **dizionario**, `union`/`intersection`/`difference`, **annotazione di variabile** (`nome: Tipo = valore`), **loop annidato** (loop dentro un loop)

### ★ PRIMA VOLTA: l'annotazione di variabile — i due punti nelle assegnazioni

```python
all_achievements: set[str] = set()
```

La riga ha DUE pezzi separati:

- **`all_achievements = set()`** — la parte VERA: crea il set vuoto e lo assegna alla variabile. È questa che gira davvero a runtime
- **`: set[str]`** — l'ETICHETTA del tipo ("questa variabile conterrà un set di stringhe"), per mypy e per chi legge. **A runtime viene IGNORATA completamente.** È la stessa cosa dei type hints nelle firme `def f(x: str) -> None` (lì i due punti li hai già visti, stesso significato) — qui applicati a una variabile invece che a un parametro

**Perché serve qui:** `all_achievements = set()` parte da un set VUOTO — mypy non può indovinare che tipo di elementi conterrà, quindi protesta finché non metti l'etichetta `set[str]`. Con variabili il cui tipo si capisce da solo (es. `n = random.randint(6, 9)` → int ovvio) l'etichetta non serve e non c'è.

**Regola:** `nome: Tipo = valore` = "dichiara il tipo E assegna il valore". Due punti = dichiarazione, uguale = assegnazione. E `all_achievements` è una variabile NOSTRA: nome scelto da noi, prima di quella riga non esisteva.

**Chiarimento (equivoco classico):** la riga NON va divisa in due istruzioni. `x: set[str] = set()` a runtime è IDENTICA a `x = set()` — l'etichetta è metadata, come un commento. E non confondere le parentesi: `set[str]` con le QUADRE = descrizione del tipo (non esegue nulla — come `tuple[float, float, float]` in ex2); `set(str)` con le TONDE = CHIAMATA ("costruisci un set da str" → errore); `set(str) = set()` = SyntaxError, non si assegna a una chiamata

**L'analogia che spiega tutto: LA PROMESSA.** `x: int = 5` = azione vera (`x = 5`) + promessa (`: int` = "x conterrà un intero"). I due punti sono SOLO la punteggiatura che separa il nome dal tipo (come un modulo cartaceo "Nome: ____", o il `:` di `if x:` e di `def f(x: str)`). Chi controlla la promessa? **Python: NESSUNO** — a runtime la ignora del tutto (demo: prometti int, ci metti una stringa, Python tace). **mypy: il controllore** — programma separato che legge il codice senza eseguirlo e confronta promesse coi fatti ("hai promesso int e messo una stringa" → errore). **Gli umani: i lettori** — vedono `: set[str]` e sanno cosa ci deve stare. Si fanno perché il subject 42 lo impone (mypy all'evaluation). **In C il tipo è LEGGE** (il compilatore rifiuta il resto); **in Python è solo PROMESSA** (ignorata dall'esecuzione)

**Cosa fa il programma:** genera per 4 giocatori (Alice, Bob, Charlie, Dylan) un sacchetto di achievement presi a caso da una lista fissa di 14. Poi calcola con le operazioni dei set: quali achievement esistono in totale, quali hanno TUTTI in comune, quali ha SOLO un giocatore, e cosa manca a ciascuno per averli tutti.

**Il set in una riga:** è una collezione di elementi **UNICI** e **SENZA ORDINE**. Analogia: un sacchetto — se butti dentro due volte lo stesso oggetto, ne resta uno solo; e se agiti il sacchetto l'ordine cambia a ogni stampa (per questo a ogni run l'output esce in ordine diverso). Si crea con le graffe `{a, b, c}` o con `set(...)`.

**Perché il set qui:** gli achievement non devono avere duplicati per definizione — o ce l'hai o non ce l'hai, non "ce l'hai 2 volte". Il set lo garantisce da solo.

### Traccia concreta dei 3 loop (giocatori piccoli: Alice={A,B}, Bob={B,C}, Charlie={C,D})

**Il pattern del loop è SEMPRE lo stesso:** `risultato = set_di_partenza` → `for name in players:` → `risultato = risultato.operazione(players[name])`. Cambia solo l'OPERAZIONE:

**1. UNION = il sacchettone che CRESCE.** Ogni giro butta dentro la roba del giocatore, i doppioni si fondono:
```
partenza:  set()
giro Alice:   union {A,B}  ->  {A,B}
giro Bob:     union {B,C}  ->  {A,B,C}     (la B si fonde)
giro Charlie: union {C,D}  ->  {A,B,C,D}
```
Ogni riga ha SEMPRE più elementi (o uguali) della precedente. Finale = tutto ciò che ALMENO uno ha.

**2. INTERSECTION = il filtro che RESTRINGE.** Ogni giro tiene SOLO ciò che sta in ENTRAMBI:
```
partenza:  {A,B,C,D} (tutti)
giro Alice:   inter {A,B}  ->  {A,B}
giro Bob:     inter {B,C}  ->  {B}
giro Charlie: inter {C,D}  ->  set()   (VUOTO: nessuno li ha tutti)
```
Ogni riga ha MENO elementi (o uguali) della precedente. Finale = ciò che è SOPRAVVISSUTO a tutti. Può finire vuoto davvero — per questo il subject dice di tarare i numeri (14 achievement, 6-9 a testa: il comune di solito esce non vuoto).

**3. DIFFERENCE = la SOTTRAzione, calcolo SECCO (non accumulatore).** "I miei MENO i loro", usata in due modi:
- `only` = Alice `{A,B}` MENO unione degli altri `{B,C,D}` = `{A}` (solo suoi)
- `missing_achievements` = TOTALE `{A,B,C,D}` MENO quelli di Charlie `{C,D}` = `{A,B}` (i mancanti)

**Da ricordare per l'evaluation:** union e intersection nel loop usano un ACCUMULATORE (la variabile sta a SINISTRA e a DESTRA dell'uguale). La difference è un calcolo in una botta sola: due set, uno meno l'altro.

### ★ PRIMA VOLTA: il loop ANNIDATO (loop dentro un loop) — i blocchi "only" e "missing"

Il for esterno `for name in players:` è la TELECAMERA: punta su UN giocatore alla volta, e tutto il blocco lavora solo su di lui.

**Blocco "only" (con loop INTERNO):** per sapere cosa ha SOLO il giocatore di turno, serve la collezione di TUTTI GLI ALTRI. Il loop interno `for other_player in players:` ripassa tutti e **salta chi è di turno** con `if other_player != name` — il cuore del blocco: "raccogli tutti tranne me". Traccia (Alice={A,B}, Bob={B,C}, Charlie={C,D}):
```
GIRO ESTERNO name="Alice":  sacchetto altri = set() (FRESCO)
  interno: "Alice"  -> != ? NO  -> SALTA
  interno: "Bob"    -> SÌ -> union {B,C} -> altri={B,C}
  interno: "Charlie"-> SÌ -> union {C,D} -> altri={B,C,D}
  solo = {A,B} MENO {B,C,D} = {A}  ->  "Only Alice has: {A}"
GIRO ESTERNO name="Bob":  sacchetto altri = set() (VUOTO DI NUOVO: ogni giro lo ricrea!)
  interno: "Alice" -> SÌ -> {A,B}
  interno: "Bob"   -> NO  -> SALTA
  interno: "Charlie" -> SÌ -> {A,B,C,D}
  solo = {B,C} MENO {A,B,C,D} = set()  ->  "Only Bob has: set()"
```
Due cose da ricordare: `achievements_of_others` rinasce vuoto a ogni giro ESTERNO (se no, il sacchetto di Bob conterrebbe la roba di Alice), e il costo è 4×4=16 passaggi.

**Perché `other_player` e non `name`:** sono DUE ruoli diversi e devono restare separati. `name` = la variabile del loop ESTERNO (la telecamera: "di CHI stiamo calcolando il 'solo lui'?"); `other_player` = la variabile del loop INTERNO (la torcia che ripassa tutti). Il confronto `if other_player != name:` ha senso SOLO perché i nomi sono diversi: confronta la torcia con la telecamera. Se il loop interno usasse anche `name`, SOVRASCRIVEREBBE quello dell'esterno (perdendo il "chi è di turno") e il confronto `name != name` sarebbe SEMPRE falso → sacchetto vuoto per sempre. È esattamente il C: `for (int i...) { for (int j...) { if (j != i) } }` — due loop, due contatori, ognuno col suo ruolo

**Blocco "missing" (NESSUN loop annidato):** la domanda è "cosa manca a Charlie?" = TUTTI i 14 MENO i suoi. Il totale è già pronto (ACHIEVEMENTS): sottrazione secca, una botta sola:
```
name="Alice"   -> {A,B,C,D} MENO {A,B} = {C,D}  -> "Alice is missing: {C,D}"
name="Bob"     -> {A,B,C,D} MENO {B,C} = {A,D}  -> "Bob is missing: {A,D}"
name="Charlie" -> {A,B,C,D} MENO {C,D} = {A,B}  -> "Charlie is missing: {A,B}"
```
Variabile fresca a ogni giro: nasce, si stampa, si butta.

**Le 3 operazioni (le tre domande sui sacchetti):**
- **union** — butto tutto nel sacchettone: ogni elemento che sta in almeno un sacchetto (i duplicati si fondono) → "tutti gli achievement distinti"
- **intersection** — cosa c'è in TUTTI i sacchetti contemporaneamente → "achievement comuni"
- **difference** — cosa c'è nel primo sacchetto ma NON nell'altro → "solo X ha" e "gli manca"

### ★ PRIMA VOLTA: il DIZIONARIO — introduzione completa

**Il problema che risolve:** finora, per trovare qualcosa, contavi le posizioni: `lista[0]`, `lista[1]`... Ma se la domanda è "quali achievement ha Alice?", la posizione non serve a niente: ti serve il NOME. Il dizionario esiste per rispondere alle domande per nome.

**L'analogia perfetta è il suo stesso nome: il dizionario di carta.** Quando cerchi "cane", non sfogli pagina per pagina contando: vai DIRETTO alla voce (l'ordine alfabetico ti fa saltare le pagine) e leggi la sua definizione. Traduzione esatta:

| Dizionario di carta | Dizionario di Python |
|---|---|
| la parola che cerchi | la CHIAVE (`"Alice"`) |
| la definizione | il VALORE (il suo set di achievement) |
| sfogliare fino alla voce | `players["Alice"]` |

```python
players = {"Alice": {"a", "b"}, "Bob": {"c", "d"}}
players["Alice"]    # → il set di Alice ("cerca la voce Alice, dammi la sua definizione")
```

**Le 3 regole d'oro:**
1. **Si apre per CHIAVE, mai per posizione** — `players["Alice"]` sì; `players[0]` ERRORE (non esiste "la voce numero 0")
2. **Le chiavi sono UNICHE** — due voci "Alice" non convivono: se riassegni, SOVRASCRIVI (una definizione per parola)
3. **Per trovare non si scorre nulla** — come l'alfabetico, il computer salta dritto alla voce. Per questo il foreword di p03 dice che il contenitore giusto cambia tutto: "c'è già questo elemento?" sul dizionario è istantaneo, sulla lista devi scorrere tutto

**Lista vs dizionario, per non confonderli più:**

| | Lista | Dizionario |
|---|---|---|
| Si apre per | posizione: `lista[0]` | nome: `dict["chiave"]` |
| Analogia | fila numerata di sedie | armadietti con etichette / dizionario di carta |

**Qui in ex3:** `players` = dizionario giocatore → suoi achievement. Il `for` sul dizionario dà le CHIAVI (i nomi), e `players[name]` apre l'armadietto giusto.

**Esecuzione passo per passo:**
1. Main → intestazione
2. `players = {"Alice": gen_player_achievements(), ...}` — qui nasce il DIZIONARIO (introduzione completa qui sotto, prima di continuare la traccia)
3. Dentro `gen_player_achievements()`:
   - `random.randint(6, 9)` — un numero a caso TRA 6 e 9 (estremi INCLUSI). Modulo `random` (importato in cima): il "dado" di Python
   - `random.sample(ACHIEVEMENTS, n)` — pesca **n** achievement dalla lista dei 14, SENZA rimetterli dentro (mai duplicati). Come pescare n carte da un mazzo senza reinserirle
   - `set(...)` — trasforma il risultato in un set → e il set viene restituito col `return`
4. `for name in players:` — il dizionario si scorre così e a ogni giro `name` è il NOME del giocatore (per i dizionari il for dà le CHIAVI). `players[name]` = il suo set → si stampa
5. `all_achievements: set[str] = set()` — **variabile-accumulatore**: il sacchettone dove confluiscono gli achievement di TUTTI i giocatori. Parte VUOTO (`set()` e non `{}`, che è il dict vuoto) e cresce a ogni giro con `all_achievements = all_achievements.union(players[name])` — traccia con {A,B}, {B,C}, {C,D}: `set()` → `{A,B}` → `{A,B,C}` (la B si fonde) → `{A,B,C,D}`. ATTENZIONE alla riassegnazione: `union()` NON modifica il set originale, ne restituisce uno NUOVO — senza il `all_achievements =` il risultato andrebbe perso. Alla fine: ogni achievement che ALMENO un giocatore ha, una volta sola ("distinct" = senza doppioni, natura del set)
6. `common_achievements = set(ACHIEVEMENTS)` — parte da TUTTI e 14, poi `intersection` col set di ogni giocatore → alla fine restano solo quelli che SOPRAVVIVONO in tutti e 4
7. "Only X has": per ogni giocatore si costruisce `achievements_of_others` = union dei set degli ALTRI tre (loop interno con `other_player`, salta se stesso con `if other_player != name`), poi `players[name].difference(achievements_of_others)` = i suoi meno quelli degli altri
   - **"Only Charlie has: set()" cosa significa davvero:** NON che Charlie non ha achievement — ne ha 8-11. Significa che ogni achievement che ha, ce l'ha anche QUALCUN ALTRO: niente di esclusivo. Micro-esempio: Charlie={B,C}, unione degli altri={A,B,C,D} → {B,C} MENO {A,B,C,D} = set() — la sottrazione toglie tutto, sopravvive solo ciò che nessun altro possiede
8. "Missing": `missing_achievements = set(ACHIEVEMENTS).difference(players[name])` = tutti i 14 meno i suoi — variabile fresca a ogni giro

**Perché i numeri sono 14 e 8-11 (il tuning del subject, la versione FINALE):** il subject dice ESATTAMENTE: "Adjust the total number of achievements and how many you pick up for each player, so that all the requested sets are likely to be non-empty". Traduzione: sei TU a scegliere i numeri, ma TUTTI i set richiesti devono uscire PROBABILMENTE non vuoti quando il valutatore lancia il programma. Il tuning è un equilibrio TRA DUE esigenze OPPOSTE:
- se peschi POCO (6-9) → common vuoto ~30% dei run (male) ma "Only X has" pieno spesso
- se peschi TANTO (10-12) → common sempre pieno, ma "Only X has" SEMPRE vuoto (tutti hanno tutto: nessuno ha esclusivi — male, il subject vuole vedere anche quelli)
- **8-11 è il punto d'oro, misurato su 15 run:** common vuoto 0/15 ✓, almeno un "Only X has" non vuoto 12/15 ✓, missing non vuoto SEMPRE (peschi max 11 di 14 → mancano sempre almeno 3) ✓

**Perché l'output NON può essere tale e quale all'esempio del subject:** i set sono CASUALI — ogni lancio esce diverso, e l'esempio del subject è UNA delle esecuzioni possibili (guarda: nell'esempio del subject stesso "Only Alice has: set()" è VUOTO — i vuoti capitano, lì sono normali). Questo esercizio non ha strict output check: l'evaluator guarda che le operazioni (union/intersection/difference) siano giuste e che il tuning rispetti il "likely non-empty".

**Domanda da evaluation: "come stampa Python un set vuoto, e perché?"** → Stampa `set()`, NON `{}`. Perché `{}` è già occupato: significa DIZIONARIO vuoto. Serviva una scrittura diversa per il set vuoto, e `set()` è l'unica: le graffe con qualcosa dentro (`{1, 2}`) sono un set, le graffe VUOTE sono un dict.

**Come testare:**
```bash
cd python/p03/ex2 && cd ../ex3
python3 ft_achievement_tracker.py
# riprova più volte: l'ordine degli elementi cambia a ogni run (il set non ha ordine)
```

**Codice:**
```python
import random

ACHIEVEMENTS = [
	"Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme",
	"Untouchable", "Boss Slayer", "Strategist", "Unstoppable",
	"Speed Runner", "Survivor", "Treasure Hunter", "First Steps",
	"Sharp Mind", "Hidden Path Finder",
]

def gen_player_achievements() -> set[str]:
	n = random.randint(6, 9)
	return set(random.sample(ACHIEVEMENTS, n))

def main() -> None:
	print("=== Achievement Tracker System ===")

	players = {
		"Alice": gen_player_achievements(),
		"Bob": gen_player_achievements(),
		"Charlie": gen_player_achievements(),
		"Dylan": gen_player_achievements(),
	}

	for name in players:
		print(f"Player {name}: {players[name]}")

	all_achievements: set[str] = set()
	for name in players:
		all_achievements = all_achievements.union(players[name])
	print(f"All distinct achievements: {all_achievements}")

	common = set(ACHIEVEMENTS)
	for name in players:
		common = common.intersection(players[name])
	print(f"Common achievements: {common}")

	for name in players:
		achievements_of_others: set[str] = set()
		for other_player in players:
			if other_player != name:
				achievements_of_others = achievements_of_others.union(players[other_player])
		only = players[name].difference(achievements_of_others)
		print(f"Only {name} has: {only}")

	for name in players:
		missing = set(ACHIEVEMENTS).difference(players[name])
		print(f"{name} is missing: {missing}")


if __name__ == "__main__":
	main()
```

**Teoria:**
- **Chi è cosa:** `random` → modulo predefinito (importato); `randint()`, `sample()` → funzioni predefinite del modulo random; `set()`, `union()`, `intersection()`, `difference()` → metodi/funzioni predefiniti dei set; `ACHIEVEMENTS`, `players`, `n`, `name`, `other`, `only`, `missing`, `common`, `all_achievements` → variabili nostre; `gen_player_achievements()`, `main()` → funzioni nostre; `{chiave: valore}` → dizionario
- **Il set è DISORDINATO e SENZA DOPPIONI** — due proprietà da sapere per l'evaluation: non puoi indicizzare (`mio_set[0]` non esiste), e aggiungere un doppione non fa nulla
- **Set concreto, toccato con mano:**
  ```python
  zaino = {1, 2, 3}
  zaino.add(3)    # butto dentro un 3 che c'è già
  print(zaino)    # {1, 2, 3} — niente doppioni
  zaino.add(4)
  print(zaino)    # {1, 2, 3, 4}
  ```
  Confronto con lo stesso contenuto: lista `[3, 1, 2, 3, 1]` = 5 elementi, ordine fisso, doppioni tenuti; set `{3, 1, 2, 3, 1}` = 3 elementi, doppioni via. E l'ordine NON è garantito: con le stringhe, ogni run del programma stampa in ordine diverso (Python riordina i suoi scaffali interni a ogni avvio) — con i numeri piccoli a volte sembra fisso per pura coincidenza
- `random.randint(a, b)` = dado con estremi inclusi; `random.sample(lista, n)` = pesca n carte senza rimetterle (mai duplicati, è già un campione unico)
- Le operazioni hanno anche i simboli: `|` = union, `&` = intersection, `-` = difference (come in matematica)
- **Il pattern "accumulatore"** (usato 3 volte in questo esercizio: `all_achievements`, `achievements_of_others`, `common_achievements`): una variabile che parte vuota (o piena, come `common_achievements` che parte da tutti e 14) e viene AGGIORNATA a ogni giro del for riassegnando a se stessa il risultato: `x = x.operazione(...)`. È lo stesso pattern di `scores = []` + append in ex1, ma con i set
- **La differenza tra gli accumulatori:** `all_achievements` parte da `set()` e si ALLARGA (union); `common_achievements` parte da TUTTI i 14 e si RESTRINGE (intersection — sopravvive solo ciò che sta ovunque); `achievements_of_others` è temporaneo, ricreato per ogni giocatore (gli altri tre, escluso lui col `if other_player != name`)
- **Classificazione completa delle variabili di ex3:**
  | Variabile | Tipo di lavoro | Meccanismo |
  |---|---|---|
  | `all_achievements` | accumulatore | vuoto → si riempie (union) |
  | `achievements_of_others` | accumulatore | vuoto → si riempie (union) |
  | `common_achievements` | accumulatore | pieno (14) → si restringe (intersection) |
  | `missing_achievements` | calcolo fresco a ogni giro | 14 MENO i suoi (difference), si stampa, si rifà da zero |
  | `only` | calcolo fresco a ogni giro | i suoi MENO gli altri (difference), si stampa, si rifà da zero |
- **Come distinguerli:** l'ACCUMULATORE ha la variabile a SINISTRA e a DESTRA della stessa assegnazione (`x = x.operazione(...)`) ed è dichiarato FUORI dal loop. `missing_achievements` e `only` sono dichiarati DENTRO il loop: a ogni giro nascono, si stampano, e muoiono — il giro dopo ne nasce uno nuovo. `missing_achievements` NON contiene una lista dentro: contiene direttamente i nomi (stringhe) degli achievement mancanti, è un set puro
- Il for sul dizionario dà le CHIAVI (i nomi dei giocatori) — in ex4 vedremo anche i valori
- **Dizionario vs lista (per non confonderli mai):** la LISTA si apre per POSIZIONE (`lista[0]` = "il primo"); il DIZIONARIO si apre per ETICHETTA (`players["Alice"]` = "il contenuto sotto l'etichetta Alice"). Analogia: lista = fila numerata di sedie (la 1ª, la 2ª...); dizionario = armadietti con le etichette (apri quello che dice "Alice", non esiste "armadietto numero 2")
- **La riga `print(f"Player {name}: {players[name]}")` smontata:** nell'f-string ogni graffa viene CALCOLATA e stampata. Giro 1 del for: `name` vale "Alice" → `{name}` stampa Alice → `{players[name]}` calcola `players["Alice"]` (apri l'armadietto Alice) → stampa il suo set. Risultato: `Player Alice: {'...', '...'}`
- Demo da terminale: `players = {'Alice': {'a','b'}, 'Bob': {'c','d'}}` poi `for name in players: print(name, players[name])` → a ogni giro: etichetta e contenuto
- L'output cambia a ogni esecuzione: è normale, è il dado
- **Nota terminale — il `(.venv)` nel prompt:** significa che un ambiente virtuale è ATTIVO in quella finestra: una copia privata di Python in una cartellina, usata perché il Python di sistema del Mac rifiuta pip install (PEP 668). Si esce con `deactivate`, si rientra con `source .venv/bin/activate`. Diventa materia d'esame in p08
- **Perché le stringhe nel set escono con le virgolette singole:** quando stampi una stringa DA SOLA → niente virgolette; DENTRO un contenitore (lista/set/dict) Python aggiunge le virgolette come ETICHETTA "questo è testo" (così `{1, 'a'}` distingue numeri da testo). Le virgolette NON fanno parte della stringa (prova: `len('Crafting Genius')` = 15). Single è la scelta di default; se il testo contiene un apostrofo, Python passa alle doppie (`["L'uomo"]`). L'f-string `{players[name]}` stampa il set, che mette la cornice a ogni elemento. In C questa cornice non esiste: è un'aggiunta di Python per leggibilità

---

## ex4 — ft_inventory_system — il dizionario protagonista

**Cosa fa in concreto:** legge oggetti e quantità da riga di comando (formato `nome:quantità`), scarta invalidi e doppioni, e calcola le statistiche dello zaino: lista oggetti, quantità totale, percentuale di ciascuno, più e meno abbondante. Poi aggiunge un "magic_item" e rimostra tutto.

**★ PRIME VOLTE qui:** metodi `dict.keys()` / `dict.values()`, e soprattutto il dizionario USATO DAVVERO (in ex3 lo abbiamo solo assaggiato)

### Il dizionario (già introdotto in ex3)

Il dizionario l'abbiamo conosciuto in ex3 (`players`): chiave → valore, si apre per nome con `dict["chiave"]`, chiavi uniche, ricerca istantanea. Qui in ex4 lo usiamo DAVVERO per la prima volta: inventario con chiave = nome dell'oggetto, valore = quantità.

### Cosa chiede l'esercizio

1. Prendere i parametri da riga di comando nel formato `nome:quantità` (es. `sword:1 potion:5`)
2. Scartare quelli invalidi: sintassi sbagliata (niente due punti), quantità non numerica, e parametri RIPETUTI (stesso nome due volte → si tiene il primo)
3. Riempire un **dizionario**: chiave = nome, valore = quantità (come int, per fare i conti)
4. Mostrare: l'inventario, la lista dei nomi, la quantità totale, la percentuale di ogni oggetto, il più e il meno abbondante (a parità, il primo della riga di comando)
5. Aggiungere `magic_item` e rimostrare

### Come testare

```bash
cd python/p03/ex4
python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
python3 ft_inventory_system.py                      # inventario vuoto
```

### Esecuzione (con l'esempio del subject)

1. Main → intestazione → `inventory: dict[str, int] = {}` — il dizionario VUOTO (`{}` vuoto = dict, NON set: ricordalo dall'ex3)
2. `for arg in sys.argv[1:]:` — un parametro alla volta ("sword:1", "potion:5", ...)
3. `arg.split(":")` — spezza ai due punti: "sword:1" → `["sword", "1"]`
4. `len(parts) != 2` → "hello" non ha i due punti → `Error - invalid parameter 'hello'` → `continue` (si passa al prossimo)
5. `name in inventory` → "sword" è GIÀ una voce? La seconda volta che appare "sword" sì → `Redundant item 'sword' - discarding` → si tiene il primo. (Il controllo "c'è già?" è istantaneo grazie al dizionario — vedi introduzione)
6. `inventory[name] = int(quantity)` — CREA la voce: chiave "sword", valore 1. Se la quantità non è un numero ("value") → except → `Quantity error for 'key': invalid literal...`
7. `names = list(inventory.keys())` — due pezzi: `keys()` è il METODO built-in dei dizionari ("dammi le etichette") ma restituisce una VISTA speciale (dict_keys), NON una lista — non ha posizioni, niente `[0]`. `list()` è la CLASSE built-in che costruisce una lista vera da qualsiasi cosa: il risultato è `['sword', 'potion', 'shield', ...]` con posizioni e ordine. Perché serve: le righe dopo usano `names[0]` (il punto di partenza di most/least — col dizionario non potresti) e il for con un ordine stabile. E Python RICORDA l'ordine di inserimento nei dizionari: la lista esce nell'ordine della riga di comando — è questo che fa funzionare la regola "a parità vince il primo della riga di comando" (names[0] È il primo)
8. `total = sum(inventory.values())` — due pezzi con due ruoli: `values()` è il METODO built-in dei dizionari, gemello di keys() ("portami tutti i contenuti") — restituisce una VISTA (dict_values), NON una lista, e NON calcola niente: è il cameriere. `sum()` è la FUNZIONE built-in già vista in ex1 ("somma tutto") — è il contabile: `sum([1, 5, 2, 3, 1])` → 12. Dettaglio importante: keys() e values() sono ALLINEATI in coppia (il 1° valore va con la 1ª chiave, ecc.) — per questo `inventory[name]` dà sempre la quantità giusta
- **sum() vs len() (equivoco classico):** `sum()` SOMMA i numeri e SOLO numeri — parte da 0 e aggiunge ogni elemento, quindi con le stringhe esplode (TypeError: 0 + "a"). `len()` CONTA gli elementi di QUALSIASI cosa (lista, stringa, dizionario). Due mestieri diversi: in ex4 `sum(inventory.values())` = somma delle quantità (12), `len(names)` = quanti oggetti (5)
9. Percentuali: `inventory[name] / total * 100` per ogni nome → `round(x, 1)` → "sword represents 8.3%"
10. Più/meno abbondante: `most = names[0]` e `least = names[0]` sono le IPOTESI DI PARTENZA ("supponiamo che il più/meno abbondante sia il primo"). IMPORTANTE: il for precedente NON ha consumato la lista — `names` è ancora intera, e `names[0]` la RILEGGE (le liste non hanno lancette: la posizione 0 è sempre lì). Poi il nuovo for confronta tutti con `>` e `<` STRETTI: a parità di quantità il pari NON sostituisce, quindi resta il primo della riga di comando — esattamente la regola del subject. E `most` deve essere un NOME (serve come chiave in `inventory[most]`), non un numero
11. **LA REGOLA DELLE QUADRE (equivoco da evitare):** stesse quadre, significato diverso a seconda del contenitore — sulla LISTA `lista[1]` = POSIZIONE (il secondo elemento); sul DIZIONARIO `dict[1]` = CHIAVE (la voce la cui etichetta È il numero 1, e se non esiste la CREA). Il dizionario non ha "primo elemento": un numero tra le quadre è un'etichetta come un'altra. Demo: `{'sword': 1, 'potion': 5}` → `inventory[1] = 99` → `{'sword': 1, 'potion': 5, 1: 99}` — NON tocca il primo, crea la voce con chiave 1. È la lezione degli armadietti di ex3: sedie numerate vs etichette.
11b. `inventory["magic_item"] = 1` — si legge: "nel dizionario inventory, la voce con etichetta 'magic_item' vale 1 — e se non esiste ancora, CREALA". È la riga dei DUE LAVORI IN UNO (già usata nel loop per creare sword/potion/...): etichetta nuova → crea la voce; etichetta esistente → sovrascrive il valore. Demo: `{'sword': 1}` → `inventory['magic_item'] = 1` → `{'sword': 1, 'magic_item': 1}`; poi `inventory['sword'] = 99` → `{'sword': 99, 'magic_item': 1}`. Python decide da solo guardando se l'etichetta esiste già

### Codice

```python
import sys

def main() -> None:
	print("=== Inventory System Analysis ===")

	inventory: dict[str, int] = {}
	for arg in sys.argv[1:]:
		parts = arg.split(":")
		if len(parts) != 2:
			print(f"Error - invalid parameter '{arg}'")
			continue
		name, quantity = parts
		if name in inventory:
			print(f"Redundant item '{name}' - discarding")
			continue
		try:
			inventory[name] = int(quantity)
		except ValueError as e:
			print(f"Quantity error for '{name}': {e}")

	print(f"Got inventory: {inventory}")

	names = list(inventory.keys())
	print(f"Item list: {names}")

	if len(names) == 0:
		print("Empty inventory")
		return

	total = sum(inventory.values())
	print(f"Total quantity of the {len(names)} items: {total}")

	for name in names:
		percent = inventory[name] / total * 100
		print(f"Item {name} represents {round(percent, 1)}%")

	most = names[0]
	least = names[0]
	for name in names:
		if inventory[name] > inventory[most]:
			most = name
		if inventory[name] < inventory[least]:
			least = name
	print(f"Item most abundant: {most} with quantity {inventory[most]}")
	print(f"Item least abundant: {least} with quantity {inventory[least]}")

	inventory["magic_item"] = 1
	print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
	main()
```

### Teoria

- **Chi è cosa:** `split()` → metodo built-in delle stringhe (già visto in ex2); `keys()`, `values()` → METODI built-in dei dizionari; `list()` → CLASSE built-in (converte in lista); `in` → parola chiave ("questa chiave esiste nel dizionario?"); `{}` vuoto → dizionario vuoto; il resto già visto
- **`inventory[name] = valore` fa due lavori in uno:** se la chiave esiste → aggiorna; se non esiste → crea. È per questo che l'aggiunta di `magic_item` usa la stessa riga di tutto il resto
- **`name, quantity = parts`** — unpacking su una lista di 2 pezzi (come `x1, y1, z1 = tupla` di ex2). Traccia con "sword:1": `parts = ["sword", "1"]` → `name = "sword"` e `quantity = "1"`. Due assegnazioni in una riga, IN ORDINE (primo elemento → prima variabile). `name` e `quantity` sono variabili NOSTRE nuove. Attenzione: `quantity` in questo momento è ancora una STRINGA ("1" come testo) — diventa un numero solo dopo, con `int(quantity)` nella riga dell'assegnazione. In C: `name = parts[0]; quantity = parts[1];`. Le variabili a sinistra devono essere ESATTAMENTE quante gli elementi (2 e 2) — per questo la riga sopra controlla `len(parts) != 2`
- **Il controllo del duplicato** (`name in inventory`) è la prima applicazione vera della potenza del dizionario: "questa etichetta esiste già?" senza scorrere niente. `in` sul dizionario guarda le CHIAVI ("esiste la voce 'sword'?"), NON i valori — demo: con `{'sword': 1}`, `'sword' in inventory` è True ma `1 in inventory` è False. Traccia del doppione: al secondo `sword:2`, `name = "sword"` → la voce esiste → "Redundant item 'sword' - discarding" → `continue` salta tutto → vince il PRIMO sword, come vuole il subject. In C: un loop sull'array per ogni ricerca; qui è una riga istantanea
- **A parità di quantità vince il primo della riga di comando** — ottenuto coi confronti STRETTI `>` e `<`: il pari NON sostituisce mai, quindi resta il primo trovato
- **Domanda da evaluation:** "perché un dizionario per l'inventario?" → perché le domande dell'inventario sono per NOME ("quante spade?"), e il dizionario risponde per nome all'istante; una lista dovrebbe essere scorsa ogni volta

---



---

## ex5 — ft_data_stream — i generatori (yield)

**Approfondimento — yield e Generator smontati (dalle domande in chat):**

- **`from typing import Generator`** si legge: "dal modulo typing (già pronto in Python, il modulo delle ETICHETTE per i tipi) prendi l'etichetta Generator". Non esegue niente: serve solo al type hint. `Generator[tuple[str, str], None, None]` ha 3 scomparti: 1° = cosa YIELD (coppie str,str), 2° = cosa RICEVE dall'esterno (None = niente), 3° = cosa RETURN alla fine (None = niente)
- **yield = un return che NON chiude (spiegazione meccanica, niente metafore):** return consegna il valore E la funzione FINISCE (la prossima chiamata riparte da zero); yield consegna il valore E la funzione si CONGELA nel punto esatto (la prossima next riparte DA LÌ). Demo con i print dentro la funzione: `def demo(): print("A"); yield 10; print("B"); yield 20; print("C")` → `g = demo()` NON stampa nulla (chiamare una funzione con yield NON la esegue: consegna l'oggetto congelato) → `next(g)` stampa A e consegna 10 → `next(g)` stampa B e consegna 20 → `next(g)` stampa C e dà StopIteration. Il punto di congelamento è ESATTAMENTE la riga dello yield
- **La tupla NON c'entra col generatore:** yield consegna qualsiasi cosa gli scrivi dopo (`yield 5`, `yield (name, action)`). Nel nostro esercizio ogni evento È una coppia (giocatore, azione) = due stringhe → la consegniamo come tupla. Stessa scelta che faresti col return: il meccanismo è uguale, il valore lo scegli tu. Il generatore è il meccanismo; la tupla è il prodotto
- **ESECUZIONE VERA con valori fissi (random.seed(42)) — il formato che fa capire tutto:**

  ```
  stream = gen_event()   ->  niente eseguito: stream = macchina al punto zero

  GIRO 0 (i = 0):
    next(stream) sblocca
    while True: vero -> entra
    name = random.choice(PLAYERS)   -> name = 'alice'
    action = random.choice(ACTIONS) -> action = 'run'
    yield (name, action)            -> consegna ('alice','run') a next() e si RICONGELA
    name, action = next(stream)     -> unpacking nel main: name='alice', action='run'
    print -> Event 0: Player alice did action run

  GIRO 1 (i = 1):
    next(stream) riparte dallo yield
    while True: vero -> nuovo giro
    dadi RITIRATI -> name = 'charlie', action = 'eat'   (valori NUOVI)
    yield -> consegna ('charlie','eat') e ricongela
    print -> Event 1: Player charlie did action eat

  GIRO 2 (i = 2):
    dadi di nuovo -> name = 'bob', action = 'eat'
    yield -> consegna e congela
    print -> Event 2: Player bob did action eat
  ```

  Le 3 cose da portarsi via: (1) le name/action DENTRO la funzione e quelle del MAIN sono variabili SEPARATE con lo stesso nome — dentro vengono rimpiENITE a ogni giro coi dadi, poi la coppia esce e l'unpacking riempie quelle del main; (2) il congelamento è sempre SULLO YIELD: tra un next e l'altro la macchina sta ferma lì con dentro l'ULTIMA coppia tirata; (3) i dadi si tirano a OGNI giro — per questo i valori cambiano

- **DEFINIZIONE di generatore (raffinata):** una funzione che può congelarsi a metà con yield invece di chiudersi con return. Chiamarla → NON la esegue, ti dà l'oggetto congelato; next() → la scongela, esegue fino al prossimo yield, consegna il valore, la ricongela; fine funzione senza altri yield → StopIteration (il for lo gestisce da solo fermandosi)
- **Il punto chiave:** una funzione con yield, quando la CHIAMI, NON si esegue — ti dà la fabbrica. `stream = gen_event()` crea la fabbrica (nessun giro); `next(stream)` = "fabbrica, dammi il prossimo": scongela, gira fino al prossimo yield, consegna, ricongela
- **Traccia col pallino di gen_event:** `next(stream)` → while True? SÌ → choice(PLAYERS) → name="bob" → choice(ACTIONS) → action="run" → yield consegna ("bob","run") e CONGELA. Seconda next: RIPARTE dal punto congelato → while True? SÌ → nuovo giro → yield nuovo pezzo → congela. Il while True non va in crash perché a ogni giro si ferma allo yield: chi decide quanto gira sei TU (nel main: 1000 next = 1000 pezzi)

- **Perplessità: "che succede ESATTAMENTE a stream = gen_event()?" — i 4 passi:** (1) Python vede lo yield nel corpo → capisce che è una funzione-generatore; (2) NON esegue il corpo, nemmeno la prima riga; (3) fabbrica l'oggetto: la funzione congelata alla prima riga (partita salvata al minuto zero); (4) stream = quell'oggetto. Nessun dado tirato, nessun name/action. La macchina è spenta
- **Perplessità: "perché il for non richiama gen_event() ma solo next()?" —** perché chiamare gen_event() di nuovo fabbricherebbe una SECONDA macchina nuova al punto zero, senza far avanzare la prima (comprare un distributore nuovo invece di girare la manovella). Regola: la chiamata si fa UNA volta (crei la macchina); poi next() sulla stessa la fa avanzare. Nel for di consume_event è identico: la chiamata avviene una volta dentro il for, e il for gira la manovella da solo
- **Correzione all'immagine "name e action scritte una volta e congelate in coda":** (a) i dadi si tirano a OGNI giro, non una volta sola — ogni next() rifà il giro completo (while → dadi → name e action RIMPIENITE di nuovi valori; demo: prima richiesta ("alice","run"), seconda ("bob","eat")); (b) NON esiste nessuna coda: yield consegna il valore IN MANO a next() nello STESSO istante in cui si congela — il testimone della staffetta: il corridore corre fino a te, ti mette il testimone in mano e si ferma lì. Passaggio e congelamento sono lo stesso momento

- **Perplessità: "chiamare stream = gen_event() che succede?" — NULLA.** Chiamare una funzione con yield NON esegue il corpo: né il while, né i dadi, né lo yield. Crea solo l'oggetto congelato AL PUNTO ZERO (macchina spenta). Il corpo parte tutto insieme solo alla PRIMA next() (demo: un print dentro la funzione esce solo alla prima next, non alla chiamata). Quindi: chiamata = crea la macchina spenta; next = accende e fa un giro; yield = spegne a metà giro conservando le variabili (name, action restano congelate per il giro dopo)
- **Perplessità: "yield si può usare solo con un while?" — NO.** Il while NON è un requisito di yield: è solo un modo per RIPETERE lo yield. Tre forme possibili: (1) niente while, yield in fila → sequenza finita di 3 valori; (2) while True + yield → infinito, ferma il chiamante (gen_event); (3) while con condizione + yield → finisce quando la condizione diventa falsa (consume_event: finché la lista non si svuota). La domanda da farsi: quanti pezzi deve produrre? 3 precisi → 3 yield in fila; infiniti → while True; finché la lista si svuota → while len>0

- **Perplessità: "il while True quando finisce?" — MAI da solo.** Il while True non finisce mai, ma non gira nemmeno mai "all'infinito" tutto insieme: a ogni giro lo yield lo congela. Il loop avanza UN passo per richiesta: il main chiede 1000 volte → 1000 giri (uno per next); poi smette → il generatore resta CONGELATO nel limbo per sempre; una 1001ª richiesta farebbe un 1001° giro senza problemi. Chi decide la fine è il CHIAMANTE, non il while. Confronto coi due generatori dell'esercizio: gen_event = while True, finisce MAI (ferma la produzione il chiamante); consume_event = while len(events) > 0, finisce quando la lista è vuota (si svuota da sola col remove). Traccia di una richiesta: while True? SÌ → choice → name → choice → action → yield consegna e CONGELA — la richiesta finisce qui; la prossima riparte e risale al while
- **`next()`** = funzione built-in (come len): "dammi il prossimo pezzo"
- **Il for sul generatore:** `for event in consume_event(event_list)` — il for chiama next() DA SOLO finché il generatore non finisce; un generatore finisce quando la funzione arriva in fondo senza altri yield
- **Cosa fa e cosa ritorna consume_event (perplessità risolta):** il nome dice tutto: CONSUMA la lista. A ogni richiesta pesca UN elemento a caso (choice), lo TOGLIE dalla lista (remove), lo consegna (yield) — finché la lista non è vuota. NON ritorna niente: nessun return, quando il while finisce dà StopIteration (il for lo usa per fermarsi). Demo col dado fisso, lista [('alice','run'),('bob','eat'),('charlie','sleep')]: giro 1 pesca ('bob','eat'), la lista resta [('alice','run'),('charlie','sleep')]; giro 2 pesca ('alice','run'), resta [('charlie','sleep')]; giro 3 pesca l'ultimo, lista = []; quarta richiesta: len>0? NO -> StopIteration -> il for si ferma
- **Il punto cruciale (effetto collaterale):** consume_event NON lavora su una copia — `events` È la stessa lista del main. Ogni remove toglie dall'originale: il generatore MANGIA la lista del chiamante (alla fine event_list è VUOTA). È per questo che il subject fa stampare "Remains in list" a ogni giro: ti fa vedere la lista che si svuota. Differenza da gen_event: quello non tocca niente di esterno (produce e basta); consume_event distrugge il suo input

- **Traccia col pallino di consume_event (lista con 2 eventi):** while len(events)>0? SÌ → choice pesca ("charlie","swim") → events.remove() lo TOGLIE (resta 1) → yield consegna → il for lo stampa → richiede ancora → pesca/toglie/consegna l'ultimo → richiede ancora → len>0? NO → il generatore finisce → il for si ferma da solo. Consume_event DISTRUGGE la sua lista di partenza (remove) — per questo "Remains in list" si accorcia a ogni stampa
- **Perché i generatori (risposta da evaluation):** 1000 eventi in lista = 1000 posti in memoria tutti insieme; il generatore ne tiene UNO alla volta. È la differenza tra portare tutto il raccolto in un carro e portarlo un sacco alla volta


**Cosa fa in concreto:** genera 1000 eventi casuali (un giocatore e un'azione) UNO ALLA VOLTA e li stampa; poi crea una lista di 10 eventi e li consuma pescandoli a caso uno per uno finché la lista non è vuota.

**★ PRIME VOLTE qui:** generatore (`yield`), `next()`, `random.choice()`

**Cosa chiede:** un generatore INFINITO `gen_event()` che produce eventi (giocatore, azione) a caso; si leggono 1000 eventi con `next()`, poi si fa una lista di 10 eventi, poi un secondo generatore `consume_event` che pesca a caso dalla lista, toglie l'elemento e lo cede, finché la lista è vuota (usato direttamente nel `for`).

**Il concetto in una riga:** un generatore è una fabbrica che produce UN valore alla volta, su richiesta — niente lista in memoria. `yield` = "consegna questo valore e METTI IN PAUSA; alla prossima richiesta riparti da qui". Il loop infinito `while True:` con `yield` dentro NON va in crash: produce un valore, si congela, aspetta la prossima richiesta.

**Esecuzione:** main → `stream = gen_event()` (chiamare una funzione con yield NON la esegue: crea la fabbrica) → 1000 volte `next(stream)` = "fabbrica, dammi il prossimo" → ogni volta: tira `random.choice(PLAYERS)` e `random.choice(ACTIONS)` → `yield (name, action)` congela → si stampa → si richiede. Poi `consume_event(event_list)`: `while len(events) > 0:` → pesca `random.choice(events)`, lo toglie con `events.remove(event)`, `yield` lo consegna → il `for event in consume_event(...)` richiede finché non è vuota.

**Come testare:** `cd python/p03/ex5 && python3 ft_data_stream.py` (1000 eventi + lista + consumo)

**Teoria:**
- **Chi è cosa:** `yield`, `while` → parole chiave; `next()` → funzione built-in ("dammi il prossimo"); `random.choice(lista)` → funzione predefinita del modulo random (pesca UN elemento a caso); `Generator` → tipo predefinito del modulo typing (etichetta); il resto già visto
- **Differenza funzione vs generatore:** la funzione con `return` fa tutto e consegna TUTTO insieme; il generatore con `yield` consegna UN pezzo, si congela, riparte. Analogia: la funzione è un fornaio che sforna tutti i panini insieme su un vassoio; il generatore è la catena di montaggio — un panino alla volta, su richiesta
- **Perché serve:** 1000 eventi in una lista = 1000 posti in memoria; col generatore = UN posto alla volta. È il "memory-saving superpower" del subject
- Il tipo `Generator[tuple[str, str], None, None]` = etichetta: "generatore che cede tuple (str, str)"

**Codice:** in `python/p03/ex5/ft_data_stream.py` (già scritto e testato)

---

## ex6 — ft_data_alchemist — le comprehensions

**Cosa fa in concreto:** da una lista di 9 nomi (alcuni maiuscoli, altri no) crea con le comprehension: la lista di tutti i nomi con la maiuscola, la lista dei soli già maiuscoli, un dizionario nome→punteggio casuale, e il dizionario dei soli punteggi sopra la media.

**★ PRIME VOLTE qui:** list comprehension, dict comprehension

**Cosa chiede:** da una lista di nomi misti (maiuscoli/minuscoli): una lista con TUTTI capitalizzati, una lista con SOLO quelli già maiuscoli; poi un DIZIONARIO nome→punteggio casuale, e un secondo dizionario con solo i punteggi sopra la media — tutto con le comprehensions, una riga sola ciascuna.

**Il concetto in una riga:** la comprehension è il for condensato in UNA riga: `[lavoro(item) for item in collezione if filtro]`. Leggila come una frase: "per ogni item della collezione (che passa il filtro), calcola lavoro(item) e mettilo nella nuova collezione".

**Esecuzione:** main → lista players → `[name.capitalize() for name in players]` = per ogni nome: prima maiuscola → lista nuova → `[name for name in players if name[0].isupper()]` = solo i nomi che PASSANO il filtro → `{name: random.randint(50, 1000) for name in capitalized}` = dict comprehension (chiave: valore per ogni nome) → media = `sum(scores.values()) / len(scores)` → `{name: score for name, score in scores.items() if score > average}` = dict filtrato (★ PRIMA VOLTA: `.items()` — dà le coppie chiave-valore del dizionario).

**Come testare:** `cd python/p03/ex6 && python3 ft_data_alchemist.py` (i punteggi cambiano a ogni run)

**Teoria:**
- **Forma della comprehension:** `[espressione for elemento in collezione]` — e con filtro: `[espressione for elemento in collezione if condizione]`. Stessa sintassi con `{}` per i dizionari: `{chiave: valore for ...}` e anche per i set: `{x for ...}`
- **Equivalente col for classico** (il for di 4 righe diventa 1): `risultato = []` → `for x in lista:` → `risultato.append(f(x))` = `[f(x) for x in lista]`
- Il subject: "Each comprehension should be on a single line"
- **Chi è cosa:** tutto già visto, tranne `.items()` → metodo built-in dei dizionari (dà le coppie chiave-valore, da spacchettare con `for chiave, valore in ...`)

**Codice:** in `python/p03/ex6/ft_data_alchemist.py` (già scritto e testato)

---

# p04 — Data Archivist (File I/O)

## ex0 — ft_ancient_text — leggere un file

**Cosa fa in concreto:** prende un nome di file da riga di comando, ne legge il contenuto e lo stampa come farebbe il comando `cat`, con una riga di intestazione e una di chiusura; se il file non esiste o è protetto, stampa l'errore senza crashare.

**★ PRIME VOLTE qui:** `open()`, oggetto file, `.read()`, `.close()`, `typing.IO`

**Cosa chiede:** prendere il nome di un file da riga di comando, leggerlo e mostrarlo come farebbe `cat`, con intestazione e chiusura; gestire gli errori (file inesistente, permessi negati) senza crashare.

**Il concetto in una riga:** `open("file", "r")` = l'`fopen` del C: apre il file e ti dà un OGGETTO-file (l'equivalente del `FILE *`). `.read()` = legge TUTTO il contenuto in una stringa. `.close()` = chiude (l'`fclose`). L'oggetto file va SEMPRE chiuso — per ora a mano, in ex3 arriva il `with` che lo fa da solo.

**Esecuzione:** main → senza argomento → usage → `open(filename, "r")` dentro il try: se il file non esiste → OSError (l'errore del C `[Errno 2] No such file or directory`) → except stampa e `return` → se ok: `content = f.read()` (tutto il file in una stringa) → `f.close()` → stampa `"--" + content` → chiusura.

**Come testare:** `cd python/p04/ex0 && python3 ft_ancient_text.py` (usage) · `python3 ft_ancient_text.py foo` (errore) · `python3 ft_ancient_text.py ancient_fragment.txt` (legge)

**Teoria:**
- **Chi è cosa:** `open()`, `print()`, `len()` → funzioni built-in; `.read()`, `.close()` → METODI built-in dell'oggetto file; `IO` → tipo predefinito del modulo typing (etichetta per l'oggetto file); `sys.argv` → già visto; il resto nostro
- **Domanda del subject: "che tipo di dato ritorna open()?"** → un OGGETTO FILE (non una stringa!): è l'oggetto che TIENE APERTO il file e ha i metodi read/close/write. In C: il `FILE *`. Il CONTENUTO è `f.read()` (quella sì è una stringa)
- `open(filename, "r")` — la "r" = modalità lettura (read). In ex1 servirà "w" = scrittura
- L'errore di un file inesistente è `FileNotFoundError` (sottotipo di OSError) — lo conosci da p02

**Codice:** in `python/p04/ex0/ft_ancient_text.py` (già scritto e testato)

## ex1 — ft_archive_creation — scrivere un file

**Cosa fa in concreto:** come ex0, ma poi aggiunge un carattere `#` in coda a ogni riga del contenuto, lo mostra, e chiede il nome di un file su cui SALVARE il risultato (vuoto = non salva).

**★ PRIME VOLTE qui:** `.write()`, modalità "w" di open

**Cosa chiede:** come ex0, ma poi: aggiungere `#` in coda a ogni riga, mostrare il risultato, chiedere il nome del file da salvare (vuoto = non salvare), creare/sovrascrivere il file.

**Esecuzione:** lettura come ex0 → `content.splitlines()` = lista delle righe (★ PRIMA VOLTA: `splitlines()`, separa alle andate a capo) → `[line + "#" for line in lines]` (comprehension di ex6 p03!) → stampa → `input()` chiede il nome → se vuoto: "Not saving data." → altrimenti `open(name, "w")` — **"w" = SCRITTURA: crea il file se non esiste, lo SVUOTA se esiste** → `.write("
".join(new_lines) + "
")` (★ PRIMA VOLTA: `"
".join(lista)` — incolla le stringhe con 
 in mezzo) → close → messaggio.

**Come testare:** `cd python/p04/ex1 && echo "" | python3 ft_archive_creation.py ancient_fragment.txt` (non salva) · `echo "new_fragment.txt" | python3 ft_archive_creation.py ancient_fragment.txt` (salva) · `cat new_fragment.txt`

**Teoria:** l'oggetto file ha DUE metodi speculari: `.read()` (legge tutto) e `.write(testo)` (scrive il testo). La modalità si sceglie nel secondo parametro di open: "r" legge, "w" scrive (crea/sovrascrive). In C: `fopen(name, "r")` / `fopen(name, "w")` + `fwrite`.

**Codice:** in `python/p04/ex1/ft_archive_creation.py` (già scritto e testato)

## ex2 — ft_stream_management — i 3 canali

**Cosa fa in concreto:** come ex1, ma gli errori vanno scritti sul canale di errore (stderr, col prefisso [STDERR]) e la domanda all'utente viene fatta senza usare input(), leggendo direttamente da stdin.

**★ PRIME VOLTE qui:** `sys.stdin`, `sys.stdout`, `sys.stderr`, `.readline()`, `.flush()`

**Cosa chiede:** come ex1, ma: gli errori vanno sul canale di ERRORE (`sys.stderr`, col prefisso `[STDERR]`) e l'input va letto SENZA `input()`, usando `sys.stdin`.

**Il concetto in una riga:** ogni programma ha 3 canali predefiniti (i "three sacred channels" del subject): `sys.stdin` (dove arriva quello che scrivi), `sys.stdout` (dove va il print normale), `sys.stderr` (dove vanno gli ERRORI — separato, così i messaggi d'errore non si mischiano all'output "vero"). In C: stdin/stdout/stderr, li conosci.

**Esecuzione:** come ex1, con 2 differenze: `sys.stderr.write(f"[STDERR] ...
")` al posto del print per gli errori (si scrive sul canale di errore — sul terminale SI VEDE uguale, ma il canale è diverso: chi usa il programma può separarli, es. `2>errori.txt`) → per l'input: `sys.stdout.write("domanda ")` + `sys.stdout.flush()` (spinge subito il testo sullo schermo) + `name = sys.stdin.readline().strip()` (legge UNA riga da stdin; `.strip()` toglie l'andata a capo finale).

**Come testare:** `cd python/p04/ex2 && python3 ft_stream_management.py foo` (errore su stderr) · con un file valido e input piped

**Teoria:** `input()` è solo una comodità costruita SOPRA stdin/stdout: il subject ti fa fare a mano quello che input() fa da solo. `flush()` serve perché l'output è bufferizzato (parte a blocchi): senza flush la domanda potrebbe non apparire prima della risposta.

**Codice:** in `python/p04/ex2/ft_stream_management.py` (già scritto e testato)

## ex3 — ft_vault_security — il with (context manager)

**Cosa fa in concreto:** fornisce una funzione "cassaforte" che legge o scrive QUALSIASI file e restituisce sempre una coppia (riuscito?, contenuto-o-errore) — col with il file si chiude da solo anche se qualcosa va storto.

**★ PRIME VOLTE qui:** `with` (context manager)

**Cosa chiede:** funzione `secure_archive(filename, action, content)` che usa il `with` per leggere/scrivere qualunque file e restituisce una tupla `(True/False, contenuto o messaggio d'errore)` — il file si chiude SEMPRE da solo, anche con errori.

**Il concetto in una riga:** `with open(...) as f:` = "apri il file, lavoraci dentro il blocco, e CHIUDILO AUTOMATICAMENTE quando esci — anche se scoppia un errore". È il finally di p02, già costruito per te: niente `f.close()` a mano, impossibile dimenticarlo.

**Esecuzione:** main → 4 dimostrazioni → ogni `secure_archive(...)` fa: `with open(filename, "r") as f:` → `return (True, f.read())` — il with chiude DA SOLO il file prima che il return consegni il valore → se open fallisce: `except OSError as e:` → `return (False, str(e))` (la TUPLA col fallimento — niente crash, come p02 vuole).

**Come testare:** `cd python/p04/ex3 && python3 ft_vault_security.py`

**Teoria:** il `with` funziona con qualunque "risorsa" che va chiusa (file, connessioni). Traduzione C: il `fclose()` che metteresti in ogni ramo d'errore, scritto UNA volta da Python. Il subject (p04): "use of the with statement will be introduced in exercise 3. You must not use it before" — per questo ex0-ex2 chiudono a mano.

**Codice:** in `python/p04/ex3/ft_vault_security.py` (già scritto e testato)



---

# p05 — Code Nexus (Classi astratte e polimorfismo)

## ex0 — data_processor — le classi astratte (ABC)

**Cosa fa in concreto:** definisce un CONTRATTO (classe astratta) con 3 operazioni che ogni "processore di dati" deve avere, e crea 3 processori concreti: uno per i numeri, uno per i testi, uno per i log. Il main li testa con dati validi e invalidi.

**★ PRIME VOLTE qui:** `ABC`, `@abstractmethod`, `isinstance()`, `all()`, `Any`

**Cosa chiede:** una classe astratta `DataProcessor` che definisce L'INTERFACCIA comune (validate, ingest, output) e 3 classi concrete (NumericProcessor, TextProcessor, LogProcessor) che la implementano per i loro tipi di dati. Il main testa validi/invalidi e l'ingest senza validazione (che deve esplodere).

**Il concetto in una riga:** una classe ASTRATTA è un CONTRATTO, non un oggetto: non puoi crearla (`DataProcessor()` → errore), esiste solo per dire alle figlie "TU devi avere questi metodi, io dico il COME si chiamano ma non il cosa fanno" (`@abstractmethod` = metodo dichiarato senza corpo, `...` al posto del codice). Le figlie SONO OBBLIGATE a implementarli, o non si possono creare nemmeno loro. È il "progetto dei progetti" — come il contratto che firmi prima di lavorare: dice i TUOI doveri, non come li svolgi.

**Esecuzione:** main → crea `NumericProcessor()` (funziona: ha implementato validate e ingest) → `numeric.validate(42)` → dentro: `isinstance(42, (int, float))` → True ("42 è un int o un float?") → `numeric.validate("Hello")` → False → `numeric.ingest("foo")` SENZA validazione → dentro ingest: `if not self.validate(data): raise TypeError("Improper numeric data")` → esplode (voluto: il subject vuole l'errore) → `ingest([1,2,3,4,5])` → valida → `_store` trasforma in stringhe e le accoda coi RANK → `output()` estrae il più vecchio (pop(0)) e lo restituisce come tupla `(rank, pezzo)`.

**Come testare:** `cd python/p05/ex0 && python3 data_processor.py`

**Teoria:**
- **Chi è cosa:** `ABC` → classe predefinita del modulo `abc` (ereditando da lei la classe diventa astratta); `@abstractmethod` → decoratore predefinito del modulo abc (marca il metodo come obbligatorio); `isinstance(x, Tipo)` → funzione built-in ("x è di quel tipo?" — il controllo dei tipi a runtime); `all()` → funzione built-in (True se TUTTI gli elementi sono veri); `Any` → tipo predefinito del modulo typing ("dato di qualunque tipo" — per questo validate accetta qualsiasi cosa); `...` → "qui non c'è codice" (pass)
- **Polimorfismo (primo assaggio):** `output()` e il meccanismo rank/store stanno nella classe MADRE, le figlie ereditano il lavoro fatto. Le figlie cambiano SOLO validate/ingest: stesso contratto, comportamenti diversi
- **Il mypy warning voluto:** chiamare `numeric.ingest("foo")` è di proposito un errore di tipo (il subject lo dice: "This will leave you with a mypy warning, on purpose")
- **`_store` col rank:** ogni pezzo ingerito riceve un NUMERO PROGRESSIVO (il rank) e viene accodato in `(rank, pezzo)`; `output()` toglie il più vecchio (FIFO — coda, come il fuoco di BFS)

**Codice:** in `python/p05/ex0/data_processor.py` (già scritto e testato)

## ex1 — data_stream — il router polimorfico

**Cosa fa in concreto:** crea un "centralino" a cui registri i processori di ex0: gli dai una lista di dati MISTI (testi, numeri, log) e lui smista ogni elemento al processore giusto; se nessuno lo vuole, stampa l'errore. Mostra anche le statistiche di ogni processore.

**★ PRIME VOLTE qui:** routing per tipo (nessuna sintassi nuova — il polimorfismo applicato)

**Cosa chiede:** una classe `DataStream` che raccoglie i processor REGISTRATI e, per ogni elemento di uno stream misto, lo manda al processor GIUSTO usando solo `validate()` — senza sapere niente dei tipi concreti.

**Il concetto in una riga:** il DataStream non conosce NumericProcessor/TextProcessor/LogProcessor: conosce SOLO "una lista di cose che hanno validate() e ingest()". Per ogni elemento: prova i processor in ordine, il PRIMO che dice "sì" se lo prende; se nessuno lo vuole → errore. È il centralino: inoltra la chiamata senza sapere chi risponderà.

**Esecuzione:** main → `stream.register_processor(NumericProcessor())` → `process_stream(batch)` → per ogni elemento: for sui processor → `proc.validate(element)` → il primo True vince (`ingest` + `break`) → se nessuno: "DataStream error" → `print_processors_stats()` legge `total` (conteggio pezzi) e `len(_data)` (rimanenti) di ognuno → poi si registrano Text e Log e si rimanda lo stesso batch (ora ogni elemento trova il suo).

**Come testare:** `cd python/p05/ex1 && python3 data_stream.py`

**Teoria:**
- **Perché è polimorfismo:** il router chiama SEMPRE lo stesso metodo (`validate`/`ingest`) su oggetti diversi, e ogni oggetto risponde a modo suo. Aggiungere un 4° processor = registrarlo, ZERO modifiche al router — è il vantaggio che il subject chiede di spiegare
- **Registrare i processor = consegnare il contratto:** il DataStream si fida che qualunque cosa registrata rispetti l'interfaccia di DataProcessor (è per questo che la classe astratta esiste)

**Codice:** in `python/p05/ex1/data_stream.py` (già scritto e testato)

## ex2 — data_pipeline — i plugin con Protocol

**Cosa fa in concreto:** aggiunge al centralino la parte di USCITA: due "plugin" (uno CSV, uno JSON) che ricevono i dati processati e li stampano formattati; il centralino estrae N pezzi da ogni processore e li passa al plugin scelto.

**★ PRIME VOLTE qui:** `Protocol` (duck typing)

**Cosa chiede:** un sistema di export a plugin: `ExportPlugin` è un Protocol che dichiara `process_output(data)`; classi CsvPlugin e JsonPlugin lo implementano; `DataStream.output_pipeline(nb, plugin)` consuma nb pezzi da OGNI processor e li passa al plugin scelto.

**Il concetto in una riga:** il Protocol è il contratto PIÙ leggero: "chiunque abbia un metodo `process_output(lista)` può fare il plugin — non deve ereditare da nessuno, basta che abbia il metodo". Duck typing: "se cammina come un'anatra e starnazza come un'anatra, è un'anatra". Il CSV e il JSON non hanno nessun antenato comune: condividono solo la FORMA.

**Esecuzione:** main → registra 3 processor → batch → `output_pipeline(3, CsvPlugin())` → per ogni processor: estrae fino a 3 pezzi (o quanti disponibili) → `plugin.process_output(data)` → il CsvPlugin incolla i valori con la virgola e stampa → secondo batch → `output_pipeline(5, JsonPlugin())` → chiavi `"item_<rank>"` coi rank progressivi (per questo i numeri ripartono da 3: i primi 3 li ha mangiati il CSV).

**Come testare:** `cd python/p05/ex2 && python3 data_pipeline.py`

**Teoria:**
- **Protocol vs ABC:** la ABC OBBLIGA a ereditare; il Protocol non obbliga a nulla — controlla solo la forma (structural typing). Niente `class CsvPlugin(ExportPlugin)`: basta `def process_output(...)` e mypy lo accetta come plugin
- **Il rank attraversa tutto il sistema:** `output()` dà `(rank, pezzo)` e il JSON lo usa per le chiavi `item_3`, `item_4`... — il motivo per cui i numeri non ripartono da 0

**Codice:** in `python/p05/ex2/data_pipeline.py` (già scritto e testato)



---

# p06 — The Codex (Import e moduli)

**Struttura del progetto (il subject la impone):** un package `alchemy/` con sottopackage `grimoire/` e `transmutation/`, un `elements.py` alla radice, e 14 script `ft_*.py` che testano i 4 misteri. Tutto sta in `python/p06/`.

## ★ PRIMA VOLTA — i 4 misteri degli import (tutta la teoria in un colpo)

**Mistero 1 — import vs from:** `import elements` carica TUTTO il modulo e lo usi col punto: `elements.create_fire()`. `from elements import create_water` carica SOLO quella funzione e la chiami DIRETTA: `create_water()`. Stessa roba, due stili: col punto = "cassetta degli attrezzi", senza = "attrezzo in mano".

**Mistero 2 — i package e `__init__.py`:** una cartella con dentro `__init__.py` diventa un PACKAGE importabile col nome della cartella. `__init__.py` gira quando importi il package e decide COSA ESPORRE: nel nostro caso espone `create_air` ma NON `create_earth` — per questo `alchemy.create_earth()` esplode con AttributeError (il "segreto" del subject, voluto). Analogia: `__init__.py` è la vetrina del negozio: la merce che non metti in vetrina non la vendi.

**Mistero 3 — import assoluti vs relativi:** assoluto = percorso completo dalla radice (`from alchemy.elements import create_air`); relativo = percorso DA QUI, coi puntini (`from ..potions import strength_potion` — `..` = cartella superiore, come nei path). Regola del mestiere: dentro un package si preferiscono i relativi (se sposti la cartella non si rompe), fuori gli assoluti.

**Mistero 4 — le dipendenze circolari:** se A importa B e B importa A → `ImportError: cannot import name ... from partially initialized module` (l'esplosione di `ft_kaboom_1`). Il labirinto: A parte, chiede B, B chiede A, A non è finito → cortocircuito. Soluzioni: importare in fondo al file, importare DENTRO le funzioni, o togliere UN lato dell'import (il light_validator non importa dal light_spellbook: il ciclo si spezza — mentre dark_validator e dark_spellbook si importano a vicenda ed esplodono apposta).

## Gli script (tutti testati, l'output è nel subject)

- **ft_alembic_0..5**: i 6 modi di raggiungere elements.py e alchemy — da `import elements` (0) a `from alchemy import create_air` (5). **ft_alembic_4 è volutamente rotto**: `alchemy.create_earth()` → AttributeError (la vetrina non lo espone) — anche mypy dà errore lì, DI PROPOSITO (il subject lo dice)
- **ft_distillation_0..1**: le pozioni — `alchemy/potions.py` importa i 4 elementi (assoluti) e costruisce le frasi; `__init__.py` le espone con ALIAS: `healing_potion as heal`
- **ft_transmutation_0..2**: recipes.py usa UN import assoluto (`from elements import create_fire`, `from alchemy.elements import create_air`) e UNO relativo (`from ..potions import strength_potion`) — il subject ne chiede almeno uno per tipo
- **ft_kaboom_0**: il grimoire LIGHT funziona (il validator ha la sua lista di ingredienti, niente ciclo) → "Spell recorded: Fantasy (Earth, wind and fire - VALID)"
- **ft_kaboom_1**: il grimoire DARK esplode — dark_spellbook importa dark_validator che importa dark_spellbook → ImportError con traceback (voluto, è la dimostrazione del mistero 4)

**Come testare:** `cd python/p06 && python3 ft_alembic_0.py` ecc. — ogni script si lancia da `python/p06/` (gli import sono relativi a quella cartella).

**Teoria extra:**
- **Chi è cosa:** `import`, `from`, `as` → parole chiave; `elements.py` / `alchemy/` → moduli e package NOSTRI; `__init__.py` → il file speciale di Python (nome DUNDER riservato) che trasforma la cartella in package; il resto è tutto nostro
- **L'`__init__.py` del subject "segue le convenzioni usuali"** per flake8/mypy: si usa `__all__` o i commenti noqa — nel nostro c'è `__all__` (lista dei nomi che la vetrina espone)
- **Come si decide il percorso:** se il file che importa è DENTRO un package → relativi; se è uno script alla radice → assoluti (i relativi non funzionano nemmeno, in uno script eseguito direttamente)

---

# p07 — DataDeck (Design pattern: factory, capability, strategy)

**Struttura:** tre package (`ex0/`, `ex1/`, `ex2/`, ognuno con `__init__.py` che espone SOLO le factory — mai le creature concrete) e tre script alla radice di `python/p07/`: `battle.py`, `capacitor.py`, `tournament.py`. Ogni esercizio costruisce sul precedente.

## ex0 — battle — l'abstract factory

**Cosa fa in concreto:** definisce creature di due famiglie (fuoco e acqua, ognuna con versione base ed evoluta) e le crea attraverso FABBRICHE: il main chiede alla fabbrica "dammi la base della famiglia fuoco" senza mai nominare la classe concreta. Poi le fa descrivere, attaccare e combattere.

**★ PRIME VOLTE qui:** pattern abstract factory (niente sintassi nuova: ABC + ereditarietà di p05, composti in un pattern)

**Cosa chiede:** creature di 2 famiglie (Fuoco: Flameling→Pyrodon; Acqua: Aquabub→Torragon) create da FACTORY astratte: `FlameFactory().create_base()` / `create_evolved()`. Il package espone solo le factory.

**Il concetto in una riga:** la factory è il negozio di creature: tu chiedi "dammi il mostro BASE della famiglia Fuoco" e il negozio sa quale classe costruire. Chi compra NON conosce i nomi delle classi — conosce solo la factory. Perché: se domani cambi le classi, chi le usa non deve cambiare niente (il segreto della "clean, maintainable code" del subject).

**Esecuzione:** battle.py → `test_factory(FlameFactory())` → `create_base()` → dentro la factory: `return Flameling()` → `describe()` (metodo CONCRETO della madre Creature) e `attack()` (metodo astratto, implementato dalla figlia) → stesso per evolved → `test_battle` fa combattere le due base.

**Come testare:** `cd python/p07 && python3 battle.py`

**Teoria:** `Creature` è astratta (attack senza corpo, `...`); `CreatureFactory` è astratta (create_base/create_evolved senza corpo); le classi concrete implementano tutto. L'`__init__.py` espone `FlameFactory, AquaFactory` — se qualcuno prova `from ex0 import Flameling` → errore: la creatura concreta non è in vetrina (stesso trucco di p06).

**Codice:** in `python/p07/ex0/` (creatures.py, factories.py, __init__.py) + `python/p07/battle.py`

## ex1 — capacitor — le capability (ereditarietà MULTIPLA)

**Cosa fa in concreto:** aggiunge due "capacità" riusabili (guarire, trasformarsi) che si ATTACCANO alle creature: le creature-guaritrici sanno attaccare E curare; le creature-trasformiste dopo transform() attaccano più forte e con revert() tornano normali.

**★ PRIME VOLTE qui:** ereditarietà multipla (`class Sproutling(Creature, HealCapability)`)

**Cosa chiede:** capacità SEPARATE dalle creature (HealCapability, TransformCapability — NON ereditano da Creature!) e creature che ereditano da ENTRAMBE: `class Sproutling(Creature, HealCapability)`. Due nuove famiglie con le loro factory.

**Il concetto in una riga:** una classe può avere DUE genitori: la creatura (cosa È) + la capacità (cosa SA FARE). Il TransformCapability ha uno STATO (`self._transformed`): dopo `transform()` l'`attack()` cambia (colpisce potenziato), dopo `revert()` torna normale — lo stato persiste tra le chiamate perché sta nell'oggetto.

**Esecuzione:** capacitor.py → crea la factory → base → `describe()`, `attack()`, `heal()` → factory transform → `transform()` mette `_transformed = True` → `attack()` ora va nel ramo "boosted" (l'if legge lo stato) → `revert()` lo rimette a False.

**Come testare:** `cd python/p07 && python3 capacitor.py`

**Teoria:**
- **Perché le capability NON ereditano da Creature:** il subject lo dice — un giorno potrebbero servire a NON-creature (oggetti, carte speciali). Tenerle separate = poterle attaccare a chiunque. È il "design for the future"
- **Ereditarietà multipla in Python:** `class X(A, B)` — X prende i metodi di entrambi. L'ordine conta per chi "vince" i conflitti; qui non ce ne sono (Creature e le capability non hanno metodi con lo stesso nome)
- **Lo stato `_transformed`** è il primo esempio di "l'oggetto RICORDA": il metodo transform cambia l'oggetto e l'attacco successivo si comporta diversamente — come il cartellino che resta attaccato

**Codice:** in `python/p07/ex1/` + `python/p07/capacitor.py`

## ex2 — tournament — lo strategy pattern

**Cosa fa in concreto:** organizza un torneo dove ogni creatura combatte con una STRATEGIA assegnata (normale = solo attacco; aggressiva = trasforma-attacca-ripristina; difensiva = attacca-cura). Se la strategia non è adatta alla creatura, il torneo si ferma con un errore chiaro.

**★ PRIME VOLTE qui:** pattern strategy (ABC + polimorfismo, niente sintassi nuova)

**Cosa chiede:** 3 strategie di battaglia (Normal, Aggressive per i trasformisti, Defensive per i guaritori) che decidono COME agisce una creatura in torneo. `is_valid(creature)` controlla la compatibilità, `act(creature)` esegue (e lancia StrategyError se invalida). Il torneo fa combattere tutti contro tutti con le proprie strategie.

**Il concetto in una riga:** la strategia è il "piano di battaglia" ATTACCATO alla creatura per il torneo: la creatura non sa combattere in torneo, il piano sì. `act()` di Normal = solo attack; Aggressive = transform → attack → revert; Defensive = attack → heal. Il tournament.py conosce SOLO `act()` — non sa quale piano sia.

**Esecuzione:** tournament.py → `battle([(FlameFactory(), NormalStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])` → crea le creature, tutti contro tutti → per ogni scontro: `strat_a.act(a)` → dentro act: `is_valid`? → no? → `raise StrategyError("Invalid Creature 'Flameling' for this aggressive strategy")` (torneo 1, l'errore voluto) → si → esegue il piano.

**Come testare:** `cd python/p07 && python3 tournament.py`

**Teoria:**
- **`isinstance(creature, TransformCapability)`** = il modo di chiedere "questa creatura HA la capacità?" — l'ereditarietà multipla lo rende possibile (lo Shiftling È un TransformCapability)
- **Strategy vs if a catena:** senza il pattern servirebbe `if tipo == trasformista: ... elif guaritore: ...` DENTRO il torneo. Col pattern, ogni piano sta nella SUA classe e il torneo non cambia mai — aggiungi una strategia nuova senza toccare il torneo (stessa lezione della factory)
- **StrategyError** è un'eccezione NOSTRA (come GardenError in p02 ex3) — `class StrategyError(Exception)`

**Codice:** in `python/p07/ex2/` + `python/p07/tournament.py`



---

# p08 — The Matrix (Ambienti virtuali, dipendenze, configurazione)

## ex0 — construct — riconoscere il venv

**Cosa fa in concreto:** controlla se il programma sta girando dentro un ambiente virtuale e stampa informazioni diverse nei due casi: dentro, percorso del venv e dei pacchetti; fuori, un avviso e le istruzioni per crearlo.

**★ PRIME VOLTE qui:** `sys.prefix`, `sys.base_prefix`, `sys.executable`, `site.getsitepackages()`, `os.path.basename()`

**Cosa chiede:** un programma che scopre se sta girando DENTRO un ambiente virtuale e mostra le informazioni giuste (dentro: percorso del venv e dei pacchetti; fuori: avviso + istruzioni per crearlo).

**Il concetto in una riga:** dentro un venv, il Python usato è quello della cartellina `.venv`. Il trucco per scoprirlo: `sys.prefix` = dov'è il Python ATTUALE; `sys.base_prefix` = dov'è il Python ORIGINALE (quello di sistema). Se sono DIVERSI → sei dentro un venv. Analogia: prefix è il tuo indirizzo attuale, base_prefix è la casa dei tuoi genitori — se non vivi più dai tuoi, sei "in trasferta" (nel venv).

**Esecuzione:** main → `in_venv = sys.prefix != sys.base_prefix` → se True: stampa `os.path.basename(sys.prefix)` (il NOME della cartellina, senza percorso) + `sys.executable` (il Python in uso) + `site.getsitepackages()[0]` (dove finiscono i pacchetti installati) → se False: avviso "sei nel globale" + istruzioni (`python -m venv matrix_env` + activate).

**Come testare:** `cd python/p08/ex0 && python3 construct.py` (fuori) → `python3 -m venv matrix_env && source matrix_env/bin/activate && python3 construct.py` (dentro — poi `deactivate`).

**Teoria:** il venv NON è magia: `python3 -m venv .venv` copia Python in una cartellina, e l'activate cambia la variabile PATH così che `python3` diventi quello della cartellina. Il programma lo scopre confrontando i due prefix. (La guida completa al venv è in fondo agli appunti.)

**Codice:** in `python/p08/ex0/construct.py`

## ex1 — loading — dipendenze e package manager

**Cosa fa in concreto:** controlla se le 4 librerie di analisi dati sono installate; se mancano, stampa le istruzioni per installarle (pip e Poetry); se ci sono, genera 1000 dati casuali con numpy, ne calcola le statistiche e disegna un grafico con matplotlib salvato su file.

**★ PRIME VOLTE qui:** `importlib.metadata.version()`, `requirements.txt`, `pyproject.toml`

**Cosa chiede:** un tool di analisi dati che usa pandas/numpy/matplotlib, con gestione GRACEFUL delle dipendenze mancanti (le controlla una a una e dà le istruzioni), e i file di dipendenze per DUE mondi: `requirements.txt` (pip) e `pyproject.toml` (Poetry).

**Il concetto in una riga:** i pacchetti esterni vanno DICHIARATI in un file, così chiunque ricrea l'ambiente con un comando. Due scuole: pip legge `requirements.txt` (lista semplice: `pandas
numpy
...`), Poetry legge `pyproject.toml` (file più ricco, con metadati del progetto). Il programma usa `importlib.metadata.version("pandas")` per chiedere "è installato? che versione?" senza importarlo davvero.

**Esecuzione:** main → per ognuna delle 4 librerie: `check_dependency()` → installata? "[OK] pandas (2.1.0)..." → mancante? "[MISSING] pandas" → se manca qualcosa: istruzioni pip e poetry e stop → se tutto ok: `numpy.random.randint` genera i 1000 dati (il subject vuole NUMPY come fonte dei dati, non liste) → media/deviazione → matplotlib disegna l'istogramma → `matrix_analysis.png`.

**Come testare:** `cd python/p08/ex1 && python3 loading.py` (senza dipendenze: messaggi) → dentro un venv: `pip install -r requirements.txt && python3 loading.py` (analisi completa).

**Teoria:** il subject tollera errori flake8/mypy sugli import qui ("Exceptionally, flake8 and mypy errors are allowed for this exercise, only for import errors"). `requirements.txt` = una riga per pacchetto; `pyproject.toml` = il formato moderno (sezione `[tool.poetry.dependencies]`). L'import di numpy/matplotlib avviene DOPO il check, dentro main — così senza dipendenze non esplode all'import.

**Codice:** in `python/p08/ex1/` (loading.py + requirements.txt + pyproject.toml)

## ex2 — oracle — configurazione con .env

**Cosa fa in concreto:** legge la configurazione da variabili d'ambiente (caricate dal file .env) e si comporta in modo diverso tra development (stampa tutto) e production (nasconde la chiave segreta e pretende i dati obbligatori); senza configurazione stampa le istruzioni.

**★ PRIME VOLTE qui:** `python-dotenv` (`load_dotenv()`), `os.getenv()`, file `.env`

**Cosa chiede:** un programma che legge la configurazione da VARIABILI D'AMBIENTE (caricate da un file `.env` con la libreria python-dotenv), con comportamento diverso in development vs production, errori chiari se manca la config, e `.env` nel .gitignore (i segreti NON vanno MAI committati).

**Il concetto in una riga:** i segreti (API key, URL database) non si scrivono nel codice. Stanno in un file `.env` (locale, gitignored) e python-dotenv li carica nelle variabili d'ambiente quando il programma parte. Analogia: il codice è la ricetta pubblica, il .env è il cassetto delle spezie segrete che solo il cuoco ha.

**Esecuzione:** main → `load_dotenv()` (legge `.env` se esiste e mette le righe `CHIAVE=valore` nelle variabili d'ambiente) → `os.getenv("MATRIX_MODE")` ecc. per ognuna → se MATRIX_MODE manca: avviso "copy .env.example to .env" e stop → se "development": stampa tutto (la API key può anche mancare) → se "production": nasconde la API key con `'*' * len(api_key)` e PRETENDE DATABASE_URL e ZION_ENDPOINT (avvisi se mancano) → mode sconosciuto: errore.

**Come testare:** `cd python/p08/ex2 && python3 oracle.py` (senza .env: warning) → `cp .env.example .env && python3 oracle.py` (legge) → modifica MATRIX_MODE=production e rilancia.

**Teoria:** il file `.env.example` è la MASCHERA: mostra quali chiavi servono, senza valori segreti — quello SÌ va committato (e infatti sta nel repo). Il `.env` vero è nel .gitignore ("Never commit real secrets to version control! You must be able to explain why" — perché chiunque clona il repo si prenderebbe le chiavi vere). Le variabili d'ambiente vincono sul file: se il sistema le ha già, getenv trova quelle.

**Codice:** in `python/p08/ex2/` (oracle.py + .env.example + .gitignore)

---

# p09 — Cosmic Data (Pydantic: validazione dei dati)

**★ PRIME VOLTE qui:** `pydantic` (libreria esterna): `BaseModel`, `Field`, `Enum`, `@model_validator`

**Prerequisito:** serve pydantic 2.x installato in un venv (il subject lo impone). Comandi: `cd python/p09 && python3 -m venv .venv && source .venv/bin/activate && pip install "pydantic>=2"`. Poi `python3 ex0/space_station.py` ecc.

**Il concetto in una riga (vale per tutti e 3 gli esercizi):** Pydantic è un GUARDIANO dei dati: definisci una CLASSE-modello (`class SpaceStation(BaseModel)`) dove ogni campo ha un tipo e dei VINCOLI (`crew_size: int = Field(ge=1, le=20)` = "intero tra 1 e 20"). Quando crei l'oggetto, Pydantic CONTROLLA tutto: dato sbagliato → `ValidationError` con il messaggio preciso. È come il guardiano dell'ex4 di p01, ma pronto e con regole scrivibili in una riga. Perché serve: i dati arrivano dall'esterno (API, file) e non ci si può fidare — Pydantic li valida alla porta.

## ex0 — space_station — il primo modello

**Cosa fa in concreto:** definisce un modello di "scheda stazione spaziale" con vincoli su ogni campo (es. equipaggio da 1 a 20) e lo testa due volte: con dati validi (crea e stampa la scheda) e con un campo invalido (mostra il messaggio d'errore di Pydantic).

**Cosa chiede:** modello `SpaceStation` con campi vincolati (station_id 3-10 caratteri, crew_size 1-20, power/oxygen 0-100, last_maintenance datetime, is_operational default True, notes opzionale max 200) + main che crea una stazione valida e ne mostra i campi, poi prova una invalida e mostra l'errore ("Input should be less than or equal to 20").

**Esecuzione:** main → `SpaceStation(station_id="ISS001", ..., last_maintenance=datetime(2024,6,1,10,0,0))` → Pydantic valida OGNI campo → tutto ok → oggetto pronto → stampa i campi → `SpaceStation(crew_size=25, ...)` → Pydantic rifiuta → `except ValidationError as e:` → `e.errors()[0]["msg"]` = il messaggio del primo errore.

**Teoria:** `Field(min_length=3, max_length=10)` = vincolo sulla lunghezza delle stringhe; `Field(ge=0.0, le=100.0)` = greater-equal/less-equal (ge/le) per i numeri; `Optional[str] = None` = campo che può mancare; `bool = True` = valore di default. La CONVERSIONE automatica: se passi una stringa "2024-06-01" a un campo datetime, Pydantic la converte da solo (domanda del subject: "what happens when you pass a string timestamp to a datetime field?" → la converte, o errore se il formato è sbagliato).

**Codice:** in `python/p09/ex0/space_station.py`

## ex1 — alien_contact — validazione custom

**Cosa fa in concreto:** definisce un modello di "rapporto di contatto alieno" con regole di business che i campi da soli non bastano a esprimere (es. i contatti telepatici richiedono almeno 3 testimoni) e lo testa con un rapporto valido e uno che viola le regole.

**★ PRIME VOLTE qui:** `Enum` (ContactType), `@model_validator(mode="after")`

**Cosa chiede:** modello AlienContact con regole DI BUSINESS che i Field da soli non sanno esprimere: contact_id deve iniziare con "AC", i contatti PHYSICAL devono essere verificati, TELEPATHIC richiede ≥3 testimoni, segnali forti (>7.0) devono avere un messaggio. Un `@model_validator(mode="after")` le controlla TUTTE insieme dopo la validazione dei campi.

**Esecuzione:** main → contatto valido → Pydantic valida i campi → POI gira il validator custom (mode="after" = DOPO i campi): controlla le 4 regole con if → tutte ok → `return self` (OBBLIGATORIO: il validator deve restituire il modello) → contatto invalido (telepathic con 1 testimone) → il validator fa `raise ValueError("Telepathic contact requires at least 3 witnesses")` → il ValidationError lo cattura.

**Teoria:** `Enum` = tipo con un numero CHIUSO di valori (`radio, visual, physical, telepathic`) — se arriva "laser" → errore di validazione automatico. `@model_validator(mode="after")` = decoratore che marca un metodo che gira dopo i campi e vede il modello INTERO (per le regole che coinvolgono più campi insieme — il vecchio `@validator` è deprecato, il subject lo vieta). Dentro il validator: `self.contact_id`, `self.contact_type` ecc. sono già disponibili.

**Codice:** in `python/p09/ex1/alien_contact.py`

## ex2 — space_crew — modelli ANNIDATI

**Cosa fa in concreto:** definisce due modelli collegati (membro dell'equipaggio e missione che contiene una LISTA di membri) e valida regole che coinvolgono tutto l'equipaggio: serve un comandante, le missioni lunghe vogliono metà equipaggio esperto. Testa una missione valida e una senza comandante.

**Cosa chiede:** due modelli in relazione: `CrewMember` (membro singolo) e `SpaceMission` che CONTIENE una LISTA di CrewMember (`crew: List[CrewMember]`). Il validator della missione controlla regole che coinvolgono TUTTO l'equipaggio: serve almeno un Commander/Capitano, le missioni lunghe (>365 giorni) vogliono il 50% di esperti (≥5 anni), tutti attivi.

**Il concetto in una riga:** un modello può stare DENTRO un altro modello (e in liste): `crew: List[CrewMember]` = "questa missione contiene una lista di oggetti CrewMember, e Pydantic valida OGNI membro della lista con le sue regole PRIMA di validare la missione". Come le bambole matrioska: la missione contiene l'equipaggio, l'equipaggio contiene i membri.

**Esecuzione:** main → `CrewMember(...)` × 2 (validati uno a uno) → `SpaceMission(..., crew=crew, ...)` → Pydantic valida i campi della missione E in cascata i 2 membri → il validator: `[m for m in self.crew if m.rank in (Rank.CAPTAIN, Rank.COMMANDER)]` (list comprehension di p03 ex6!) → se la lista è vuota → raise → missione invalida di prova (solo ufficiali, nessun capitano) → "Must have at least one Commander or Captain".

**Teoria:** il Rank è un Enum come il ContactType. Le regole nel validator usano le comprehension per filtrare l'equipaggio — è il p03 che rientra dalla finestra. `Field(min_length=1, max_length=12)` sulla lista = l'equipaggio deve avere 1-12 membri.

**Codice:** in `python/p09/ex2/space_crew.py`

# Elementi usati: cosa è cosa (per l'evaluation)

Devi saper dire di OGNI nome che usi: **è una cosa di Python (predefinita) o una cosa creata da noi? E di che tipo è?**

## Parole chiave del linguaggio (keyword) — NON si possono usare come nomi

`def`, `class`, `if`, `elif`, `else`, `for`, `in`, `return`, `raise`, `try`, `except`, `finally`, `import`, `as`, `and`, `or`, `not`, `True`, `False`, `None`

## Funzioni/classi predefinite di Python (built-in) — pronte all'uso, non create da noi

| Nome | Cos'è | Cosa fa |
|---|---|---|
| `print()` | funzione built-in | stampa sullo schermo |
| `input()` | funzione built-in | legge input, restituisce stringa |
| `int()` | CLASSE built-in | converte in intero (in realtà crea un oggetto int) |
| `str()` | CLASSE built-in | converte in stringa |
| `float` | CLASSE built-in | il tipo dei decimali |
| `range()` | funzione/classe built-in | genera sequenze di numeri |
| `round()` | funzione built-in | arrotonda |
| `len()` | funzione built-in | lunghezza di liste/stringhe |
| `open()` | funzione built-in | apre file (l'fopen di Python) |
| `"x".isupper()` | metodo built-in delle stringhe | True se tutto maiuscolo |
| `"x".islower()` | metodo built-in delle stringhe | True se tutto minuscolo |
| `"x".capitalize()` | metodo built-in delle stringhe | prima lettera maiuscola, resto minuscolo |
| `"x"[0]` | indicizzazione | il carattere in posizione 0 (la prima) |
| `Exception` | CLASSE built-in | capostipite di tutti gli errori |
| `ValueError` | CLASSE built-in | errore di valore sbagliato |
| `ZeroDivisionError` | CLASSE built-in | errore divisione per zero |
| `FileNotFoundError` | CLASSE built-in | errore file inesistente |
| `TypeError` | CLASSE built-in | errore tipi incompatibili |

## Variabili speciali di Python (dunder)

| Nome | Cos'è |
|---|---|
| `__name__` | etichetta automatica del modulo: `"__main__"` se eseguito direttamente |
| `__init__` | il costruttore: metodo che Python chiama da solo alla creazione dell'oggetto |
| `__main__` | il valore che assume `__name__` quando il file è il principale |

Regola: i doppi underscore sono di Python. Noi NON creiamo mai nomi con `__`.

## Cose create da NOI (i nomi li scegliamo noi)

| Cosa | Esempio | Come la riconosci |
|---|---|---|
| Funzione nostra | `def ft_hello_garden():` | `def` + nome + parentesi |
| Classe nostra | `class Plant:` | `class` + Nome con la Maiuscola |
| Classe figlia | `class Flower(Plant):` | tra parentesi c'è il genitore |
| Eccezione nostra | `class GardenError(Exception):` | eredita da Exception |
| Metodo | `def show(self):` dentro una classe | sta dentro la classe, ha `self` |
| Costruttore | `def __init__(self, ...):` | nome `__init__` (usiamo il nome di Python, ma il contenuto è nostro) |
| Attributo | `self.name = name` | `self.` + nome scelto da noi |
| Oggetto | `rose = Plant("Rose", 25, 30)` | variabile che contiene un'istanza |
| Parametro | `def f(temp_str):` | nome scelto da noi tra le parentesi del def |

## Come distinguere classe da funzione (regola pratica)

- **Classe**: si "chiama" per CREARE qualcosa → `Plant("Rose", 25, 30)` produce un oggetto pianta. `int("25")` produce un oggetto intero. `Exception` è una classe: la usi per ereditare o per catturare
- **Funzione**: si chiama per FARE qualcosa → `print()` stampa, `input()` legge, `round()` arrotonda
- **Trucco**: se il risultato lo salvi in una variabile come oggetto nuovo, dietro c'è quasi sempre una classe. Se lo usi per l'effetto (stampa, lettura), è una funzione

## Il vocabolario dell'OOP (domande tipiche da evaluation)

| Termine | Definizione in una frase |
|---|---|
| Classe | il progetto/stampo (struct + funzioni dentro) |
| Oggetto (istanza) | la cosa concreta creata dal progetto |
| Attributo | un dato salvato dentro l'oggetto (`self.name`) |
| Metodo | una funzione della classe, riceve `self` |
| Costruttore `__init__` | metodo che inizializza l'oggetto alla creazione |
| `self` | l'oggetto stesso dentro i suoi metodi |
| Ereditarietà | una classe figlia riceve tutto dal genitore |
| `super()` | "la classe genitore" — per riusare i suoi metodi |
| Incapsulamento | `_` + getter/setter: proteggere i dati con accesso controllato |
| Polimorfismo | una stessa chiamata si comporta in base al tipo vero dell'oggetto |
| Metodo statico | funzione nella classe, senza self — si chiama sulla classe |
| Metodo di classe | riceve `cls` — serve per creare oggetti |

---

# Tabelle di riferimento rapido

## C → Python

| C | Python |
|---|---|
| `printf("x=%d", x)` | `print(f"x={x}")` |
| `scanf("%d", &x)` | `x = int(input())` |
| `void` | `-> None` |
| `typedef struct` | `class` |
| `t_plant rose; rose.name = ...` | `rose = Plant("Rose", 25, 30)` |
| `p->name` | `self.name` |
| `void grow(t_plant *p)` | `def grow(self):` |
| `grow(&rose)` | `rose.grow()` |
| `for (int i=1; i<=n; i++)` | `for i in range(1, n + 1):` |
| `atoi(str)` | `int(str)` |
| `if (x > 0) { }` | `if x > 0:` + indentazione |
| `else if` | `elif` |
| `errno` / `if (x == -1)` | eccezioni + try/except |

## Type hints

| Hint | Significato |
|---|---|
| `: str` | stringa |
| `: int` | intero |
| `: float` | decimale |
| `-> None` | void |
| `-> int` | restituisce intero |
| `-> bool` | restituisce True/False |

## Eccezioni comuni

| Eccezione | Quando esplode |
|---|---|
| `ValueError` | `int("abc")` |
| `ZeroDivisionError` | `1 / 0` |
| `FileNotFoundError` | `open()` di file inesistente |
| `TypeError` | `"a" + 1` |
| `IndexError` | indice fuori dalla lista |
| `KeyError` | chiave inesistente nel dizionario |

## La matrioska del punto

```
self . stats . grows
 │      │       │
 │      │       └─ un numero dentro il contatore
 │      └─ il contatore dentro la pianta
 └─ la pianta
```

Il punto = "vai dentro". Si legge SEMPRE da sinistra a destra, un passo alla volta.

---

# Registro delle prime volte

Dove è comparso per la prima volta ogni elemento nuovo di Python (per ripassare in ordine):

| Elemento | Prima volta in |
|---|---|
| `print()`, `def` | p00 ex0 |
| `input()` | p00 ex1 |
| `int()`, f-string, `str` | p00 ex2 |
| `if`/`else` | p00 ex4 |
| `for`, `range()`, ricorsione helper | p00 ex6 |
| type hints, `elif`, `.capitalize()` | p00 ex7 |
| `if __name__ == "__main__":` | p01 ex0 |
| classe, oggetto, `__init__`, `self`, metodo, attributo | p01 ex1 |
| `round()` | p01 ex2 |
| lista di oggetti, `end=" "` | p01 ex3 |
| incapsulamento `_`, getter/setter, `return` | p01 ex4 |
| ereditarietà, `super()` | p01 ex5 |
| `@staticmethod`, `@classmethod`, classe annidata | p01 ex6 |
| `import`, `try`/`except`, `as e`, `Exception` | p02 ex0 |
| `raise` | p02 ex1 |
| tipi di errore specifici, `else` del try | p02 ex2 |
| eccezione custom `class X(Exception)`, valore di default di un parametro | p02 ex3 |
| `finally`, indicizzazione `stringa[0]`, `.isupper()` | p02 ex4 |
| `sys`, `sys.argv`, `len()`, lista | p03 ex0 |
| `.append()`, `sum()`/`max()`/`min()`, slicing `[1:]`, `return` senza valore | p03 ex1 |
| tupla, `math.sqrt()`, `.split()`, `float()`, unpacking, `while True`, `**`, `continue`/`break` | p03 ex2 |
| set, `random.randint()`, `random.sample()`, **dizionario**, `union`/`intersection`/`difference`, **annotazione di variabile** (`x: Tipo = valore`) | p03 ex3 |
| `dict.keys()` / `dict.values()` | p03 ex4 |
| generatore (`yield`), `next()`, `random.choice()` | p03 ex5 |
| comprehension (list/dict), `.items()` | p03 ex6 |
| `open()`, oggetto file, `.read()`, `.close()`, `typing.IO` | p04 ex0 |
| `.write()`, modalità "w", `.splitlines()`, `"\n".join()` | p04 ex1 |
| `sys.stdin`/`stdout`/`stderr`, `.readline()`, `.flush()` | p04 ex2 |
| `with` (context manager) | p04 ex3 |
| `ABC`, `@abstractmethod`, `isinstance()`, `all()`, `Any` | p05 ex0 |
| router polimorfico (nessuna sintassi nuova) | p05 ex1 |
| `Protocol` (duck typing) | p05 ex2 |
| `import`/`from`, package, `__init__.py`, import relativi, dipendenze circolari | p06 |
| abstract factory, ereditarietà multipla, strategy pattern, `StrategyError` | p07 |
| `sys.prefix`/`base_prefix`, `site`, `os.path.basename` | p08 ex0 |
| `importlib.metadata`, `requirements.txt`, `pyproject.toml` | p08 ex1 |
| `python-dotenv`, `os.getenv()`, file `.env` | p08 ex2 |
| `pydantic`: `BaseModel`, `Field`, `Enum`, `@model_validator` | p09 |

---

# Guida venv — cos'è e quando serve davvero


## In una riga

Un **venv** (virtual environment) è una **copia privata di Python** dentro una cartellina (di solito `.venv`). Quando è attivo, `python3` e `pip` usano QUELLA copia, non quella del sistema. Analogia: un laboratorio personale chiuso a chiave — puoi sporcarlo quanto vuoi senza toccare il laboratorio comune.

## Quando serve DAVVERO nei nostri moduli

| Moduli | Serve il venv? | Perché |
|---|---|---|
| p00, p01, p02, p03, p04, p05, p06, p07 | **NO** | usano solo la libreria standard di Python (sys, math, random, abc...) — `python3` di sistema basta |
| p08 (The Matrix) | **SÌ** | ex1 ha bisogno di pandas/numpy/matplotlib, ex2 di python-dotenv — pacchetti da installare, e il subject chiede di testare dentro/fuori venv |
| p09 (Cosmic Data) | **SÌ (obbligatorio)** | il subject lo impone: "You must use Virtual environments" + pydantic installato via pip |
| AMAZEING | **SÌ** | ha il suo `.venv` già creato (perché il Python di sistema del Mac rifiuta `pip install`) |

Regola pratica: **serve il venv solo quando un modulo ha bisogno di pacchetti esterni** (cose da `pip install`). Se il modulo usa solo import standard, no.

## I 4 comandi della vita

```bash
# 1. CREARE (una volta sola, dentro la cartella del progetto)
python3 -m venv .venv

# 2. ATTIVARE (ogni volta che apri un terminale nuovo per quel progetto)
source .venv/bin/activate
# → il prompt ora mostra (.venv): sei dentro

# 3. INSTALLARE (solo dentro il venv attivo; pip ora funziona)
pip install pydantic

# 4. USCIRE
deactivate
# → il (.venv) sparisce, si torna al Python di sistema
```

## Cose da sapere per non farsi fregare

- **L'attivazione vale per UNA finestra di terminale.** Apri un'altra finestra? Non è attivo lì. Per questo vedi `(.venv)` in una finestra e non in un'altra
- **Il venv si riconosce dal prompt:** `(.venv)` prima del nome utente
- **Ogni progetto ha il SUO venv** — quello di AMAZEING non c'entra con p09. Si crea uno per cartella di progetto
- **La cartella `.venv` NON va mai pushata su GitHub** (è nel .gitignore, contiene copie giganti di Python — chi corregge se lo ricrea da solo)
- **Il problema pip del Mac** (errore "externally-managed-environment" / PEP 668) sparisce DENTRO il venv: lì pip è libero di installare
- **Creare il venv NON lo attiva** — sono due passi separati: `python3 -m venv .venv` crea, `source .venv/bin/activate` accende. Errore classico: creare e poi chiedersi perché pip non va
- **Se sbagli, si butta via:** `rm -rf .venv` e si ricrea. Non si rompe niente di sistema

## Il comando per i moduli che ne hanno bisogno (p08, p09)

```bash
cd python/p09              # cartella del modulo
python3 -m venv .venv      # crea
source .venv/bin/activate  # attiva
pip install pydantic       # installa
python3 ex0/space_station.py   # esegui con python3 (ora è quello del venv)
deactivate                 # a fine lavoro
```
