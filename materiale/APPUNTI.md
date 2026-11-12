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
- **★ GUARDIA EOF (fix audit 25/9):** se l'input FINISCE (es. `echo "1,2,3" | python3 ft_coordinate_system.py` — dopo la prima risposta lo stdin è chiuso), `input()` lancia `EOFError` ("End Of File": nessuno sta più scrivendo) → senza gestione = TRACEBACK. Fix: nel main le due chiamate sono dentro `try ... except EOFError:` → stampa "Input ended unexpectedly." e `return` (uscita pulita, niente traceback). L'evaluator può pipare l'input: senza questa guardia si viene bocciati. EOFError è un'eccezione predefinita come ValueError/OSError. Attenzione: get_player_pos() NON cattura EOFError — lo lascia PROPAGARE al main, che decide come finire; dentro il loop invece il ValueError viene catturato lì (ritenta). Due errori, due posti diversi: il ValueError è "risposta sbagliata → richiedi", l'EOFError è "nessuno risponderà più → esci"

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
- **Come leggere il nome consume_event (imposto dal subject, non rinominabile):** "consume" in inglese = consumare/divorare — il nome dice esattamente cosa fa: DIVORA la lista. Traduzione mentale da tenere quando lo leggi: `remove_event_from_list`. Non va rinominato nel codice (il subject lo impone, l'evaluator lo cerca con quel nome), ma negli appunti lo leggiamo con la traduzione che fa capire tutto

**Cosa fa e cosa ritorna consume_event (perplessità risolta):** il nome dice tutto: CONSUMA la lista. A ogni richiesta pesca UN elemento a caso (choice), lo TOGLIE dalla lista (remove), lo consegna (yield) — finché la lista non è vuota. NON ritorna niente: nessun return, quando il while finisce dà StopIteration (il for lo usa per fermarsi). Demo col dado fisso, lista [('alice','run'),('bob','eat'),('charlie','sleep')]: giro 1 pesca ('bob','eat'), la lista resta [('alice','run'),('charlie','sleep')]; giro 2 pesca ('alice','run'), resta [('charlie','sleep')]; giro 3 pesca l'ultimo, lista = []; quarta richiesta: len>0? NO -> StopIteration -> il for si ferma
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
- **List vs dict comprehension (perplessità risolta):** la LOGICA è identica — è il for+append condensato in una riga. Cambiano due cose: (a) le graffe {} al posto delle quadre [] — il contenitore decide il risultato: `[cosa for x in lista]` produce una LISTA di cose singole, `{chiave: valore for x in lista}` produce un DICT di coppie; (b) ogni elemento prodotto è una COPPIA chiave:valore — e i due punti NON sono sintassi della comprehension, sono i due punti del dizionario (quelli di {"alice": 5}). Demo: `[x*2 for x in [1,2,3]]` → [2,4,6]; `{name: len(name) for name in ["alice","bob"]}` → {'alice': 5, 'bob': 3} — entrambi identici al for classico di 4 righe. Traccia del dict: giro 1 name="alice" → coppia "alice":5 → nel dict; giro 2 name="bob" → coppia "bob":3 → nel dict

- **Forma della comprehension:** `[espressione for elemento in collezione]` — e con filtro: `[espressione for elemento in collezione if condizione]`. Stessa sintassi con `{}` per i dizionari: `{chiave: valore for ...}` e anche per i set: `{x for ...}`
- **Struttura e ordine di lettura (perplessità risolta):** si legge DA SINISTRA A DESTRA: (1) SINISTRA = l'espressione, COSA produrre (usa la variabile ma NON la dichiara — la variabile NASCE nel for, come nel for classico); (2) CENTRO = `for variabile in collezione`, da dove pescare (solo FOR, mai while); (3) DESTRA = `if filtro` opzionale. La comprehension è il for di 4 righe RIBALTATO IN ORIZZONTALE: il corpo (append) va PRIMA, poi il for, poi l'if
- **Equivalente col for classico** (il for di 4 righe diventa 1): `risultato = []` → `for x in lista:` → `risultato.append(f(x))` = `[f(x) for x in lista]`
- Il subject: "Each comprehension should be on a single line"
- **Chi è cosa:** tutto già visto, tranne `.items()` → metodo built-in dei dizionari (dà le coppie chiave-valore, da spacchettare con `for chiave, valore in ...`)

**Codice:** in `python/p03/ex6/ft_data_alchemist.py` (già scritto e testato)

---

# p04 — Data Archivist (File I/O)

**Il pericolo principale degli archivi digitali (dall'introduzione del subject):** la PERDITA DEI DATI — il subject: "data is fragile. Without proper preservation, it vanishes into the digital void forever". Tradotto in tecnica, i modi in cui i dati muoiono: file non chiusi (i dati restano nel buffer e non arrivano mai su disco, soprattutto col crash) · errori non gestiti (traceback che interrompe tutto) · apertura in "w" sopra un file esistente (lo svuota). Tutto il modulo è difesa contro questo: chiudere sempre, gestire gli errori senza crashare, il `with`, i 3 canali.

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
- **Come si legge `f: IO = open(filename, "r")`:** "f — prometto che sarà un oggetto file (IO è l'etichetta) — uguale al risultato di open(filename, 'r')". Tre pezzi: `f` = variabile nostra · `: IO` = etichetta/promessa (a runtime non fa NULLA, serve a mypy e all'evaluator) · `= open(...)` = la chiamata vera, che apre il file e ritorna l'oggetto file. In C è esattamente `FILE *f = fopen(filename, "r");` — il `FILE *` è la promessa, fopen la chiamata
- **Come si legge `from typing import IO`:** "dal modulo typing, importa l'etichetta IO". `typing` = modulo PREDEFINITO della libreria standard che contiene SOLO etichette per le promesse (nessuna funzione utile al programma); `IO` = l'etichetta "oggetto file". Il subject lo autorizza esplicitamente ("Authorized: import typing, typing.IO") — senza l'import, il nome `IO` non esiste e la promessa `f: IO` darebbe NameError
- **Cosa è `OSError`:** la FAMIGLIA di eccezioni predefinita che raccoglie TUTTI gli errori del sistema operativo. `FileNotFoundError` (errno 2, file inesistente) e `PermissionError` (errno 13, permesso negato) sono suoi sottotipi. Il subject mostra ENTRAMBI i casi (foo e /etc/master.passwd): un solo `except OSError` li prende tutti e due. In C: la variabile `errno` e `perror()`
- **Come si legge `except OSError as e`:** "se dentro il try scatta un qualsiasi errore del sistema operativo, prendilo e mettilo nella variabile e"
- **Le modalità di open (SECONDO parametro, NON sono i permessi unix rwx):** `"r"` = read: legge, il file DEVE esistere (errno 2 altrimenti) · `"w"` = write: crea se non esiste, SVUOTA se esiste · `"x"` = creazione esclusiva (errore FileExistsError se esiste già) · `"a"` = append, scrive in coda senza svuotare. Per p04 servono solo `"r"` (ex0) e `"w"` (ex1)
- **★ Cosa succede se NON chiudi un file (domanda da evaluation, 25/9):** (1) file descriptor occupato — risorsa limitata del SO per processo: demo con `ulimit -n 64` → esploso a 61 file aperti con `[Errno 24] Too many open files` (una memory leak ma di file; in C fopen senza fclose, identico) · (2) le scritture restano nel BUFFER, su disco solo a flush/close — crash = dati persi, altri programmi vedono il file vuoto · (3) a fine programma NORMALE Python chiude e svuota tutto da solo → in uno script corto non si nota nulla, ma è affidarsi alla misericordia dell'interprete; su Windows un file aperto non è rinominabile/cancellabile. Per questo il `with`: chiude in ogni caso. Risposta tascabile: "finché gira occupa un file descriptor (limite → errno 24) e le scritture stanno nel buffer (crash = perse); a fine normale Python chiude da solo ma è cattiva pratica".

- **Perché chiudere sempre (`.close()` = `fclose` del C):** (1) finché il programma vive, il file aperto occupa un file descriptor — il SO ne concede un numero limitato per processo (in C: "Too many open files") · (2) le scritture NON vanno subito su disco: restano nel BUFFER di Python e arrivano al file solo con flush/close (demo fatta: durante il run `cat` vede il file VUOTO, dopo la fine del programma appare "ciao") · a fine programma NORMALE Python chiude e svuota tutto da solo (per questo in uno script corto non si nota nulla), MA se il programma crasha i dati nel buffer vanno persi · dal ex3 in poi il subject introduce `with`, che chiude da solo anche in caso di errore (il subject VIETA di usarlo prima di ex3)

**All'evaluation:**
- Files to Submit del subject: SOLO `ft_ancient_text.py`. Nessun file txt da consegnare: l'evaluator si porta i suoi file di test (o ricrea il frammento dell'esempio). Il nostro `ancient_fragment.txt` serve SOLO per testare in locale e non è pushato (su GitHub ci sono solo i 4 .py di p04)
- I 4 casi di test del subject, da saper riprodurre: (1) senza argomento → usage · (2) `python3 ft_ancient_text.py foo` → errno 2 gestito, NO crash · (3) `python3 ft_ancient_text.py /etc/master.passwd` → errno 13 Permission denied, gestito, NO crash · (4) file vero → contenuto con `--` e chiusura
- La domanda del subject: "What is the type of the data returned by open()?" → un oggetto IO (oggetto file), NON una stringa

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

**Come testare il ramo "Error opening file" + "Data not saved" (25/9):** far FALLIRE `open(name, "w")` con un nome impossibile: (1) cartella del percorso inesistente → `echo "/nonexistent/prova.txt" | ...` → errno 2 · (2) nome = cartella → `echo "/tmp" | ...` → errno 21 IsADirectory · (3) permesso negato → `echo "/etc/prova.txt" | ...` → errno 13. PERCHÉ fallisce il caso 1 se "w" crea il file? Perché "w" crea il FILE, non le CARTELLE: se la cartella del percorso non esiste, open fallisce — crea solo l'ultimo pezzo. Ordine dei print: "Saving data to..." esce PRIMA del try (sempre), poi except stampa errore + "Data not saved." + return.

**Teoria:** l'oggetto file ha DUE metodi speculari: `.read()` (legge tutto) e `.write(testo)` (scrive il testo). La modalità si sceglie nel secondo parametro di open: "r" legge, "w" scrive (crea/sovrascrive). In C: `fopen(name, "r")` / `fopen(name, "w")` + `fwrite`.

- **Salvare sullo STESSO file letto (domanda del 25/9):** funziona — la lettura è finita e il file è CHIUSO prima della scrittura; i dati stanno in memoria (content/lines/new_lines). `open(name, "w")` svuota il file e ci scrive la versione trasformata. Il file non è mai aperto due volte insieme. Risposta evaluation: "si può salvare sul file letto?" → sì, lettura chiusa prima della scrittura, dati già in memoria, "w" svuota e riscrive.
- **`out.write("\n".join(new_lines) + "\n")` come si legge (domanda del 25/9):** "sull'oggetto out, scrivi la stringa ottenuta incollando le righe di new_lines con un a-capo IN MEZZO, più un a-capo finale". `join` = metodo della stringa COLLA che sta prima del punto: prende la lista e restituisce UNA stringa con la colla SOLO TRA gli elementi, mai all'inizio o alla fine (`"X".join(["a","b","c"])` → `"aXbXc"`). Serve perché splitlines aveva tolto gli a-capo e perché write() accetta UNA stringa sola, non una lista. Il `+ "\n"` chiude il file con la riga finale completa (join non mette colla in coda) — demo: repr = `'a\nb\nc\n'`. C: ciclo con strcat o `fprintf(out, "%s\n", riga)`. E scrive nel BUFFER: i dati arrivano su disco col `.close()` successivo.

- **Perché la variabile si chiama `out` (domanda del 25/9):** `out` NON è il nome del file — è il nome della VARIABILE (il telecomando/oggetto file per scrivere). Il nome del file su disco è la stringa dentro `name` (dall'input). Come si legge `out: IO = open(name, "w")`: "out — prometto che sarà un oggetto file — uguale a: apri in SCRITTURA il file il cui nome è la stringa dentro name". Il nome della variabile lo scegliamo noi e non tocca il file: potevamo chiamarla `pippo`, il file salvato sarebbe identico. `out` = i dati ESCONO verso il disco (output), mentre in lettura si usa `f`. Sono due oggetti DIVERSI con ruoli diversi: `f` apre l'ingresso (letto e chiuso subito), `out` apre l'uscita (ci scriviamo) — quando `out` nasce, `f` è già chiuso. In C identico: `FILE *out = fopen(name, "w");` — `out` è il puntatore, `name` la stringa col nome.

- **La comprehension `[line + "#" for line in lines]` (richiamo di p03 ex6, sfumatura importante):** quello che entra nella lista NON è la variabile `line` da sola, ma il RISULTATO dell'espressione a sinistra del for (`line + "#"`, la riga col cancelleto in coda) — se fosse solo `line`, i cancelletti sparirebbero. Srotolata: `for line in lines: new_lines.append(line + "#")`. Ordine di lettura sx→dx: cosa entra → da dove. La variabile del for è il biglietto da visita che cambia a ogni giro; in lista finisce il suo contenuto TRASFORMATO.

**★ Perché `end=""` + `if not content.endswith("\n")` (★ PRIMA VOLTA: il parametro `end` di print — domanda nata qui, 25/9):** la riga di chiusura `--File ... closed.` deve SEMPRE stare su una riga sua, con ESATTAMENTE un a-capo tra contenuto e chiusura — né zero né due. Ma non si sa in anticipo se il file finisce con l'a-capo o no. La coppia: `end=""` TOGLIE l'a-capo automatico di print (quello del contenuto, se c'è, resta) · `if not content.endswith("\n")` = domanda "il contenuto NON finisce con a-capo?" → `print()` vuoto RIMETTE quello che manca. Uno toglie sempre, l'altro rimette solo se serve → sempre esattamente uno. `end=""` NON innesca l'if: sono due pezzi indipendenti (l'if guarda il FILE, non il print). E NON si può omettere `end=""`: senza, col file che finisce con a-capo esce UNA RIGA VUOTA in più (a-capo del contenuto + a-capo di print = 2) e l'output non è più quello del subject. Dimostrato dal vero con 4 varianti (file con/senza a-capo finale × codice con/senza la coppia). Lo stesso pezzo identico sta anche in ex0 e ex2.

**★ LEZIONE DEL FILE VUOTO (bug vero trovato al PC della scuola, 25/9):** se il file è VUOTO (0 byte), `splitlines()` dà la lista VUOTA `[]` → `new_lines[0]` esplode con `IndexError: list index out of range` (il primo elemento di una lista vuota non esiste). Perché su un PC sì e sull'altro no? Perché i due "file vuoti" NON erano uguali: un file con DENTRO un solo a-capo (`\n`, 1 byte) ha UNA riga (vuota) → `splitlines()` dà `[""]` → funziona e stampa `--#`; un file di 0 byte veri (creato con `touch`) ha ZERO righe → `[]` → traceback. LA DIFFERENZA ERA IL FILE, NON IL PC. Fix: `if len(new_lines) > 0:` prima di `new_lines[0]` — si legge "se nella lista c'è almeno una riga" (if = domanda). Con la guardia: file vuoto → solo "Transform data:" e poi la domanda, niente crash; file normale → output identico a prima. Stesso fix in ex2. Risposta pronta evaluation: "cosa succede se ti danno un file vuoto?" → splitlines dà lista vuota, senza la guardia new_lines[0] esploderebbe — il subject chiede di gestire i casi di errore.

**★ COS'È UNA RIGA per splitlines (domanda del cancelleto, 25/9):** una riga = il testo che sta PRIMA di un a-capo. `splitlines()` non conta i caratteri, conta gli A-CAPO (i separatori): 0 byte → 0 righe → `[]` → NESSUN # (il # appartiene alle RIGHE, non al file: zero righe = zero cancelletti); un `\n` da solo → 1 riga VUOTA → `[""]` → `#`; uno spazio ` ` → 1 riga → `[" "]` → ` #` (spazio + #); `abc` → `abc#`. Il # si infila tra il contenuto della riga e il suo a-capo: `splitlines()` TOGLIE l'a-capo dalla riga, `line + "#"` lo attacca in coda, `join` rimette gli a-capo DOPO i #. In C sarebbe: `" \n\0"` → togli `\n`, appendi #, rimetti `\n` → `" #\n\0"` — il # sta dove in C stava il `\n`, NON il `\0` (in Python il `\0` non esiste: la stringa sa quanto è lunga). File vuoto salvato: `"\n".join([]) + "\n"` = solo un a-capo (1 byte): si salva il contenuto trasformato, che di "zero righe" è solo l'a-capo finale. **Stessa famiglia di guardia (fix audit 25/9): `input()` è dentro `try ... except EOFError:`** — se lo stdin finisce prima della risposta (es. `< /dev/null`), EOFError → `name = ""` → il ramo "Not saving data." esce pulito senza traceback. ex2 è già sicuro: `sys.stdin.readline()` a EOF restituisce "" invece di esplodere.

**Codice:** in `python/p04/ex1/ft_archive_creation.py` (già scritto e testato)

## ex2 — ft_stream_management — i 3 canali

**Cosa fa in concreto:** come ex1, ma gli errori vanno scritti sul canale di errore (stderr, col prefisso [STDERR]) e la domanda all'utente viene fatta senza usare input(), leggendo direttamente da stdin.

**★ PRIME VOLTE qui:** `sys.stdin`, `sys.stdout`, `sys.stderr`, `.readline()`, `.flush()`

**Cosa chiede:** come ex1, ma: gli errori vanno sul canale di ERRORE (`sys.stderr`, col prefisso `[STDERR]`) e l'input va letto SENZA `input()`, usando `sys.stdin`.

**Il concetto in una riga:** ogni programma ha 3 canali predefiniti (i "three sacred channels" del subject): `sys.stdin` (dove arriva quello che scrivi), `sys.stdout` (dove va il print normale), `sys.stderr` (dove vanno gli ERRORI — separato, così i messaggi d'errore non si mischiano all'output "vero"). In C: stdin/stdout/stderr, li conosci.

**Esecuzione:** come ex1, con 2 differenze: `sys.stderr.write(f"[STDERR] ...
")` al posto del print per gli errori (si scrive sul canale di errore — sul terminale SI VEDE uguale, ma il canale è diverso: chi usa il programma può separarli, es. `2>errori.txt`) → per l'input: `sys.stdout.write("domanda ")` + `sys.stdout.flush()` (spinge subito il testo sullo schermo) + `name = sys.stdin.readline().strip()` (legge UNA riga da stdin; `.strip()` toglie l'andata a capo finale).

**Come testare:** `cd python/p04/ex2 && python3 ft_stream_management.py foo` (errore su stderr) · con un file valido e input piped

**Teoria:** `input()` è solo una comodità costruita SOPRA stdin/stdout: il subject ti fa fare a mano quello che input() fa da solo. `flush()` serve perché l'output è bufferizzato (parte a blocchi): senza flush la domanda potrebbe non apparire prima della risposta. **DIMOSTRAZIONE VISTA DAL VERO (25/9):** quando stdout e stderr finiscono nello stesso canale (es. `2>&1 | tail -2`), la riga `[STDERR] ...` è comparsa PRIMA delle righe del programma, anche se nel codice il print dell'intestazione viene prima: stdout è BUFFERIZZATO (aspetta di riempire un blocco prima di spedire), stderr è SENZA buffer (parte SUBITO). Per questo la domanda usa `sys.stdout.write(...)` + `flush()`: senza flush, la domanda resterebbe nel buffer mentre l'utente fissa lo schermo vuoto. Con la pipe il comando di test può mostrare l'ordine "sbagliato": è il buffer, non un bug — all'evaluation va saputo spiegare.

**★ STRIP vs SPLIT — i gemelli con lavori opposti (confusione del 25/9):** `strip()` = spella i BORDI: toglie spazi/a-capo SOLO dall'inizio e dalla fine → resta UNA STRINGA (`'  ciao mondo  \n'` → `'ciao mondo'`, lo spazio in mezzo è intatto). `split()` = taglia in PEZZI → diventa UNA LISTA (`['ciao', 'mondo']`) — già visto in p03 ex2 per le coordinate. In ex2 c'è strip, quindi `name` resta UNA STRINGA (il nome del file) e DEVE esserlo: `name == ""` ha senso solo con una stringa e `open(name, "w")` vuole una stringa, non una lista. Se scrivi "mio file.txt", strip lascia lo spazio interno: il nome resta con lo spazio.

**★ Come arriva l'input SENZA input() (domanda del 25/9):** l'input non arriva DA input() — arriva dal CANALE. Alla nascita del programma il SO collega tre tubi: tastiera → stdin, schermo → stdout e stderr; quello che scrivi finisce nel tubo stdin da solo. input() è solo un ASSISTENTE che pesca dal canale, toglie l'a-capo e mostra il prompt — non ha mai toccato la tastiera direttamente. `sys.stdin.readline()` sei tu che infili la mano nel tubo: pesca una riga CON l'a-capo (demo: `'ciao mondo\n'`), poi `.strip()` la ripulisce. Stesso tubo, due modi di pescare. In C si fa già così da sempre: `fgets`/`scanf` leggono direttamente da stdin — "senza input()" è il modo nudo del C.

**★ WRITE vs FLUSH — i due ruoli distinti (domanda del 25/9):** `write("testo")` = il testo va nella CASSA (il buffer), NON sullo schermo: Python accumula perché ogni invio al terminale è lento (camion che parte a carico pieno). `flush()` = svuota la cassetta e spinge tutto sullo schermo ADESSO, anche a camion mezzo vuoto. Demo vera: senza flush, una riga scritta su stdout PRIMA di una su stderr esce DOPO (resta in cassetta fino alla fine del programma, dove Python svuota da solo); con flush esce subito nell'ordine giusto. In ex2 i due lavorano in coppia: write mette la domanda in cassetta → flush la fa comparire → SOLO DOPO readline si ferma ad aspettare la risposta; senza flush il programma aspetterebbe la risposta con la domanda ancora in cassetta (schermo vuoto). Prova dal vivo: `python3 -c "import sys,time; sys.stdout.write('domanda '); time.sleep(3); print('fine')"` — "domanda" appare solo alla fine, col flush appare subito. In C: `fflush(stdout)`, stesso nome stesso scopo.

**Codice:** in `python/p04/ex2/ft_stream_management.py` (già scritto e testato)

## ex3 — ft_vault_security — il with (context manager)

**Cosa fa in concreto:** fornisce una funzione "cassaforte" che legge o scrive QUALSIASI file e restituisce sempre una coppia (riuscito?, contenuto-o-errore) — col with il file si chiude da solo anche se qualcosa va storto.

**★ PRIME VOLTE qui:** `with` (context manager)

**Cosa chiede:** funzione `secure_archive(filename, action, content)` che usa il `with` per leggere/scrivere qualunque file e restituisce una tupla `(True/False, contenuto o messaggio d'errore)` — il file si chiude SEMPRE da solo, anche con errori.

**Il concetto in una riga:** `with open(...) as f:` = "apri il file, lavoraci dentro il blocco, e CHIUDILO AUTOMATICAMENTE quando esci — anche se scoppia un errore". È il finally di p02, già costruito per te: niente `f.close()` a mano, impossibile dimenticarlo.

**Esecuzione:** main → 4 dimostrazioni → ogni `secure_archive(...)` fa: `with open(filename, "r") as f:` → `return (True, f.read())` — il with chiude DA SOLO il file prima che il return consegni il valore → se open fallisce: `except OSError as e:` → `return (False, str(e))` (la TUPLA col fallimento — niente crash, come p02 vuole).

**Come testare:** `cd python/p04/ex3 && python3 ft_vault_security.py` — l'unica cosa da preparare è il file NORMALE (copiarlo da materiale). Il file inesistente non va creato (il punto è che non esiste) e quello inaccessibile è già di sistema (`/etc/master.passwd`, verificabile con `cat` → Permission denied). Per un file inaccessibile PROPRIO (trucco da evaluation): `touch vietato.txt && chmod 000 vietato.txt` → anche il tuo file dà errno 13; poi `chmod 644` per ripristinare. Il programma non chiede NIENTE: 4 demo in fila, poi `cat new_fragment.txt` per vedere il file scritto, e pulire.

**★ CONTEXT MANAGER e RAII (chiesti dall'evaluation sheet, 25/9):** context manager = un OGGETTO che sa prepararsi prima del blocco e ripulirsi dopo, SEMPRE: il `with` è la sintassi, il context manager è l'oggetto con i metodi `__enter__` (chiamato entrando → apre, ti dà l'`as f`) e `__exit__` (chiamato uscendo, in ogni caso → chiude). Il file È un context manager. RAII = "Resource Acquisition Is Initialization", l'idioma del C++: la risorsa si prende quando l'oggetto nasce (costruttore) e si libera quando muore (distruttore), mai a mano — il ciclo di vita dell'oggetto È quello della risorsa. Python non può usare il RAII puro perché il garbage collector distrugge gli oggetti quando GLI PARE (niente tempi certi) → stessa garanzia col `with` + context manager: liberazione a momento CERTO (fine blocco). In C: il `goto cleanup` dei progetti 42 è il RAII scritto a mano. Perché il with rende più sicuro: il close lo scrive Python (impossibile dimenticarlo), gira in TUTTI i finali (normale, eccezione catturata, non catturata), file descriptor sempre liberato e buffer sempre svuotato.

**★ Il with NON sostituisce il try (correzione 25/9):** sono due strumenti per due problemi diversi: il try/except cattura l'APERTURA fallita (file inesistente/permessi → open lancia OSError → senza except = traceback, demo fatta), il with gestisce la CHIUSURA automatica. Nel codice di ex3 il try AVVOLGE il with proprio per questo: quando open fallisce, l'eccezione parte prima di entrare nel with e solo l'except la prende. Versione essenziale: "con il with non serve il .close() (chiude da solo, anche con errori); ma il try/except resta per l'apertura fallita".

**★ Il with NON ritorna un booleano (correzione 25/9):** `with` non ritorna NULLA — è una struttura di controllo come if/for, non una funzione. Il True/False della coppia lo scriviamo NOI nei due return. Due strade, due return: (1) open RIESCE → si entra nel blocco → `return (True, f.read())`; (2) open FALLISCE → il blocco NON si percorre proprio, l'eccezione salta all'except → `return (False, str(e))`. Se open fallisce il return del try NON si esegue: non c'è nessun "if sul booleano di with", c'è il try/except che sceglie la strada. Chiamata con 1 solo argomento → va al PRIMO parametro (filename), gli altri restano ai default. E "ok, msg" è lo spacchettamento della TUPLA ritornata da secure_archive (non di "while"): ok = True/False, msg = contenuto o testo d'errore.

**Teoria:** il `with` funziona con qualunque "risorsa" che va chiusa (file, connessioni). Traduzione C: il `fclose()` che metteresti in ogni ramo d'errore, scritto UNA volta da Python. Il subject (p04): "use of the with statement will be introduced in exercise 3. You must not use it before" — per questo ex0-ex2 chiudono a mano. **Ripassino finally (25/9):** il blocco che gira SEMPRE — try riuscito, fallito o esploso; anche con eccezione NON catturata gira PRIMA del crash (l'ultimo desiderio). Demo: con `1/0` catturato il finally chiude il file e il programma continua; con `1/0` non catturato il finally pulisce e POI il programma muore. `with` È un try/finally confezionato: `with open(name) as f: content = f.read()` equivale a `f = open(name)` + `try: content = f.read()` + `finally: f.close()` — stessa garanzia "chiudi a qualunque costo", scritta da Python, impossibile dimenticarla.

**Codice:** in `python/p04/ex3/ft_vault_security.py` (già scritto e testato)



---

# p05 — Code Nexus (Classi astratte e polimorfismo)

## ex0 — data_processor — le classi astratte (ABC)

**Cosa fa in concreto:** costruisce una mini-libreria di 3 "processori" — Numeric (numeri), Text (testi), Log (dizionari) — ognuno con 3 verbi: `validate` (questo dato è roba mia?), `ingest` (sì? lo metto in magazzino), `output` (tiro fuori il pezzo più vecchio col suo numero d'ordine). Il main li crea e li testa con dati giusti e sbagliati, incluso un errore FATTO ESPLODERE apposta perché lo chiede il subject.

**★ PRIME VOLTE qui:** `ABC`, `@abstractmethod`, `isinstance()`, `all()`, `Any`

**Cosa chiede:** la classe astratta `DataProcessor` (ABC) coi 2 metodi astratti `validate`/`ingest` e il metodo normale `output`; 3 classi figlie che li implementano ognuna per i suoi tipi; il main testa validi/invalidi e l'ingest senza validazione (che deve esplodere).

**★ IL CONCETTO — quello che Python fa DAVVERO (una sola regola nuova):**

1. Classe = scatola di metodi (p01). Oggetto = lo costruisci dalla scatola.
2. **L'UNICA regola nuova di tutto l'esercizio:** se nella scatola c'è anche UN SOLO metodo rimasto VUOTO (corpo `...`) marcato con `@abstractmethod`, Python RIFIUTA di costruire oggetti da quella scatola. `DataProcessor()` → `TypeError: Can't instantiate abstract class DataProcessor without an implementation for abstract methods 'ingest', 'validate'`. Niente "ideali", niente magie: solo questo controllo.
3. La madre lascia vuoti apposta `validate` e `ingest`. Perché? Perché lei NON SA come si valida "un dato qualunque" (numero? stringa? dizionario? non è affar suo). Scrive i NOMI dei metodi, lascia il corpo vuoto, e ci appiccica il bollino.
4. Il bollino `@abstractmethod` vuol dire UNA cosa: "chi eredita da me DEVE scrivere il corpo di questo metodo, altrimenti non si costruisce nemmeno lui". La figlia scrive un metodo con lo STESSO NOME → il SUO prende il posto di quello vuoto della madre → bollino rispettato. Questa mossa si chiama **OVERRIDE** (sovrascrivere): si fa già in p01 quando una figlia riscrive un metodo della madre — solo che in p01 è FACOLTATIVA, qui sui buchi è OBBLIGATORIA. Il template si può riassumere così: "erediti il codice già scritto + i buchi, e nei buchi DEVI scrivere (override), altrimenti errore alla creazione".
5. Ogni figlia scrive `validate` e `ingest` A MODO SUO (3 ricette diverse: numeri / stringhe / dizionari). Ora nella scatola della figlia non c'è più niente di vuoto → si costruisce.
6. Tutto il resto (`output`, `_store`, `_rank`, `name`) è codice GIÀ SCRITTO nella madre: le figlie lo ereditano ESATTAMENTE come in p01. La madre è metà lavoro già fatto, metà buchi da riempire.

La "regola" che si sente è solo il controllo del punto 2. **Il bollino è il foglietto "NON DIMENTICARE: ogni processore deve saper validare e ingerire" — ma Python non si fida dei foglietti: se dimentichi, ERRORE alla creazione.**

**Perché si chiama "astratta":** astratto = il contrario di concreto. La madre ESISTE davvero (classe vera in memoria, con codice vero: `__init__`, `_store`, `output`) — ma alcuni suoi metodi esistono SOLO COME IDEA (nome + firma, corpo `...`): per questo la classe nel complesso è INCOMPLETA, non può creare oggetti, ed è detta astratta. "Un processore di dati" è l'idea astratta; "il processore di numeri" è la cosa concreta: non assumi un'idea, assumi un lavoratore concreto. Col CMS: il template non è un sito, è l'idea di sito. Nel codice: ABC = Abstract Base Class (il modulo si chiama proprio `abc`). In C il gemello è il prototipo di funzione (`int validate(void *);`): dichiara l'idea; la definizione col corpo è la cosa concreta — un header di soli prototipi non lo esegui, e la madre astratta non la costruisci.

**L'analogia — il regolamento di famiglia (dice il VERBO, non la ricetta):** "Chi lavora in famiglia DEVE saper CUCINARE (validate) e SERVIRE (ingest). Il regolamento dice i VERBI, non le ricette: uno fa la pasta, uno la pizza, uno il sushi." La madre non lavora mai (non si costruisce), ma lascia il magazzino di famiglia già pronto (`output`) a tutti i figli. Il figlio che non sa cucinare non viene assunto (errore alla creazione).

**L'analogia dell'utente (CMS):** la madre è il template di un sito: design e struttura FISSI (il codice già scritto), campi MODIFICABILI vuoti (i buchi). Le figlie sono i siti consegnati ai clienti: ognuna riempie i campi a modo suo, ma il design non si tocca. Precisione per l'evaluation: tecnicamente una figlia POTREBBE fare override anche di `output` (l'override funziona su qualsiasi metodo), ma il senso del template è "riempi i buchi, il resto usalo com'è".

**Perché esiste questo meccanismo (domanda da evaluation):**
1. **La madre non saprebbe cosa scrivere nei buchi:** come si valida "un dato qualunque"? Se `validate` fosse un metodo classico avrebbe un corpo finto che le figlie riscriverebbero comunque — il buco dice esplicitamente "questo NON lo so fare io, lo devi fare tu".
2. **La garanzia per chi usa gli oggetti:** con le classi classiche chiamare `oggetto.validate()` è una promessa a parole (se il metodo manca → AttributeError a runtime); con l'ABC è una garanzia controllata dall'interprete (se la classe è figlia di DataProcessor, i metodi CI SONO — altrimenti l'oggetto non sarebbe mai nato). ex1 userà proprio questa garanzia: il DataStream chiama validate su processori di cui non conosce il tipo.
3. **L'errore nel momento giusto:** processore che dimentica `ingest` — senza ABC l'errore esplode alla CHIAMATA (magari all'evaluation); con ABC esplode alla CREAZIONE, sulla riga che va corretta. In C è la differenza tra errore di compilazione (subito, al build) e segfault a runtime (in demo): Python non ha il compilatore che controlla, l'ABC è la rete di sicurezza.
**In una riga:** l'ABC trasforma una promessa ("tutti devono avere validate e ingest") in una garanzia controllata dall'interprete, con l'errore alla creazione dell'oggetto invece che alla chiamata.
**Figlia vuota, il contrasto in una riga:** con la madre CLASSICA una figlia vuota (`class Figlia(Madre): pass`) eredita tutto e funziona — perché la madre ha fatto TUTTO il lavoro. Con la madre ASTRATTA una figlia vuota viene RIFIUTATA alla creazione — perché la madre ha lasciato apposta dei buchi ("non so validare un dato qualunque"), e se la figlia non li riempie Python se ne accorge SUBITO invece di scoprirlo alla prima chiamata. Non cambia cosa può fare il programma: cambia QUANDO scopri l'errore — subito, sulla riga che lo ha causato, invece che a runtime davanti all'evaluator.

**Differenza con l'ereditarietà classica (p01 ex5):**

| | p01 (classica) | p05 (astratta) |
|---|---|---|
| La madre | completa → puoi crearla | coi buchi → non puoi crearla |
| Override | facoltativo — senza, gira la versione della madre | obbligatorio sui buchi — senza, nemmeno la figlia si crea |
| La meccanica | identica: si eredita codice vero | identica |
| In una riga | "erediti tutto, cambi ciò che vuoi" | "erediti il già fatto, i buchi DEVI riempirli" |

**★ L'albero genealogico (chi ha cosa — richiesto il 3/11):**

```
ABC (modulo abc — la legge del controllo buchi)
 └── DataProcessor (ASTRATTA: non costruibile)
      ├── NumericProcessor → oggetto numeric (numeri)
      ├── TextProcessor    → oggetto text    (testi)
      └── LogProcessor     → oggetto log     (log)
```

- **Attributi** `name`, `_data`, `_rank`, `_total`: creati dall'`__init__` della MADRE → ogni oggetto ha la SUA copia (3 magazzini separati, uno per lavoratore)
- **Metodi completi** `_store`, `output`: scritti nella madre UNA volta → ereditati da tutte le figlie senza riscriverli
- **Buchi** `validate`, `ingest`: dichiarati dalla madre (vuoti), RIEMPITI da ogni figlia a modo suo (override) → ogni chiamata usa la versione DELLA FIGLIA, quella vuota della madre non gira mai
- **`__init__` delle figlie:** contiene solo `super().__init__("Nome")` — super() = "la parte di madre che è dentro di me". ATTENZIONE alla distinzione (da evaluation): l'ereditarietà dei METODI è automatica (basta `class Figlia(Madre):` — `_store` e `output` arrivano gratis); gli ATTRIBUTI invece si CREANO solo quando gira un `__init__`, e siccome la figlia ha il SUO `__init__` (override, come per qualunque metodo) quello della madre non girerebbe MAI da solo → la figlia lo chiama esplicitamente: `super().__init__("Nome")` = "esegui il costruttore della MADRE" → nascono name, _data, _rank, _total. Senza super: oggetto nato senza attributi → AttributeError (provato con demo). La stringa tra parentesi è il VALORE che finisce in self.name — la targhetta col nome del lavoratore (usata in ex1 per le statistiche), non un "proprietario"
- **Ricerca meccanica dei metodi:** `numeric.validate(...)` → 1° in NumericProcessor → trovato (buco riempito) → gira la figlia · `numeric._store(...)` → non c'è nella figlia → si SALE alla madre → trovato → gira la madre · `numeric.output()` → idem (madre). Python sale la catena solo quando la classe più in basso non ha il metodo
- **I 3 attributi della scheda — cosa contengono e quando cambiano (PROVA col ciclo di vita):** tutti e 3 nascono nell'`__init__` della madre (`_data=[]`, `_rank=0`, `_total=0`) — ogni lavoratore ha le SUE copie. `_data` = il MAGAZZINO: la lista di coppie (rank, pezzo) che c'è FISICAMENTE dentro ADESSO — cresce con ingest, si accorcia con output, len(_data) = il "remaining" delle stats di ex1. `_rank` = il TIMBRO numeratore: il numero d'ordine del PROSSIMO pezzo (parte da 0, ogni pezzo prende il valore attuale poi rank += 1) — non scende MAI, output non lo tocca, in ex2 diventa le chiavi item_N. `_total` = la STORIA: contatore dei pezzi processati (+1 per pezzo in _store) — non scende MAI, è il "total X items processed" delle stats. CICLO DI VITA (demo): creato → []/0/0 · ingest([1,2,3,4,5]) → 5 pezzi/5/5 · output ×3 → _data scende a 2, _rank e _total RESTANO 5. Regola: ingest fa crescere tutti e 3; output fa scendere SOLO _data — rank e total contano la STORIA, data conta l'ADESSO. ex1: dopo i 2 batch numeric = 8/8/8 → consuma 3 → _data 5, rank e total restano 8 → stats "total 8, remaining 5" = _total e len(_data). NOTA ONESTA da evaluation: _rank e _total hanno SEMPRE lo stesso valore (entrambi +1 per pezzo da 0) — stesso numero, due lavori diversi: rank = il numero da stampare sul pezzo (il biglietto), total = il contatore per le statistiche. In C: _data = buffer della coda; _rank = contatore globale di ID progressivi (static); _total = contatore statistico. **CHI CAMBIA COSA:** `_store` è l'UNICO che cambia _rank e _total; _data la cambiano in DUE (_store cresce, output scende); validate non tocca nulla; __init__ li crea. Frase da evaluation: "_store è l'unica porta d'ingresso dei dati (cresce _data, _rank, _total); output è l'unica porta d'uscita (accorcia solo _data); i contatori della storia si muovono solo all'ingresso"

**Esecuzione (traccia completa):**
- **Prima del main:** import (abc dà `ABC` e `@abstractmethod`, typing dà `Any`) → Python registra le 4 classi in memoria (i `def` NON eseguono i corpi) → riga 145: `__name__ == "__main__"` vero → parte `main()`
- **101-104:** banner → `numeric = NumericProcessor()` → `__init__` della figlia → `super().__init__("Numeric Processor")` — `super()` si legge "la parte di MADRE che è dentro di me" → l'`__init__` della madre crea la scheda: name="Numeric Processor", `_data=[]` (magazzino vuoto), `_rank=0`, `_total=0`
- **105 `numeric.validate(42)`:** `isinstance(42, (int, float))` → True → return True → "…'42': True". **★ isinstance(x, Tipo)** = built-in: "x è un int o un float?" — controllo del tipo A RUNTIME (in C: confronto di tag), risponde True/False
- **106 `numeric.validate("Hello")`:** le domande si fanno TUTTE in fila: "Hello" è int/float? NO (salto il corpo) → è lista? NO (salto il corpo) → return False. A risposta falsa si salta solo il CORPO, mai la funzione
- **107-112 LA BOMBA VOLUTA:** `try: numeric.ingest("foo")` → dentro ingest: `validate("foo")` → False → `not False` = True → `raise TypeError("Improper numeric data")` — l'eccezione PARTE (le righe dopo non girano, la funzione muore lì) → il try la intercetta: `except TypeError as e` → e = l'eccezione, `{e}` = il messaggio → "Got exception: Improper numeric data". Il subject VUOLE questa esplosione ("on purpose"): è un test richiesto, non un bug
- **114-115 `ingest([1,2,3,4,5])`:** validate → è lista → `all(isinstance(item, (int, float)) for item in data)` — pezzo per pezzo: 1 ok, 2 ok, 3 ok, 4 ok, 5 ok → **★ all()** = built-in "sono TUTTI True?" (in C: catena di &&) → True → `self._store([str(item) for item in data])` — la comprehension fa ["1","2","3","4","5"]: i numeri diventano STRINGHE (il magazzino parla solo str) → **_store (madre)**: giro 0: append((0,"1")) → _data=[(0,"1")], _rank=1, _total=1 · giro 1: (1,"2"), _rank=2 · … · giro 4: (4,"5"), _rank=5, _total=5. Magazzino: [(0,"1"),(1,"2"),(2,"3"),(3,"4"),(4,"5")] — ogni pezzo entra come coppia (rank, pezzo), il rank è il NUMERO D'ORDINE d'ingresso; `_total` conta i pezzi passati TOTALI e non scende MAI (in ex1 farà le statistiche)
- **116-119 estrazione:** `for i in range(3)` (i=0,1,2) → `output()` = `return self._data.pop(0)` — **pop(0) si legge** "tira fuori il PRIMO della lista e toglilo" (FIFO, la coda — come il fuoco del BFS di AMAZEING) → giro 0: (0,"1") → rank=0, value="1" → "Numeric value 0: 1" (il rank esce dall'unpacking ma NON si stampa) · giro 1: (1,"2") · giro 2: (2,"3"). In magazzino restano (3,"4") e (4,"5"); _rank=5 e _total=5 NON scendono (contano la storia, non il magazzino attuale)
- **121-128 Text:** `text = TextProcessor()` → super().__init__("Text Processor") → magazzino FRESCO tutto suo → `validate(42)`: né str né lista → False → `ingest(["Hello","Nexus","World"])`: validi → `self._store(list(data))` — **list(data) = la COPIA della lista** (così se il chiamante modifica la sua, il magazzino non cambia) → magazzino [(0,"Hello"),(1,"Nexus"),(2,"World")] → `output()` → (0,"Hello") → "Text value 0: Hello" (Nexus e World restano nel magazzino: il subject li lascia lì)
- **130-142 Log:** `log.validate("Hello")` → False → logs = lista di 2 dict → `ingest(logs)`: validate → è lista → `all(self.validate(item) for item in data)` — ogni elemento deve passare lo stesso controllo: le 2 chiavi log_level/log_message DEVONO esserci (correzione del 29/10: prima un dict senza chiave → KeyError a runtime; ora validate dice False → TypeError pulito) e ogni chiave/valore deve essere str (`.items()` = le coppie chiave,valore, p03 ex4) → valido → comprehension `f"{entry['log_level']}: {entry['log_message']}"` → ["NOTICE: Connection to server", "ERROR: Unauthorized access!!"] — il dict diventa una STRINGA "livello: messaggio" (il "converts the data into strings" del subject) → _store → [(0,"NOTICE…"),(1,"ERROR…")] → 2 output → le 2 stampe finali
- **Chiusura:** main finisce, si torna alla riga 146, il programma esce. Nessun input utente, nessun file: è un collaudo a copione fisso

**Come testare:** `cd python/p05/ex0 && python3 data_processor.py` (l'output è identico all'esempio del subject, verificato)

**Quali rami testa il main (e quali abbiamo verificato noi):** il main per tutti e 3 i processori testa SOLO il ramo LISTA di ingest (`ingest([1,2,3,4,5])`, `ingest(['Hello','Nexus','World'])`, `ingest(logs)` con logs = lista di 2 dict — le QUADRE attorno ai dict fanno la lista). I rami del pezzo SINGOLO (else) NON compaiono nell'output del subject e sono stati verificati con demo separate (regola vitale: ogni ramo eseguito almeno una volta): `ingest(42)` → [(0,'42')] · `ingest('Hello')` → [(0,'Hello')] · `ingest({'log_level':'NOTICE','log_message':'Connection to server'})` → [(0,'NOTICE: Connection to server')] — tutti funzionano. NOTA sui riferimenti: `_data` è passato per RIFERIMENTO (come un puntatore in C) — `output()` fa `pop` sulla STESSA lista che chiunque altro osserva: per questo dopo l'estrazione la lista è più corta ovunque

**Il viaggio di un numero SOLO (ingest(42) passo per passo):** guardia (riga 44): validate(42) → True → non scatta → `isinstance(42, list)` → False → else → `self._store([str(42)])`: str(42) = "42" → lista da UN pezzo ["42"] (perché _store lavora sempre con una lista di pezzi: numero solo = lista da 1, lista di numeri = lista da molti — stesso nastro trasportatore) → un giro di for: append((0,"42")) → magazzino [(0,"42")], _rank=1, _total=1. ingest = l'ENTRATA del magazzino (trasforma in str, incarta in lista, archivia col rank); output = l'USCITA. In questo programma è un collaudo dell'architettura; in ex1/ex2 il router userà ingest per davvero.
**Perché TUTTO tra parentesi quadre (i 2 rami di ingest):** le quadre costruiscono una NUOVA lista da dare a `_store`, che per contratto vuole UNA LISTA di stringhe (`pieces: list[str]`) e ci fa il for. Ramo if (è lista): `[str(item) for item in data]` = comprehension — giro 1: item=1 → "1" entra nella lista nuova · … · giro 5: "5" → risultato ["1","2","3","4","5"]. Ramo else (numero solo): `[str(42)]` = quadre con UNO slot → ["42"]. LE QUADRE SONO OBBLIGATORIE: PROVA — `n._store('42')` senza quadre → [(0,'4'),(1,'2')]: il for sbrìciola la stringa in caratteri! Le quadre trasformano "42" da DUE pezzi ('4','2') a UN pezzo solo ("42"). Regola: _store riceve SEMPRE una lista; le quadre la costruiscono (pezzo per pezzo col for nel ramo lista, direttamente col pezzo unico nel ramo singolo)

**Teoria:**
- **Chi è cosa:** `ABC` → classe predefinita del modulo `abc` (ereditandola, Python attiva il controllo dei buchi); `@abstractmethod` → decoratore predefinito del modulo abc (il BOLLINO); `isinstance(x, Tipo)` → funzione built-in ("x è di quel tipo?" — il controllo dei tipi a runtime, in C sarebbe un confronto di tag); `all()` → funzione built-in (True se TUTTI gli elementi sono veri); `Any` → tipo predefinito del modulo typing ("dato di qualunque tipo" — per questo validate accetta qualsiasi cosa); `...` → corpo vuoto, "qui non c'è codice" (equivale a pass)
- **`self` tra parentesi (perché c'è):** self = l'OGGETTO STESSO. Quando chiami `n.validate(42)`, Python di nascosto passa DUE cose: l'oggetto a sinistra del punto (→ self) e 42 (→ data). Nella DEFINIZIONE dichiari entrambi i parametri, nella CHIAMATA ne scrivi uno solo: il primo lo riempie Python con l'oggetto a sinistra del punto. A cosa serve: a raggiungere le cose DI QUEL lavoratore — `self._store(...)` = "il magazzino di QUESTO oggetto" (senza self, Python non saprebbe quale dei 3 magazzini riempire); `validate` invece non tocca self, gli basta data. PROVA: `n.validate(42)` e `NumericProcessor.validate(n, 42)` sono la STESSA chiamata (la seconda è la forma esplicita). In C: self è il puntatore `this` che passeresti a mano come primo parametro — Python lo passa da solo col punto
- **`item` dove nasce (e le altre variabili del ciclo):** `item` NON si dichiara prima: nasce DENTRO il `for` della comprehension (`[str(item) for item in data]`) — il for dichiara SEMPRE la sua variabile del ciclo, anche dentro una riga. È il ciclo normale compresso: `nuova = []` + `for item in data: nuova.append(str(item))` — giro 1: item=1, giro 2: item=2... Alla fine la variabile sparisce (PROVA: usare item fuori → NameError). Stesso discorso in `all(isinstance(item, (int, float)) for item in data)` (generatore senza quadre, p03 ex5), in `for entry in entries` (entry = il dict della passata) e in `for k, v in data.items()` (k = chiave, v = valore). In C: la variabile del `for (int i = 0; ...)` — la dichiara il ciclo
- **Polimorfismo (primo assaggio):** `output()` e `_store` stanno nella MADRE, le figlie li ereditano e li usano senza riscriverli. Le figlie cambiano SOLO validate/ingest: stessi verbi, ricette diverse
- **Il mypy warning voluto:** `numeric.ingest("foo")` è di proposito un errore di tipo — il subject lo dice: "This will leave you with a mypy warning, on purpose". È la BOMBA VOLUTA: deve esplodere a runtime
- **ingest: il vero lavoro è il MAGAZZINO, non l'alert:** l'alert (`raise`) è solo la GUARDIA all'ingresso (il caso invalido); il lavoro vero è trasformare in stringhe e chiamare `_store` — PROVA: `n._data` prima è [], dopo `n.ingest([1,2,3,4,5])` è [(0,'1'),(1,'2'),(2,'3'),(3,'4'),(4,'5')] (numeri → STRINGHE coi rank, _rank=5, _total=5). Perché ingest ricontrolla invece di fidarsi: il subject impone che se chiami ingest SENZA validate e il dato è invalido, deve esplodere — ingest è autosufficiente (guardia + lavoro). Perché trasforma in stringhe: il magazzino parla solo str, così ex1/ex2 possono mescolare numeri, testi e log nello stesso flusso
- **`_store` col rank:** ogni pezzo ingerito riceve un NUMERO PROGRESSIVO (rank) e viene accodato come coppia `(rank, pezzo)`; `output()` toglie il più vecchio (FIFO — la coda, come il fuoco del BFS di AMAZEING)
- **`pop` spiegato (il cuore di output):** `lista.pop(indice)` fa DUE cose in una: LEGGE l'elemento a quell'indice E lo RIMUOVE dalla lista, restituendolo come valore. `lista[0]` legge SOLO (lista invariata); `lista.pop(0)` legge e toglie (lista accorciata) — PROVA. Senza indice pop() toglie l'ULTIMO (LIFO, la pila); con 0 toglie il PRIMO (FIFO, la coda — esce la roba entrata prima). In C sarebbe il dequeue: prendi array[0] e fai scorrere tutto a sinistra — pop(0) lo fa da solo. `_data` = il magazzino (attributo nostro, lista di coppie (rank, pezzo))
- **output NON è gestione della memoria:** Python ha il garbage collector — niente leak da evitare (niente free() come in C). output è l'USCITA del magazzino: il pezzo esce perché va al CONSUMATORE (in ex1 il main lo consuma e le stats "remaining" scendono; in ex2 alimenterà i plugin CSV/JSON). Il subject: "extract the oldest piece... The piece of data is then removed" — estrarre E rimuovere: il pezzo è del chiamante adesso, insieme al suo rank (in ex2 il rank diventa la chiave item_3, item_4...). Analogia: il bancomat eroga una banconota — esce perché ce l'hai TU, non per svuotare la macchina. In C: il dequeue preleva per PROCESSARE, la free è la conseguenza non lo scopo
- **Perché l'if/else in ingest (lista sì/no):** `_store` lavora SEMPRE con una lista di pezzi (fa il for) — il dato però arriva in DUE forme: lista → i pezzi sono già separati → `[str(item) for item in data]`; numero solo → un pezzo solo → `[str(data)]` (lista da uno). Due strade, stessa destinazione: PROVA — ingest(42) → [(0,'42')] e ingest([1,2,3]) → [(0,'1'),(1,'2'),(2,'3')]. NON è un doppio controllo inutile: (1) validate risponde solo SÌ/NO, un bool senza memoria — non dice a ingest "era una lista"; (2) ingest deve funzionare anche SENZA validate chiamato prima (il subject lo impone) — è autosufficiente. E non sono la stessa domanda: validate chiede "è ACCETTABILE?", ingest chiede "è una LISTA?" per scegliere la confezione. Analogia: il portiere dice solo "può entrare" e non accompagna nessuno; l'operaio guarda lui il pacco per decidere come spacchettarlo (vassoio o pezzo unico)

**Codice:** in `python/p05/ex0/data_processor.py` (già scritto e testato)

## ex1 — data_stream — il router polimorfico

**Cosa fa in concreto:** costruisce un CENTRALINO (`DataStream`) a cui registri i lavoratori di ex0; gli dai una lista di dati MISTI (stringhe, numeri, log) e lui smista OGNI elemento al lavoratore giusto chiedendo in giro `validate`; se nessuno lo vuole, stampa l'errore. Poi stampa le STATISTICHE di ogni lavoratore (totale pezzi processati / rimasti nel magazzino). Il main: registra solo Numeric → manda un batch di 5 elementi → 3 errori + 4 pezzi numerici → registra anche Text e Log → rimanda lo stesso batch → ognuno prende i suoi → consuma 3/2/1 pezzi → statistiche aggiornate.

**★ PRIME VOLTE qui:** nessuna sintassi nuova — il polimorfismo in AZIONE (la garanzia di ex0 viene USATA)

**★ L'albero genealogico:**

```
ABC
 └── DataProcessor (astratta)            ← copia IDENTICA a ex0
      ├── NumericProcessor ┐
      ├── TextProcessor    ├─ i 3 lavoratori di ex0
      └── LogProcessor     ┘

DataStream (classe NUOVA — NON è figlia di nessuno: è il CLIENTE del contratto)
 └── _processors = lista (la RUBRICA dei lavoratori registrati)
```

- **DataStream** = il centralino: non eredita da DataProcessor, la USA. Ha: `_processors` (lista vuota all'inizio), `register_processor(proc)` = append nella rubrica, `process_stream(stream)` = il cuore, `print_processors_stats()` = le statistiche
- Il contratto di ex0 è la garanzia che rende sicuro il centralino: qualunque cosa registrata HA validate e ingest (altrimenti non sarebbe mai nata)

**La meccanica del router (process_stream), giro giro:**

```
for element in stream:            # un elemento alla volta
    handled = False               # "per ora nessuno se l'è preso"
    for proc in self._processors: # chiedo ai lavoratori IN ORDINE di registrazione
        if proc.validate(element):  # "è roba tua?"
            proc.ingest(element)    # "sì? prenditela"
            handled = True
            break                   # il PRIMO che dice sì vince
    if not handled:                 # ho chiesto a tutti: nessuno l'ha voluto
        print("DataStream error - Can't process element in stream: ...")
```

**Esecuzione (traccia completa coi valori veri):**
- `stream = DataStream()` → rubrica vuota → stats: "No processor found, no data" (len == 0)
- `register_processor(NumericProcessor())` → rubrica = [numeric]
- **Primo batch** (solo Numeric): "Hello world" → validate False → ERROR · [3.14,-1,2.71] → True → ingest → 3 pezzi · [2 dict] → False → ERROR · 42 → True → 1 pezzo · ["Hi","five"] → False → ERROR. Stats: "Numeric Processor: total 4 items processed, remaining 4 on processor" (total = _total = la storia; remaining = len(_data) = il magazzino)
- `register_processor(TextProcessor())` + `register_processor(LogProcessor())` → rubrica = [numeric, text, log] — L'ORDINE CONTA: il primo che dice sì vince
- **Stesso batch di nuovo:** "Hello world" → numeric no, TEXT sì (1 pezzo) · [3.14,-1,2.71] → numeric sì (è il primo) → +3 · [2 dict] → numeric no, text no, LOG sì → +2 · 42 → numeric +1 · ["Hi","five"] → text +2. Stats: Numeric 8/8, Text 3/3, Log 2/2
- **Consumo 3/2/1:** `for proc in stream._processors:` (il main accede all'attributo privato: si può, è lo stesso file) con `nb = 3 se Numeric, 2 se Text, 1 se Log` — TERNARIO annidato: if/else che PRODUCE un valore (si legge: "se il nome è Numeric → 3; altrimenti se è Text → 2; altrimenti → 1"; in C è il `?:`). `for _ in range(nb):` — `_` = variabile usa-e-getta ("il contatore non mi serve, ripeto e basta") → `proc.output()` × nb: il valore restituito viene BUTTATO VIA — interessa solo l'effetto collaterale (il pezzo esce e le stats cambiano: è il consumo dimostrato dal subject, non la pulizia della memoria). Traccia: numeric 3× pop → magazzino 8→5 · text 2× → 3→1 · log 1× → 2→1 → stats: total NON scende (storia), remaining scende (len(_data)). Nessun IndexError: ogni processore ha pezzi a sufficienza (8≥3, 3≥2, 2≥1). **ATTENZIONE: 3/2/1 non c'entra col 5 del batch** — il batch ha 5 ELEMENTI ma genera 8 PEZZI (un elemento-lista si scompone in più pezzi: [3.14,-1,2.71] → 3, [2 dict] → 2, ["Hi","five"] → 2, più i 2 singoli). Il 3/2/1 è il copione del subject: numeri arbitrari di PEZZI da estrarre, scelti per (1) non svuotare i magazzini (nessun IndexError) e (2) lasciare qualcosa dentro (remaining 5/1/1) così le stats finali mostrano la differenza total vs remaining. **E 3/2/1 non sono né indici né rank:** sono il numero di RIPETIZIONI di output() (nb). Il rank è il BIGLIETTO assegnato da _store (0,1,2,3...) che viaggia nella tupla; pop(0) usa SEMPRE l'indice 0 (il primo della lista, qualunque biglietto abbia). Coincidenza che confonde: 3 poppate fanno uscire i biglietti 0,1,2 — il 3 è il CONTO delle poppate, gli 0/1/2 sono i BIGLIETTI dei pezzi usciti
- **Nota:** il main accede a `stream._processors` (attributo col trattino basso): si può perché è lo stesso file — da fuori l'underscore dice "non toccare"

**Come testare:** `cd python/p05/ex1 && python3 data_stream.py` (output identico all'esempio del subject, verificato; bugfix 5/11: il validate di Log qui e in ex2 aveva lo stesso buco delle chiavi mancanti di ex0 — corretto in entrambi, edge case verificati)

**Teoria — il POLIMORFISMO spiegato (la domanda centrale del modulo):**
- La parola: poli = molti, morfos = forme → "molte forme"
- **In una riga:** la STESSA chiamata produce comportamenti DIVERSI a seconda dell'oggetto che la riceve. `proc.validate([3.14,-1,2.71])` → True se proc è Numeric, False se è Text, False se è Log — stessa riga, 3 comportamenti (ogni figlia ha riempito il buco a modo suo)
- Il meccanismo è la ricerca che sale (vista in ex0): Python cerca il metodo nella classe DELL'oggetto → trova la versione della figlia → gira quella. Questa ricerca automatica È il polimorfismo
- **Analogia C:** in C non esiste — lo faresti a mano con un puntatore a funzione nella struct (vtable): `proc->validate(proc, data)` gira codice diverso secondo il puntatore. Python fa lo stesso automaticamente
- **Analogia di parole:** il verbo "aprire" — apri la porta, la bottiglia, il libro: un verbo, molte azioni. validate è il verbo: sul Numeric controlla numeri, sul Text stringhe, sul Log dizionari
- **Il vantaggio:** chi usa gli oggetti scrive UNA riga e gestisce tutti i tipi; un QuartoProcessor nuovo = registrarlo, ZERO modifiche al router
- **Risposta da evaluation:** "polimorfismo significa che la stessa chiamata di metodo si comporta diversamente in base alla classe dell'oggetto: ogni figlia riempie i buchi del contratto a modo suo, e Python, cercando il metodo nella classe dell'oggetto, esegue automaticamente la versione giusta — così chi usa gli oggetti non deve sapere che tipo sono"

**Teoria — le 2 domande del subject (da evaluation):**
- **"How does polymorphism allow the DataStream to handle different data types without knowing their specific implementations?"** → il router conosce SOLO il contratto: chiama `validate`/`ingest` con gli STESSI nomi su oggetti diversi, e ognuno risponde a modo suo (il buco riempito da ogni figlia). Non serve sapere CHE classe sia: basta che rispetti DataProcessor — la garanzia di ex0. È il centralino che inoltra la chiamata senza sapere chi risponderà
- **"What are the benefits of this design approach?"** → (1) aggiungere un 4° processore = UN register_processor, ZERO modifiche al router (il centralino non cambia mai); (2) il router resta semplice: niente if a catena sui tipi; (3) ogni lavoratore tiene le SUE regole chiuse in casa sua (incapsulamento); (4) il contratto rende sicuro il salto nel buio: se è registrato, i metodi ci sono
- **Registrare = consegnare il contratto:** il DataStream si fida che qualunque cosa registrata rispetti l'interfaccia di DataProcessor (è per questo che la classe astratta esiste)

**Codice:** in `python/p05/ex1/data_stream.py` (già scritto e testato)

## ex2 — data_pipeline — i plugin con Protocol

**Cosa fa in concreto:** completa la pipeline di ex1 con la parte di USCITA. Il DataStream impara `output_pipeline(nb, plugin)`: estrae fino a nb pezzi da OGNI processore registrato e li consegna su un vassoio a un plugin che li formatta e stampa — due plugin: CSV (valori separati da virgole) e JSON (coppie chiave-valore). Il main: registra i 3 → batch 1 → esporta 3 pezzi a testa in CSV → batch 2 → esporta 5 a testa in JSON. Output verificato identico al subject.

**★ PRIME VOLTE qui:** `Protocol` (duck typing / structural typing)

**★ L'albero genealogico:**

```
ABC
 └── DataProcessor (astratta)        ← copia di ex0/ex1
      ├── NumericProcessor
      ├── TextProcessor
      └── LogProcessor

ExportPlugin (Protocol)              ← NUOVO: dichiara la FORMA del plugin
      (NESSUNO eredita da lui!)

CsvPlugin    ← NON è figlia di nessuno: ha solo process_output
JsonPlugin   ← idem

DataStream   ← come ex1 + il metodo nuovo output_pipeline
```

Il punto chiave: CsvPlugin e JsonPlugin NON hanno nessun antenato comune — non ereditano da ExportPlugin. Sono due classi libere che hanno il metodo `process_output`. Questo È il concetto nuovo.

**★ IL PROTOCOL (l'unico concetto nuovo):** `class ExportPlugin(Protocol)` con `def process_output(self, data: list[tuple[int, str]]) -> None: ...` — sembra un abstractmethod (il corpo `...`) ma il meccanismo è TOTALMENTE diverso:

| | ABC (ex0) | Protocol (ex2) |
|---|---|---|
| Chi lo rispetta | DEVE ereditare dalla madre | chiunque abbia il metodo giusto |
| Chi controlla | Python a RUNTIME: figlia senza il metodo → non si crea | SOLO mypy: a runtime non controlla NIENTE |
| Nome del gioco | nominal typing (conta la parentela) | duck typing / structural typing (conta la FORMA) |

**Duck typing** = "se cammina come un'anatra e starnazza come un'anatra, è un'anatra": se la classe ha `process_output` con la firma giusta, mypy la accetta come ExportPlugin — senza parentele (il subject: "made export-compatible through duck typing"). **Conseguenza da evaluation:** il Protocol NON protegge a runtime — oggetto senza process_output → AttributeError solo QUANDO viene chiamato. L'ABC protegge, il Protocol documenta: l'annotazione `plugin: ExportPlugin` è il post-it per mypy.

**COSA È ESATTAMENTE il Protocol (le 4 prove del demo):** una classe del modulo typing il cui unico lavoro è DESCRIVERE UNA FORMA (metodi + firme) — uno stampino. Prova 1: `ExportPlugin()` → `TypeError: Protocols cannot be instantiated` (non si crea: esiste solo come descrizione). Prova 2: `issubclass(CsvPlugin, ExportPlugin)` → TypeError "Instance and class checks can only be used with @runtime_checkable protocols" (a runtime Python rifiuta persino di confrontarlo). Prova 3: `CsvPlugin.__bases__` = (object,) — il plugin NON eredita da lui. Prova 4: oggetto senza process_output → AttributeError solo alla CHIAMATA (nessun controllo a runtime). Il metodo `...` dentro il Protocol non gira MAI: è solo la forma scritta. Chi lo usa: SOLO MYPY — legge `plugin: ExportPlugin`, confronta la STRUTTURA dell'oggetto (ha process_output? sì → ok) e accetta o rifiuta a tempo di scrittura; Python esegue e se ne frega. Definizione da evaluation: "Protocol è un tipo del modulo typing che descrive una FORMA senza imporre parentele: a runtime è inerte (non si istanzia, non si controlla, i suoi metodi non girano), mypy lo usa per accettare qualunque oggetto con quella forma (structural typing). L'ABC invece è un contratto imposto a runtime sull'ereditarietà"
**RUNTIME = quando il programma viene eseguito** (vs tempo di scrittura: quando mypy/linter/compilatore analizzano il codice fermo). ABC = controllo a runtime (Python esplode mentre il programma gira); Protocol = controllo solo a tempo di scrittura (mypy); isinstance = runtime. In C: compile time (gcc) vs runtime (il binario che gira — il segfault è un errore a runtime). Analogia: la revisione della macchina (mypy) vs la guida vera (runtime) — una macchina mai revisionata può partire e si rompe in corsa (AttributeError). L'ABC è il dispositivo che blocca la partenza se manca un pezzo; il Protocol è la lista dei controlli del meccanico

**La meccanica di output_pipeline, giro giro:**

```
for proc in self._processors:          # ogni lavoratore della rubrica
    data = []                          # il VASSOIO vuoto
    for _ in range(nb):                # prova a estrarre nb pezzi
        if len(proc._data) == 0:       # magazzino vuoto? (LA GUARDIA!)
            break
        data.append(proc.output())     # pop e metti sul vassoio
    plugin.process_output(data)        # consegna il vassoio al plugin
```

La guardia `if len(proc._data) == 0: break` è la protezione che mancava in ex1: magazzino con meno di nb pezzi → si estrae quello che c'è e basta, niente IndexError (fase JSON: Text ne ha 4 con nb=5 → escono 4). I 2 plugin — stessi ingredienti, ricette diverse: CsvPlugin = `values = [piece for _, piece in data]` (unpacking che butta il rank col `_`) → `",".join(values)` (il join di p04) → "3.14,-1,2.71" · JsonPlugin = `items = [f'"item_{rank}": "{piece}"' for rank, piece in data]` (qui il rank SERVE: diventa la chiave) → `"{" + ", ".join(items) + "}"` → {"item_3": "42", ...}.

**Esecuzione (traccia completa):** registra i 3 → batch 1 → stats 4/3/2 → `output_pipeline(3, CsvPlugin())` → 3 pezzi a testa → stats 4/1, 3/0, 2/0 (il CSV ha mangiato i rank 0,1,2 di ogni processore) → batch 2 → stats 11/8, 7/4, 4/2 → `output_pipeline(5, JsonPlugin())` → Numeric ha 8 pezzi, ne escono 5 con rank che RIPARTONO DA 3: item_3, item_4... perché i biglietti 0,1,2 li aveva già consumati il CSV — **il rank non si azzera MAI: è la storia del processore. È per questo che il subject stampa item_3 e non item_0 — domanda da evaluation garantita.** Text ne ha 4 → escono 4 (item_3..item_6) · Log ne ha 2 → item_2, item_3. Stats finali: Numeric 11/3, Text 7/0, Log 4/0. **ATTENZIONE ai nomi:** il "total 4" delle stats NON è la variabile locale `data` di output_pipeline (il vassoio, lista vuota fresca a ogni chiamata — non compare mai nelle stats): è `proc._total`, l'ATTRIBUTO del processore. La riga delle stats è `f\"{proc.name}: total {proc._total} items processed, remaining {len(proc._data)} on processor\"` — total = _total (la storia: [3.14,-1,2.71] → 3 pezzi + 42 → 1 pezzo = 4), remaining = len(_data) (il magazzino). `data` è un nome generico riusato ovunque (validate(data), ingest(data), process_output(data), data=[]): ogni volta è una variabile diversa di un metodo diverso

**Come testare:** `cd python/p05/ex2 && python3 data_pipeline.py` (output identico al subject, verificato; il validate di Log qui ha ricevuto lo stesso fix delle chiavi di ex0/ex1)

**Teoria:**
- **Plugin, definizione semplice:** pezzo INTERCAMBIABILE che si ATTACCA a un sistema già funzionante per aggiungergli una capacità (qui: un formato di export) senza toccare il sistema — da "plug in" = attaccarsi. Il sistema definisce la PRESA (la forma richiesta: il Protocol ExportPlugin), il plugin è la SPINA: qualunque pezzo con quella forma si attacca. Perché CSV e JSON sono plugin: (1) intercambiabili — la STESSA chiamata `output_pipeline(nb, plugin)` cambia formato con ZERO modifiche al DataStream; (2) esterni al sistema (non ereditano da niente); (3) hanno la forma giusta (process_output). Prova del nove da evaluation: per aggiungere un formato XML basta scrivere una classe XmlPlugin con process_output e passarla — il DataStream non cambia. Analogia: la presa della corrente — forma fissa, qualunque spina giusta ci si attacca (lampada, TV, aspirapolvere); il muro non sa cosa stai attaccando
- **Protocol vs ABC (domanda da evaluation):** la ABC obbliga a ereditare e Python controlla alla creazione (nominal typing); il Protocol non obbliga a nulla — conta solo la forma (structural typing), controllata da mypy, zero controlli a runtime. Niente `class CsvPlugin(ExportPlugin)`: basta `def process_output(...)`
- **Il rank attraversa tutto il sistema:** output() dà (rank, pezzo); il CSV lo butta (`_`), il JSON lo usa per le chiavi item_N — il motivo per cui i numeri non ripartono da 0

**Codice:** in `python/p05/ex2/data_pipeline.py` (già scritto e testato)



---

# p06 — The Codex (Import e moduli)

**Struttura del progetto (il subject la impone):** un package `alchemy/` con sottopackage `grimoire/` e `transmutation/`, un `elements.py` alla radice, e 14 script `ft_*.py` che testano i 4 misteri. Tutto sta in `python/p06/`.

## ★ PRIMA VOLTA — i 4 misteri degli import (tutta la teoria in un colpo)

**Mistero 1 — import vs from:** `import elements` carica TUTTO il modulo e lo usi col punto: `elements.create_fire()`. `from elements import create_water` esegue comunque TUTTO il file (come sempre: un modulo gira sempre per intero, una volta sola), ma ti CONSEGNA solo quel nome, e lo chiami DIRETTA: `create_water()`. Stessa roba, due stili: col punto = "cassetta degli attrezzi" (hai un nome per la cassetta), senza = "attrezzo in mano" (hai il nome SOLO dell'attrezzo, la cassetta non ha nome da te).

**Mistero 2 — i package e `__init__.py`:** una cartella con dentro `__init__.py` diventa un PACKAGE importabile col nome della cartella. `__init__.py` gira quando importi il package e decide COSA ESPORRE: nel nostro caso espone `create_air` ma NON `create_earth` — per questo `alchemy.create_earth()` esplode con AttributeError (il "segreto" del subject, voluto). Analogia: `__init__.py` è la vetrina del negozio: la merce che non metti in vetrina non la vendi.

**Mistero 3 — import assoluti vs relativi:** assoluto = percorso completo dalla radice (`from alchemy.elements import create_air`); relativo = percorso DA QUI, coi puntini (`from ..potions import strength_potion` — `..` = cartella superiore, come nei path). Regola del mestiere: dentro un package si preferiscono i relativi (se sposti la cartella non si rompe), fuori gli assoluti.

**Mistero 4 — le dipendenze circolari:** se A importa B e B importa A → `ImportError: cannot import name ... from partially initialized module` (l'esplosione di `ft_kaboom_1`). Il labirinto: A parte, chiede B, B chiede A, A non è finito → cortocircuito. Soluzioni: importare in fondo al file, importare DENTRO le funzioni, o togliere UN lato dell'import (il light_validator non importa dal light_spellbook: il ciclo si spezza — mentre dark_validator e dark_spellbook si importano a vicenda ed esplodono apposta).

## Gli script (tutti testati, l'output è nel subject)

- **ft_alembic_0..5**: i 6 modi di raggiungere elements.py e alchemy — da `import elements` (0) a `from alchemy import create_air` (5). **ft_alembic_4 è volutamente rotto**: `alchemy.create_earth()` → AttributeError (la vetrina non lo espone) — anche mypy dà errore lì, DI PROPOSITO (il subject lo dice)
- **ft_distillation_0..1**: le pozioni — `alchemy/potions.py` importa i 4 elementi (assoluti) e costruisce le frasi; `__init__.py` le espone con ALIAS: `healing_potion as heal`
- **ft_transmutation_0..2**: recipes.py usa UN import assoluto (`from elements import create_fire`, `from alchemy.elements import create_air`) e UNO relativo (`from ..potions import strength_potion`) — il subject ne chiede almeno uno per tipo
- **ft_kaboom_0**: il grimoire LIGHT funziona (il validator ha la sua lista di ingredienti, niente ciclo) → "Spell recorded: Fantasy (Earth, wind and fire - VALID)"
- **ft_kaboom_1**: il grimoire DARK esplode — dark_spellbook importa dark_validator che importa dark_spellbook → ImportError con traceback (voluto, è la dimostrazione del mistero 4)

## ft_alembic_0..1 — il mistero 1 riga per riga (i due stili in pratica)

### ft_alembic_0 — `import elements` (la cassetta)

**Cosa fa in concreto:** stampa il risultato di `elements.create_fire()` — la frase "Fire element created" prodotta dalla funzione dentro elements.py.

**Meccanica dell'import in 3 passi:**
1. Python cerca `elements.py` nella cartella dello script (quella da cui lanci).
2. ESEGUE il file una volta sola, riga per riga: nascono le due funzioni `create_fire` e `create_water`, e il modulo finisce in CACHE (sys.modules) — se un altro script lo importa, NON lo riesegue: la cassetta è una sola, condivisa.
3. Ti consegna il MODULO come un oggetto, nella variabile `elements`.

**Il punto = "DENTRO":** `elements.create_fire()` si legge "dentro la cassetta elements, prendi create_fire".

**Differenza dal C:** `#include` incolla il testo del file al suo posto, a compile time. `import` ESegue il file a runtime, una volta, e consegna un oggetto condiviso in cache.

**Punto chiave (dimostrato dallo script stesso):** il modulo ha DUE funzioni ma noi ne usiamo UNA. Importare la cassetta intera non obbliga a usarla tutta: usi ciò che ti serve, quando ti serve.

### ft_alembic_1 — `from elements import create_water` (l'attrezzo in mano)

**Come si legge la riga:** "dal modulo elements, prendimi la funzione create_water".

**La chiamata:** `create_water()` SENZA punto — come se la funzione fosse scritta nel nostro script. In alembic 0 si scriveva `elements.create_fire()` col punto.

**Cosa succede DENTRO (la domanda da 100 all'evaluation):** il file elements.py viene ESEGUITO TUTTO comunque (create_fire nasce anche qui, e la cassetta finisce in sys.modules), ma a noi viene consegnato UN nome solo: `create_water`. Il nome `elements` NON esiste nel nostro script — dimostrato in demo: `print(elements)` → NameError, mentre `'elements' in sys.modules` → True (la cassetta c'è, in cache, ma non abbiamo un nome per raggiungerla).

**Tabella di confronto (risposta pronta):**
- alembic 0: `import elements` → 1 nome in mano (la cassetta) → chiami col punto
- alembic 1: `from elements import create_water` → 1 nome in mano (l'attrezzo) → chiami senza punto
- in entrambi: il file gira TUTTO una volta sola; cambia solo COSA ti viene consegnato come nome

**Analogia C:** `import elements` = hai il puntatore alla struct del modulo e chiami `m->create_water()`. `from elements import create_water` = hai copiato un puntatore a funzione singolo in una variabile locale e chiami `f()` — la funzione è la stessa, cambia come la tieni in mano.

**Perché esiste lo stile "from":** se usi sempre la stessa funzione ti risparmi il punto a ogni chiamata, e chi legge lo script vede in cima esattamente cosa ti serve.

## ft_alembic_2 — `import alchemy.elements` (il package, prima puntata)

**Cosa fa in concreto:** stampa il risultato di `alchemy.elements.create_earth()` — raggiunge il file `alchemy/elements.py` PASSANDO ATTRAVERSO il package.

**Come si legge la riga 1:** "carica il package alchemy, e dentro di esso il modulo elements". La parola che ti resta in mano è la PRIMA: `alchemy` (il package). Il file dentro si raggiunge incatenando: `alchemy.elements`.

**Novità — il package:** una CARTELLA con dentro `__init__.py` diventa importabile col nome della cartella. `__init__.py` è la firma che la trasforma in package.

**Meccanica in 4 passi:**
1. Python trova la cartella `alchemy/` e vede `__init__.py` → è un package.
2. PRIMA gira l'`__init__.py` (la porta d'ingresso): fa 4 import relativi e mette in vetrina `create_air`, `heal`, `strength`, `transmutation`.
3. Poi gira `alchemy/elements.py`: nascono `create_earth` e `create_air`.
4. Ti consegna il nome `alchemy` = l'oggetto-package; i sotto-moduli caricati diventano suoi attributi (`alchemy.elements`, `alchemy.potions`...).

**La demo (valori veri):** dopo `import alchemy.elements`, dentro `alchemy` ci sono: `create_air`, `elements`, `heal`, `potions`, `strength`, `transmutation` — ma `create_earth` NON c'è (False). Eppure `alchemy.elements.create_earth()` FUNZIONA: la vetrina non l'ha esposto, ma il retro del negozio è raggiungibile passando dall'attributo `elements`.

**Effetto collaterale (stessa lezione dell'import che ESegue):** pur chiedendo solo `elements`, sono stati caricati anche `potions` e `transmutation.recipes` — perché l'`__init__.py` gira per intero e importando quei pezzi li esegue. (sys.modules lo dimostra.)

**`__all__`:** ultima riga dell'`__init__.py` = il listino ufficiale della vetrina (usato da `from alchemy import *` e come dichiarazione di cosa è pubblico). NON è un lucchetto: non blocca l'accesso diretto ai file — create_earth resta raggiungibile dal retro.

**La distinzione che anticipa la bomba di ft_alembic_4:**
- `alchemy.elements.create_earth()` → porta sul retro (file diretto) → FUNZIONA
- `alchemy.create_earth()` → vetrina (dentro alchemy senza passare da elements) → AttributeError, la vetrina non l'ha mai importato

**Analogia C:** il package è la cartella `lib/alchemy/`; `__init__.py` è l'header-ombrello `alchemy/alchemy.h` che include SOLO gli header pubblici; ma puoi sempre includere direttamente `alchemy/elements.h` — la dichiarazione c'è, che l'ombrello la esponga o no.

## alchemy/__init__.py — lettura riga per riga (la porta d'ingresso)

NON lo chiami tu: Python lo esegue DA SOLO quando entri nella cartella, PRIMA del modulo che hai chiesto.

**Riga 1** — `from .elements import create_air` — "dal modulo elements che sta IN QUESTA cartella, prendimi create_air".
★ PRIMA VOLTA — **il puntino davanti** = import RELATIVO: `.` vuol dire "questa stessa cartella (il package in cui sono)". Il file non sa nemmeno che la cartella si chiama "alchemy": dice solo "da qui". Effetto: esegue elements.py per intero (nasce anche create_earth — il file gira sempre tutto) e mette create_air in vetrina.
**Analogia C:** il puntino = `#include "elements.h"` con le VIRGOLETTE (relativo al file corrente); `from alchemy.elements import ...` = `#include <alchemy/elements.h>` con gli ANGOLI (assoluto dalla radice).

**Riga 2** — `from .potions import healing_potion as heal` — "dal modulo potions in questa cartella, prendimi healing_potion e chiamala heal".
★ PRIMA VOLTA — **`as` = ALIAS**, rinomina da qui in poi. Effetto doppio: esegue potions.py (effetto collaterale) e mette in vetrina il nome corto `heal`.

**Riga 3** — stesso per `strength_potion` → in vetrina come `strength`.

**Riga 4** — `from . import transmutation` — "da questa cartella, prendimi il sotto-package transmutation". Effetto a catena: esegue `transmutation/__init__.py`, che fa `from .recipes import lead_to_gold` → esegue pure recipes.py. Per questo la demo trovava tutti quei moduli in sys.modules senza che nessuno li avesse chiesti.

**Riga 6** — `__all__ = [...]` — il listino ufficiale della vetrina (per `from alchemy import *` e come documentazione). NON è un lucchetto: create_earth non è in lista ma resta raggiungibile passando da `alchemy.elements`.

**Verificato con la demo:** l'alias è lo STESSO oggetto, non una copia: `alchemy.heal is alchemy.potions.healing_potion` → True (stesso indirizzo di memoria).

**L'ordine vero quando "entri nella cartella" (ft_alembic_2):**
1. La porta si apre da sola: gira `alchemy/__init__.py` → esegue elements.py, potions.py, transmutation (→ recipes.py) e riempie la vetrina con create_air, heal, strength, transmutation.
2. Poi `import alchemy.elements` — ma elements.py è GIÀ stato eseguito dalla riga 1 della porta → cache! Non riesegue niente, dà solo il nome `alchemy`.
3. `alchemy.elements.create_earth()` → retro → trovata → "Earth element created".

**CARICATA ≠ IN VETRINA (la distinzione chiave, dimostrata con la demo):** l'`__init__.py` NON decide cosa viene eseguito — decide solo a chi dà un NOME in vetrina. L'esecuzione è un effetto collaterale che tocca tutto: `import alchemy` esegue elements.py, potions.py e transmutation per intero (tutte le funzioni NASCONO), ma i nomi corti sono solo quelli importati dall'`__init__`.

| funzione | ESEGUITA con `import alchemy`? | nome in VETRINA? | come raggiungerla |
|---|---|---|---|
| create_air | sì | sì | `alchemy.create_air()` |
| create_earth | SÌ (il file gira tutto) | no | `alchemy.elements.create_earth()` |
| healing_potion | sì | no (ma l'alias `heal` sì) | `alchemy.potions.healing_potion()` oppure `alchemy.heal()` |
| strength_potion | sì | no (alias `strength` sì) | `alchemy.potions.strength_potion()` oppure `alchemy.strength()` |

Prova lampo: `alchemy.healing_potion()` → AttributeError (in vetrina c'è solo l'alias), ma `alchemy.potions.healing_potion()` funziona — stesso gioco di create_earth su un'altra coppia.

## ft_alembic_3 — `from alchemy.elements import create_air` (package + stile from)

**Cosa fa in concreto:** stampa il risultato di `create_air()` — stessa funzione raggiungibile sia dal file sia dalla vetrina, qui presa dal FILE.

**Come si legge la riga 1:** "dal package alchemy, dal modulo elements che sta dentro, prendimi create_air". Percorso ASSOLUTO (niente puntino): lo script sta alla RADICE, fuori dal package — da fuori indichi il percorso completo; l'`__init__.py` invece è DENTRO e usa il puntino. Regola del mistero 3 applicata dal vivo: **fuori → assoluto, dentro → relativo**.

**La demo (valori veri):**
- in mano c'è SOLO `create_air` — `alchemy` non esiste nello script (NameError), come in alembic_1
- la porta è girata lo stesso: sys.modules contiene alchemy, elements, potions, transmutation, recipes — entri nel package → la porta gira SEMPRE, qualunque cosa tu chieda
- `create_air` sta SIA nel file SIA in vetrina (stessa funzione, due porte) — qui la prendiamo dal file perché il percorso punta a `elements`

**Il quadro dei 4 script visti finora (due stili × due percorsi):**
- alembic_0: `import` + file radice → `elements.create_fire()`
- alembic_1: `from` + file radice → `create_water()`
- alembic_2: `import` + package→file → `alchemy.elements.create_earth()`
- alembic_3: `from` + package→file → `create_air()`

## ft_alembic_4 — `import alchemy` e la BOMBA AttributeError (voluta dal subject)

**Cosa fa in concreto:** importa SOLO il package (senza dire quale file), chiama `alchemy.create_air()` dalla vetrina (funziona), poi prova `alchemy.create_earth()` e ESPLODE con AttributeError + traceback. Output atteso dal subject: il traceback È l'output giusto (eccezione ammessa, come le altre bombe).

**Lettura riga per riga:**
1. `import alchemy` — importi la cartella senza file: gira SOLO la porta (`__init__.py`). In mano hai l'oggetto-package con ciò che la vetrina espone: create_air, heal, strength, transmutation (+ elements e potions come attributi).
2. `alchemy.create_air()` — UN punto = "dentro alchemy" → vetrina → "Air element created". ✅
3. `alchemy.create_earth()` → **AttributeError: module 'alchemy' has no attribute 'create_earth'. Did you mean: 'create_air'?** — perché `create_earth` non è MAI stato importato nel namespace del package: vive solo dentro `alchemy/elements.py`. Il "Did you mean" è il suggerimento automatico di Python.

**Il trucco completo (risposta da evaluation):** la parola giusta non è "protetta", è "NON IN VETRINA". Dimostrato con la demo: nello stesso script, `alchemy.elements.create_earth()` FUNZIONA — il retro esiste anche importando solo `alchemy`, perché la riga 1 della porta (`from .elements import create_air`) ha eseguito elements.py e attaccato `elements` come attributo del package.
- `alchemy.create_earth()` → ❌ la vetrina non lo espone
- `alchemy.elements.create_earth()` → ✅ il file ce l'ha

Il subject non chiede di proteggere niente: chiede di capire che la vetrina decide cosa si raggiunge col nome corto, e che il percorso completo passa comunque.

**Analogia C:** l'oggetto-package è una struct di puntatori a funzione costruita dall'`__init__.py`; `create_earth` non è un membro della struct → in C errore di compilazione, in Python AttributeError a RUNTIME (la ricerca degli attributi è dinamica).

**`# type: ignore[attr-defined]`:** marca il punto anche per mypy (che lì dà errore DI PROPOSITO, come dice il subject).

## ft_alembic_5 — `from alchemy import create_air` (l'attrezzo preso DALLA VETRINA)

**Cosa fa in concreto:** stampa il risultato di `create_air()` chiamata a ZERO puntini, presa dalla vetrina con lo stile `from`.

**Come si legge la riga 1:** "dal package alchemy — cioè dalla sua VETRINA — prendimi create_air". Funziona solo perché l'`__init__.py` l'ha messa in esposizione.

**ZERO puntini, e attenzione: è un DEVO, non un posso.** Con lo stile `from` hai in mano solo l'attrezzo: il nome `alchemy` NON esiste nello script (demo: NameError). Scrivere `alchemy.create_air()` qui → NameError anche quello.

**La novità — la vetrina blocca anche alla PORTA, non solo alla chiamata (demo):**
- `from alchemy import create_earth` → ImportError: cannot import name 'create_earth' from 'alchemy' — subito, all'import
- (ft_alembic_4) `alchemy.create_earth()` → AttributeError — dopo, alla chiamata

Stessa ragione (non è in vetrina), due errori diversi: l'ImportError scatta nel momento in cui il `from` chiede il nome alla vetrina; l'AttributeError quando chiedi l'attributo a runtime. Il messaggio dell'ImportError indica pure il colpevole: `__init__.py`.

**Quadro finale della serie alembic (2 stili × 3 porte):**
- file alla radice: `import elements` → `elements.create_fire()` (0) · `from elements import create_water` → `create_water()` (1)
- package → file: `import alchemy.elements` → `alchemy.elements.create_earth()` (2) · `from alchemy.elements import create_air` → `create_air()` (3)
- vetrina: `import alchemy` → `alchemy.create_air()` + bomba AttributeError (4) · `from alchemy import create_air` → `create_air()` (5)

## ft_kaboom_1 — il ciclo dark (la bomba ImportError)

**ATTENZIONE alla causa:** NON esplode per la vetrina né per i puntini — il percorso `from alchemy.grimoire.dark_spellbook import dark_spell_record` è perfettamente legale (stessa forma di kaboom_0 col light, che funziona). Esplode SOLO per il CICLO A↔B. Le due bombe di p06 hanno cause diverse: ft_alembic_4 = nome non in vetrina; ft_kaboom_1 = ciclo.

**Chi sta dove (file e funzioni separati, i nomi si somigliano tutti):**
- `dark_spellbook.py` — riga 1: importa `dark_validate_ingredients` da `.dark_validator`; funzioni: `dark_spell_allowed_ingredients`, `dark_spell_record`
- `dark_validator.py` — riga 1 (# bomba): importa `dark_spell_allowed_ingredients` da `.dark_spellbook`; funzione: `dark_validate_ingredients`
Il ciclo è tra i FILE, alla riga 1 di ciascuno: spellbook vuole la funzione del validator, il validator vuole la funzione dello spellbook → anello.

**Esecuzione vera (il traceback è la prova filmata):**
1. ft_kaboom_1 riga 1: `from alchemy.grimoire.dark_spellbook import dark_spell_record` — "dal file dark_spellbook prendimi la funzione dark_spell_record"
2. Girano le porte: alchemy/__init__.py (non tocca il dark) e grimoire/__init__.py (importa SOLO il light). Nessun problema.
3. Parte dark_spellbook.py. MOMENTO CHIAVE: prima di eseguire la riga 1, Python registra il modulo in sys.modules come GUSCIO VUOTO — scatola col nome, senza contenuto = "partially initialized".
4. dark_spellbook riga 1: chiede dark_validate_ingredients → Python SOSPENDE lo spellbook (guscio che resta vuoto) e parte con dark_validator.py.
5. dark_validator riga 1: chiede dark_spell_allowed_ingredients → Python trova il GUSCIO in sys.modules ma è VUOTO (lo spellbook non è mai arrivato alla riga che definisce quella funzione, è bloccato alla riga 1) → ImportError.

**Il dettaglio da evaluation:** l'errore non dice "dark_spellbook non esiste" — dice "partially initialized": il modulo ESISTE nel registro ma è nato a metà. Python registra prima di eseguire, quindi il secondo giro lo trova, ma lo trova vuoto.

**Perché il LIGHT non esplode (il trucco del subject):** light_validator.py NON HA NESSUN IMPORT — la lista `ALLOWED` se la porta da casa. Il validator dark invece non ha lista sua: la CHIEDE allo spellbook (chiama `dark_spell_allowed_ingredients()` dentro `dark_validate_ingredients`) → due frecce → anello. Il light spezza l'anello dando a UN lato tutto ciò che gli serve.

**Analogia C:** due .c si includono a vicenda gli header senza problemi (include guard: il testo si incolla, nulla si esegue). In Python gli import ESEGUONO: A per consegnare i nomi deve FINIRE, B per finire ha bisogno di A finito → stallo → ImportError. Come due persone che aspettano entrambe che l'altro finisca di parlare.

## Chiusura p06 — distillation, transmutation e il `..` (passata veloce, 8/11)

**distillation 0-1:** nessun concetto nuovo. potions.py importa i 4 elementi (2 assoluti: `from alchemy.elements import ...` e `from elements import ...`) e costruisce le frasi delle pozioni; gli script usano stili già visti (vetrina + alias `heal`/`strength` dal lato del cliente).

**transmutation 0-2:** i 3 script ripetono le 3 porte di alembic (file diretto / sotto-package / vetrina di alchemy). L'UNICA sintassi nuova di tutto il resto di p06 è il `..` di recipes.py.

**Il `..` (doppio puntino):** recipes.py sta in `alchemy/transmutation/` e ha TRE import in fila (il subject ne vuole almeno uno per tipo):
- `from elements import create_fire` — ASSOLUTO (file alla radice)
- `from alchemy.elements import create_air` — ASSOLUTO (package → file)
- `from ..potions import strength_potion` — RELATIVO: `..` = "sali di un piano, poi entra in potions". IDENTICO al terminale: `cd ..` = cartella padre. Il puntino singolo `.` = "questa cartella", il doppio `..` = "la cartella di sopra".

**Ripasso p06 in 4 punti (tutto negli appunti):** scala della comodità (retro/vetrina/attrezzo = 2/1/0 puntini) · caricata ≠ in vetrina · le 2 bombe con cause diverse (ft_alembic_4 AttributeError = nome non in vetrina; ft_kaboom_1 ImportError = ciclo A↔B) · il guscio "partially initialized" (registrato prima di eseguire, trovato vuoto al secondo giro).

**Come testare:** `cd python/p06 && python3 ft_alembic_0.py` ecc. — ogni script si lancia da `python/p06/` (gli import sono relativi a quella cartella).

**Teoria extra:**
- **Chi è cosa:** `import`, `from`, `as` → parole chiave; `elements.py` / `alchemy/` → moduli e package NOSTRI; `__init__.py` → il file speciale di Python (nome DUNDER riservato) che trasforma la cartella in package; il resto è tutto nostro
- **Commenti (politica 8/11):** nessun commento nei .py di p06, tranne `# bomba` sui DUE punti che esplodono (ft_alembic_4 riga 9 — AttributeError; `dark_validator.py` riga 1 — il ciclo dark) e il `# type: ignore[attr-defined]` FUNZIONALE: non è un commento per umani ma un'istruzione per mypy, e sulla stessa riga va messo PRIMA di `# bomba` (se lo segue, mypy non lo riconosce più — verificato). Le due bombe volute: ft_alembic_4 (AttributeError) e ft_kaboom_1 (ImportError) — gli altri 11 script girano puliti.
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

**Traccia riga per riga di battle.py (con i valori reali):**
1. Riga 1 `from ex0 import AquaFactory, FlameFactory` — ex0 è un package (cartella+__init__.py, p06). Dietro le quinte: gira la porta ex0/__init__.py → `from .factories import ...` → esegue factories.py → la sua riga 2 `from .creatures import ...` → esegue creatures.py → nascono Creature (col buco attack) e le 4 figlie → nascono CreatureFactory (2 buchi) e le 2 fabbriche → la porta consegna i 2 nomi a battle.py.
2. Riga 2 `from ex0.factories import CreatureFactory` — factories.py è GIÀ eseguito (cache): prende solo il nome, usato SOLO come etichetta nel type hint di riga 5 (mai per creare oggetti).
3. Righe 5-31 — le tre `def` sono DEFINIZIONI: imparate a memoria, non eseguite.
4. Riga 34 `if __name__ == "__main__":` → "questo file è stato lanciato direttamente?" → sì → main().
5. Riga 29 `test_factory(FlameFactory())` — prima si valuta l'argomento: FlameFactory() = oggetto SENZA attributi (nessun __init__ scritto → default): è solo uno SPORTELLO.
6. Dentro test_factory: `base = factory.create_base()` → ricerca nella classe FlameFactory → trovato → `return Flameling()` → Flameling.__init__ → `super().__init__("Flameling", "Fire")` → il costruttore della MADRE crea name e creature_type. `base` = mostro completo.
7. `base.describe()` → Flameling NON ce l'ha → la ricerca SALE alla madre → gira quella di Creature → "Flameling is a Fire type Creature".
8. `base.attack()` → Flameling CE l'HA (buco riempito) → gira quella della figlia → "Flameling uses Ember!".
9. Riga 30: stesso giro con AquaFactory → Aquabub (Water Gun!) e Torragon (Hydro Pump!).
10. Riga 31 test_battle: due sportelli → due mostri base → describe/describe/fight!/attack/attack → Ember! vs Water Gun!.

**Osservazione che chiude il pattern:** il main NON nomina MAI una classe concreta — niente "Flameling" né "Pyrodon": parla solo con le fabbriche (`test_factory(FlameFactory())`). I nomi concreti vivono SOLO dentro factories.py (righe 19 e 22). Se domani cambiano i mostri, battle.py non si tocca: la fabbrica è l'unica che conosce i nomi delle classi.

**Lettura di creatures.py (primo file eseguito nella catena):**
- La coppia che rende astratta Creature: `class Creature(ABC)` + `@abstractmethod` sul metodo. Il decoratore È quello che segna il buco.
- I tre puntini `...` = segnaposto (Ellipsis): una `def` DEVE avere un corpo, `...` = "corpo vuoto". Da solo non rende nulla astratto.
- `describe` è CONCRETA ed EREDITATA: le 4 figlie non la riscrivono — la ricerca sale e gira quella della madre, che legge `self.name`/`self.creature_type` DI QUEL mostro (una sola funzione, dati che cambiano col self).
- Le figlie: ognuna chiama `super().__init__("Nome", "Tipo")` (attributi creati dal costruttore della madre) e riempie il buco `attack` con la sua mossa (stringa). Il tipo è solo una STRINGA, nessuno lo controlla (Pyrodon: "Fire/Flying").
- Chi è cosa: `abc`, `ABC`, `abstractmethod` predefiniti (libreria standard `abc`); `str` built-in; il resto tutto nostro.

**Lettura di factories.py (secondo file eseguito):**
- Riga 2 `from .creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon` — import relativo (p06, il puntino) che ESEGUE creatures.py (per questo nella catena gira prima creatures, poi factories). Una classe si importa come un nome qualunque: le classi sono oggetti anche loro.
- `CreatureFactory(ABC)` — madre astratta con DUE buchi (create_base, create_evolved) e type hint `-> Creature` = "consegno una creatura (o una figlia)". Non ha __init__: nessun attributo. NON istanziabile (astratta).
- `FlameFactory`/`AquaFactory` — riempiono entrambi i buchi con UNA riga ciascuno: `return Flameling()` si legge "prendi la classe Flameling, chiamala con le parentesi → nasce un oggetto → consegnalo". Tutto il lavoro vero del file: 4 righe.
- Risposte da evaluation: (1) CreatureFactory non si istanzia (astratta); (2) `-> Creature` e non `-> Flameling` perché il contratto dice solo "una creatura" — Flameling È una Creature, polimorfismo (stessa etichetta, un figlio qualunque sotto); (3) i nomi delle classi concrete vivono SOLO qui, dentro i return — la fabbrica è il distributore automatico: tu premi `create_base`, lui costruisce la classe giusta.
- Analogia C: `create_base` ritorna `Creature *` ma dentro fa `malloc(sizeof(Flameling))` — chi chiama vede solo il puntatore alla madre.
- `ex0/__init__.py` (2 righe, logica p06): espone solo `AquaFactory, FlameFactory` — le creature concrete non passano dalla vetrina.

**Come testare:** `cd python/p07 && python3 battle.py`

**Teoria:** `Creature` è astratta (attack senza corpo, `...`); `CreatureFactory` è astratta (create_base/create_evolved senza corpo); le classi concrete implementano tutto. L'`__init__.py` espone `FlameFactory, AquaFactory` — se qualcuno prova `from ex0 import Flameling` → errore: la creatura concreta non è in vetrina (stesso trucco di p06).

**Codice:** in `python/p07/ex0/` (creatures.py, factories.py, __init__.py) + `python/p07/battle.py`

## ex1 — capacitor — le capability (ereditarietà MULTIPLA)

**Cosa fa in concreto:** aggiunge due "capacità" riusabili (guarire, trasformarsi) che si ATTACCANO alle creature: le creature-guaritrici sanno attaccare E curare; le creature-trasformiste dopo transform() attaccano più forte e con revert() tornano normali.

**★ PRIME VOLTE qui:** ereditarietà multipla (`class Sproutling(Creature, HealCapability)`)

**Cosa chiede:** capacità SEPARATE dalle creature (HealCapability, TransformCapability — NON ereditano da Creature!) e creature che ereditano da ENTRAMBE: `class Sproutling(Creature, HealCapability)`. Due nuove famiglie con le loro factory.

**Il concetto in una riga:** una classe può avere DUE genitori: la creatura (cosa È) + la capacità (cosa SA FARE). Il TransformCapability ha uno STATO (`self._transformed`): dopo `transform()` l'`attack()` cambia (colpisce potenziato), dopo `revert()` torna normale — lo stato persiste tra le chiamate perché sta nell'oggetto.

**ALBERO GENEALOGICO (regola permanente):**
```
ABC
 ├── Creature (da ex0, IMPORTATA) — describe concreta, attack buco
 ├── HealCapability (ABC) — heal buco, NESSUN __init__
 ├── TransformCapability (ABC) — __init__ VERO (_transformed=False) + transform/revert buchi
 ├── Sproutling(Creature, HealCapability)        ┐
 ├── Bloomelle(Creature, HealCapability)         │ creature con DUE madri:
 ├── Shiftling(Creature, TransformCapability)    │ creatura + capacità
 └── Morphagon(Creature, TransformCapability)    ┘
CreatureFactory (da ex0) — 2 buchi
 ├── HealingCreatureFactory → Sproutling()/Bloomelle()
 └── TransformCreatureFactory → Shiftling()/Morphagon()
```
Le capacità sono SORELLE di Creature (ereditano da ABC, NON da Creature): sono espansioni riusabili, si attaccano a QUALUNQUE creatura aggiungendole come seconda madre.

**Le DUE regole della meccanica nuova:**
1. **MRO (ordine di ricerca):** `Sproutling(Creature, HealCapability)` — la ricerca parte dalla classe dell'oggetto e sale da SINISTRA a destra: Sproutling → Creature → HealCapability. Il primo che ha il metodo vince. `describe()` → non in Sproutling → Creature sì → gira la madre. `heal()` → Sproutling ce l'ha → gira la figlia.
2. **`__init__` col NOME della madre + self a MANO (★ PRIMA VOLTA):** `Creature.__init__(self, "Sproutling", "Grass")` si legge "Creature, esegui il tuo __init__ SU questo oggetto (self a mano)". Con DUE madri `super()` chiamerebbe solo la PRIMA (segue l'ordine delle parentesi) → la manovra classica è chiamare OGNI madre per nome. Quando chiami un metodo attraverso il NOME DELLA CLASSE, Python NON passa self da solo (il PUNTO lo passa, la classe no) → self va scritto a mano. Si chiamano gli __init__ SOLO delle madri che ce l'hanno: Shiftling chiama Creature E TransformCapability (che crea `_transformed` — senza → AttributeError in attack); Sproutling chiama solo Creature (HealCapability non ha __init__).
**Analogia C:** `class Sproutling : public Creature, public HealCapability` (C++) e `Creature.__init__(self, ...)` = chiamare esplicitamente il costruttore della base (`Creature::Creature(this, ...)`).

**DOMANDA D'ORO — la capacità si può dare a runtime? NO (demo):** l'accoppiata si decide alla NASCITA DELLA CLASSE, nel sorgente. Un Flameling già nato NON diventa mai Sproutling: `isinstance(flameling, HealCapability)` → False per sempre, `f.heal()` → AttributeError. Per un mostro di fuoco che guarisce bisogna SCRIVERE una classe NUOVA nel sorgente (`class FireHealer(Creature, HealCapability)`) — la demo l'ha creata al volo: `isinstance(fh, Creature)` True, `isinstance(fh, HealCapability)` True, describe() ereditata gratis da Creature, attack e heal propri. FireHealer NON È né Sproutling né Bloomelle: è una terza classe. La capacità è il pezzo RIUSABILE scritto una volta sola.

**Esecuzione:** capacitor.py → crea la factory → base → `describe()`, `attack()`, `heal()` → factory transform → `transform()` mette `_transformed = True` → `attack()` ora va nel ramo "boosted" (l'if legge lo stato) → `revert()` lo rimette a False.

**Traccia di capacitor.py (il ciclo VIVO dello stato):**
- Riga 1: `from ex1 import HealingCreatureFactory, TransformCreatureFactory` — dalla vetrina (espone solo le 2 factory).
- Guaritrici: `create_base()` → `Sproutling()` → SOLO `Creature.__init__(self, ...)` (HealCapability non ha __init__) → describe (sale alla madre) + attack/heal (propri della figlia). Evolved: Bloomelle.
- Trasformiste: `Shiftling()` → DUE __init__: `Creature.__init__(self, "Shiftling", "Normal")` (name, type) E `TransformCapability.__init__(self)` (`_transformed = False`).
- Il ciclo: attack → `if self._transformed:` → NO (appena nato) → "attacks normally." → `transform()` scrive `_transformed = True` → attack di nuovo → SÌ → "performs a boosted strike!" → `revert()` scrive False → "returns to normal." (Morphagon: normale → morph form → devastating morph strike → stabilizes.)
- **Lo STATO (terzo concetto di p07, dopo factory e capacità):** la stessa identica chiamata `attack()` due volte dà due risposte diverse SENZA argomenti — la differenza sta DENTRO l'oggetto: il flag `_transformed` che transform/revert SCRIVONO e attack LEGGE. L'oggetto RICORDA.
- **Collaborazione tra le madri:** `attack()` riempie il buco di Creature ma il suo comportamento dipende dallo stato creato da TransformCapability — le due madri lavorano insieme nello stesso oggetto.
- Analogia C: un campo della struct (`int transformed;`) che transform() mette a 1, revert() a 0, attack() controlla con `if (monster->transformed)`.

**LA MAPPA DEL BESTIARIO (ex0 + ex1):**
```
EX0 — creature semplici (UNA madre: Creature)
  FlameFactory (famiglia FUOCO)
      Flameling --evolve--> Pyrodon
      tipo Fire          tipo Fire/Flying
      Ember!             Flamethrower!
  AquaFactory (famiglia ACQUA)
      Aquabub --evolve--> Torragon
      tipo Water          tipo Water
      Water Gun!          Hydro Pump!

EX1 — creature con capacità (DUE madri: Creature + Capability)
  HealingCreatureFactory (famiglia GUARITRICI)
      Sproutling --evolve--> Bloomelle
      tipo Grass            tipo Grass/Fairy
      Vine Whip! + heal     Petal Dance! + heal grande
  TransformCreatureFactory (famiglia TRASFORMISTE)
      Shiftling --evolve--> Morphagon
      tipo Normal           tipo Normal/Dragon
      attacco normale/      attacco normale/
      potenziato +          devastante +
      transform/revert      transform/revert
```
**Le 3 regole della mappa:** (1) la freccia evolve È la factory — nel codice non c'è una freccia, c'è `create_base()` → `return Flameling()` e `create_evolved()` → `return Pyrodon()`; ogni famiglia = una classe factory coi suoi 2 pulsanti. (2) Le mosse sono i buchi riempiti: stringhe restituite da `attack()`; per le trasformiste `attack()` è l'unico con un `if` dentro (legge `_transformed` e sceglie la stringa). (3) Le capacità sono le SECONDE madri: Sproutling/Bloomelle = (Creature, HealCapability), Shiftling/Morphagon = (Creature, TransformCapability).
**Cose che NON esistono (trappole da evaluation):** nessun mostro di fuoco che guarisce; nessuna famiglia mista; le capacità non sono creature (niente nome né tipo: sono cartellini di potere, non Pokémon).

**Come testare:** `cd python/p07 && python3 capacitor.py`

**Teoria:**
- **Perché le capability NON ereditano da Creature:** il subject lo dice — un giorno potrebbero servire a NON-creature (oggetti, carte speciali). Tenerle separate = poterle attaccare a chiunque. È il "design for the future"
- **Ereditarietà multipla in Python:** `class X(A, B)` — X prende i metodi di entrambi. L'ordine conta per chi "vince" i conflitti; qui non ce ne sono (Creature e le capability non hanno metodi con lo stesso nome)
- **Lo stato `_transformed`** è il primo esempio di "l'oggetto RICORDA": il metodo transform cambia l'oggetto e l'attacco successivo si comporta diversamente — come il cartellino che resta attaccato

**Codice:** in `python/p07/ex1/` + `python/p07/capacitor.py`

## ex2 — tournament — lo strategy pattern

**Cosa fa in concreto:** organizza un torneo dove ogni creatura combatte con una STRATEGIA assegnata (normale = solo attacco; aggressiva = trasforma-attacca-ripristina; difensiva = attacca-cura). Se la strategia non è adatta alla creatura, il torneo si ferma con un errore chiaro.

**★ PRIME VOLTE qui:** pattern strategy + `cast()` di typing + eccezione NOSTRA (`class StrategyError(Exception): pass`)

**Cosa chiede:** 3 strategie di battaglia (Normal, Aggressive per i trasformisti, Defensive per i guaritori) che decidono COME agisce una creatura in torneo. `is_valid(creature)` controlla la compatibilità, `act(creature)` esegue (e lancia StrategyError se invalida). Il torneo fa combattere tutti contro tutti con le proprie strategie.

**ALBERO GENEALOGICO (regola permanente):** ex2 NON ha né creatures.py né factories.py — riusa TUTTO il bestiario da ex0+ex1 (import assoluti da pacchetto a pacchetto). Aggiunge solo il ramo delle strategie:
```
Exception (built-in)
 └── StrategyError (nostra eccezione)
ABC
 └── BattleStrategy (astratta: is_valid + act = 2 buchi)
      ├── NormalStrategy      is_valid: sempre True · act: attack()
      ├── AggressiveStrategy  is_valid: è TransformCapability? · act: transform→attack→revert
      └── DefensiveStrategy   is_valid: è HealCapability? · act: attack→heal
```

**COMPLETAMENTO DEL BESTIARIO — le coppie lecite:**
- CHIUNQUE + NormalStrategy (sempre valida)
- Shiftling/Morphagon + AggressiveStrategy (esige TransformCapability)
- Sproutling/Bloomelle + DefensiveStrategy (esige HealCapability)
- Il lottatore = COPPIA (creatura, strategia) formata a RUNTIME nel main: `(FlameFactory(), NormalStrategy())`. Confronto chiave con le capacità (ex1): la capacità si decide alla NASCITA della classe (sorgente, seconda madre, NON cambiabile); la strategia si sceglie a RUNTIME (oggetto a parte, cambiabile al volo per lo stesso mostro). Aggiungere una strategia nuova NON tocca il bestiario (principio aperto/chiuso).

**cast() (★ PRIMA VOLTA, da typing):** `cast(Tipo, valore)` restituisce lo STESSO oggetto senza fare NULLA a runtime (demo: tipo invariato) — è una nota per mypy: "fidati, questo oggetto È un Tipo". Serve qui perché la guardia `is_valid` è una funzione OPAca per mypy: dopo `if not self.is_valid(...): raise`, mypy non sa che creature è un TransformCapability e `creature.transform()` darebbe errore — cast lo zittisce. `transforming = cast(TransformCapability, creature)` → due nomi per lo stesso oggetto, il secondo dichiara l'uso "come trasformista". Analogia C: `(TransformCapability *)creature` — ma in C il cast converte davvero a runtime, in Python è solo un'etichetta per il type-checker.

**Lettura di strategies.py:**
- righe 1-2: `from abc import ABC, abstractmethod` (p05) · `from typing import cast` (nuovo)
- righe 3-4: `from ex0.creatures import Creature` e `from ex1.capabilities import HealCapability, TransformCapability` — import ASSOLUTI tra pacchetti fratelli (si poteva col `..`, ma l'assoluto è il più semplice)
- `class StrategyError(Exception): pass` — eccezione NOSTRA: eredita tutto da Exception, `pass` = corpo vuoto. Serve un NOME nostro per catturare SOLO questo errore nel try/except del torneo
- `class BattleStrategy(ABC)` — madre astratta, 2 buchi: `is_valid(creature: Creature) -> bool` e `act(creature: Creature) -> None`
- NormalStrategy: `is_valid` → `return True` (tutti validi); `act` → `print(creature.attack())`
- AggressiveStrategy: `is_valid` → `return isinstance(creature, TransformCapability)` — chiede alla creatura se HA la madre-capacità (l'ereditarietà multipla rende possibile questo isinstance); `act` → prima la GUARDIA: se non valida → `raise StrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")` (doppio controllo di sicurezza) → poi `transforming = cast(...)` → print(transform/attack/revert)
- DefensiveStrategy: speculare con HealCapability: attacco + heal

**Il concetto in una riga:** la strategia è il "piano di battaglia" ATTACCATO alla creatura per il torneo: la creatura non sa combattere in torneo, il piano sì. `act()` di Normal = solo attack; Aggressive = transform → attack → revert; Defensive = attack → heal. Il tournament.py conosce SOLO `act()` — non sa quale piano sia.

**Esecuzione:** tournament.py → `battle([(FlameFactory(), NormalStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])` → crea le creature, tutti contro tutti → per ogni scontro: `strat_a.act(a)` → dentro act: `is_valid`? → no? → `raise StrategyError("Invalid Creature 'Flameling' for this aggressive strategy")` (torneo 1, l'errore voluto) → si → esegue il piano.

**Traccia di tournament.py (10/11):**
1. Righe 1-4: import dalle 3 vetrine (p06, niente di nuovo).
2. `def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]])` — "una lista di COPPIE (fabbrica, strategia)": ogni elemento è una tupla di 2.
3. `for factory, strategy in opponents:` — unpacking della coppia nel for: a ogni giro la tupla si APRE nelle due variabili. `creatures.append((factory.create_base(), strategy))` — coppia NUOVA col mostro appena NATO al posto della fabbrica.
4. Tutti contro tutti: `for i in range(len): for j in range(i+1, len):` — il classico "ogni coppia UNA volta sola": j parte da i+1, mai incontri doppi né contro se stessi. 2 lottatori → 1 scontro; 3 → 3 scontri.
5. `a, strat_a = creatures[i]` / `b, strat_b = creatures[j]` — unpacking della coppia.
6. IL CUORE: `try: strat_a.act(a); strat_b.act(b)` / `except StrategyError as e: print("Battle error, aborting tournament...") + return` — l'errore di validità è un FLUSSO previsto: catturato per NOME (solo la nostra eccezione), stampato chiaro, e `return` chiude SOLO battle() (il main continua: torneo 2 gira anche dopo l'errore del torneo 1). Nessun traceback.
7. I 3 tornei: 0 = Flameling+Normal vs Sproutling+Defensive (tutto valido) · 1 = Flameling+Aggressive → is_valid chiede "sei TransformCapability?" → no → StrategyError catturata (errore VOLUTO dal subject, senza crash) · 2 = 3 lottatori, e nello scontro con Shiftling si vede il ciclo di ex1 dentro la strategia (transform → boosted → revert).
**Punto da evaluation:** il torneo conosce solo `act()` — non sa quale piano sta eseguendo. La decisione "come combattere" sta nella classe della strategia (polimorfismo, stessa lezione del router di p05). Doppio controllo: `is_valid` verifica PRIMA, `act` riverifica DENTRO.

**Come testare:** `cd python/p07 && python3 tournament.py`

**Teoria:**
- **`isinstance(creature, TransformCapability)`** = il modo di chiedere "questa creatura HA la capacità?" — l'ereditarietà multipla lo rende possibile (lo Shiftling È un TransformCapability)
- **Strategy vs if a catena:** senza il pattern servirebbe `if tipo == trasformista: ... elif guaritore: ...` DENTRO il torneo. Col pattern, ogni piano sta nella SUA classe e il torneo non cambia mai — aggiungi una strategia nuova senza toccare il torneo (stessa lezione della factory)
- **StrategyError** è un'eccezione NOSTRA (come GardenError in p02 ex3) — `class StrategyError(Exception)`
- **`pass` vs `...` (domanda classica):** `...` = segnaposto per il CORPO DI UNA FUNZIONE vuota (i buchi astratti: "il corpo lo scrive la figlia"). `pass` = "non fare niente, vai avanti": serve per le CLASSI (o i blocchi) che devono esistere ma non aggiungono nulla. `class StrategyError(Exception): pass` si legge "crea una classe che eredita tutto da Exception e non aggiunge niente — mi serve solo il NOME". Python non ha le graffette del C: un blocco vuoto è errore di sintassi, quindi serve la parola `pass`. Convenzione: `...` per i metodi astratti, `pass` per le classi vuote.
- **is_valid e act — la coppia domanda/azione:** `is_valid(creature) -> bool` = LA DOMANDA ("puoi usare questa strategia?" — Aggressive chiede `isinstance(creature, TransformCapability)`, cioè guarda la FAMIGLIA/genitori, non il nome). `act(creature) -> None` = L'AZIONE: esegue il piano coi print (None = si vede a schermo, niente da restituire) e RIVERIFICA all'inizio (`if not self.is_valid: raise StrategyError`) — il doppio controllo: act non si fida di chi la chiama, si protegge da sola (filosofia delle guardie di p04/p05). Il torneo chiama SOLO act (dentro il try); is_valid è un affare interno della strategia.

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

**CHI È COSA — la distinzione che chiarisce tutto (demo 10/11):** `sys`, `os`, `site` NON sono classi — sono MODULI (cassette, come `elements` di p06): `type(sys)` → `<class 'module'>`. `sys.prefix`, `sys.base_prefix`, `sys.executable` NON sono metodi — sono VARIABILI DI TESTO dentro la cassetta (`type(sys.prefix)` → `<class 'str'>`): si leggono col punto "DENTRO" e senza parentesi = valore conservato, non azione. `site.getsitepackages()` invece È una funzione (parentesi!) che ritorna una LISTA di percorsi — fuori dal venv ne ha 2, dentro ne ha 1 (quella del venv); il `[0]` = "prendi il PRIMO elemento" (indicizzazione p03). I valori veri:
- FUORI: prefix = base_prefix = `/opt/homebrew/.../3.14` → uguali → in_venv False; executable = `.../bin/python3.14`
- DENTRO: prefix = `.../matrix_env`, base_prefix = `/opt/homebrew/.../3.14` (INCHIODATO alla casa di nascita, non cambia MAI) → diversi → in_venv True; executable = `.../matrix_env/bin/python`
- Analogia C: sys = libreria con variabili globali: prefix/executable = `char*` globali; getsitepackages() = funzione che ritorna un array di stringhe; [0] = primo elemento dell'array.

**Codice:** in `python/p08/ex0/construct.py`

## ex1 — loading — dipendenze e package manager

**Cosa fa in concreto:** controlla se le 4 librerie di analisi dati sono installate; se mancano, stampa le istruzioni per installarle (pip e Poetry); se ci sono, genera 1000 dati casuali con numpy, ne calcola le statistiche e disegna un grafico con matplotlib salvato su file.

**★ PRIME VOLTE qui:** `importlib.metadata.version()`, `requirements.txt`, `pyproject.toml`

**Cosa chiede:** un tool di analisi dati che usa pandas/numpy/matplotlib, con gestione GRACEFUL delle dipendenze mancanti (le controlla una a una e dà le istruzioni), e i file di dipendenze per DUE mondi: `requirements.txt` (pip) e `pyproject.toml` (Poetry).

**Il concetto in una riga:** i pacchetti esterni vanno DICHIARATI in un file, così chiunque ricrea l'ambiente con un comando. Due scuole: pip legge `requirements.txt` (lista semplice: `pandas
numpy
...`), Poetry legge `pyproject.toml` (file più ricco, con metadati del progetto). Il programma usa `importlib.metadata.version("pandas")` per chiedere "è installato? che versione?" senza importarlo davvero.

**Esecuzione:** main → per ognuna delle 4 librerie: `check_dependency()` → installata? "[OK] pandas (2.1.0)..." → mancante? "[MISSING] pandas" → se manca qualcosa: istruzioni pip e poetry e stop → se tutto ok: `numpy.random.randint` genera i 1000 dati (il subject vuole NUMPY come fonte dei dati, non liste) → media/deviazione → PANDAS: `pd.DataFrame(data, columns=["value"])` costruisce la tabella e `table.describe()` stampa il riassunto statistico (count/mean/std/min/max/quartili — aggiunto all'audit del 11/11: il subject dice "Uses pandas for data manipulation" e prima pandas era solo controllato, mai usato) → matplotlib disegna l'istogramma → `matrix_analysis.png`.

**Come testare:** `cd python/p08/ex1 && python3 loading.py` (senza dipendenze: messaggi) → dentro un venv: `pip install -r requirements.txt && python3 loading.py` (analisi completa).

**Teoria:** il subject tollera errori flake8/mypy sugli import qui ("Exceptionally, flake8 and mypy errors are allowed for this exercise, only for import errors"). **I due file delle dipendenze (11/11):** `requirements.txt` = la LISTA DELLA SPESA di pip — una riga per pacchetto, file piatto, `pip install -r requirements.txt` la esegue. `pyproject.toml` = il file di POETRY, il gestore COMPLETO: `[tool.poetry]` coi metadati del progetto (nome, versione, autore), `[tool.poetry.dependencies]` con le dipendenze + la versione di Python (`^3.10` = "3.10 o più"), `[build-system]` col motore di costruzione; in più Poetry genera il file di LOCK con le versioni esatte bloccate (riproducibilità) e ha i suoi comandi (`poetry install`, `poetry run`). Risposta da evaluation in una riga: pip è solo l'INSTALLATORE (compra i mattoni dalla lista); Poetry è il GESTORE DEL PROGETTO (sa chi è il progetto, cosa serve, in che versioni esatte, e come eseguirlo). Il subject chiede entrambi per dimostrare che si conoscono i due mondi. L'import di numpy/matplotlib avviene DOPO il check, dentro main — così senza dipendenze non esplode all'import.

**L'import RITARDATO — il meccanismo esatto (domanda 10/11):** `import numpy` NON è dentro un if — è protetto dal `return` che sta PRIMA. `if missing:` = "la lista missing ha qualcosa dentro?" → SÌ: corpo dell'if → istruzioni → `return` → main FINISCE lì, le righe sotto (compreso l'import) non vengono MAI eseguite. NO (lista vuota): corpo saltato → l'esecuzione PROSEGUE e arriva all'import → lo esegue (sicuro: il registro ha già confermato). Prova nei run veri: senza dipendenze "Analyzing Matrix data..." non compare mai. Perché non in cima al file: un import in cima si esegue SUBITO allo start dello script, prima di qualunque check → esplosione alla prima riga. Due passi: (1) si chiede al REGISTRO (importlib.metadata — non tocca i pacchetti, non esplode mai); (2) si importa solo se il registro ha risposto bene. Analogia C: guard clause — `if (!library_present()) { ...; return; } load_library();`. `as np` = alias (come `healing_potion as heal` di p06): "chiamala np d'ora in poi".

**check_dependency smontata (demo 10/11):**
- `importlib.metadata.version("numpy")` = "dentro importlib, nella sotto-cassetta metadata, chiedi la versione installata" → `"2.5.4"` (stringa). NON importa il pacchetto: legge la SCHEDA di registrazione lasciata in site-packages (i file METADATA) — consultare il registro non può rompere niente.
- Pacchetto sconosciuto → la funzione LANCIA `PackageNotFoundError` (classe della libreria standard): "No package metadata was found for..." — catturato per NOME dal try/except (solo questo errore, come in p07).
- `return f"[OK] {name} ({version})"` — return fa DUE cose: CONSEGNA il valore E CHIUDE la funzione. L'espressione della chiamata viene SOSTITUITA dal valore: `line = check_dependency("pandas")` → `line = "[OK] pandas (3.1.1)"`. Come in C: `char *s = check_dependency("pandas");` — la chiamata lascia il posto al puntatore ritornato. Un return per ramo → la funzione dà SEMPRE una stringa (contratto `-> str`).

**numpy (★ PRIMA VOLTA, demo 10/11):** "NUMerical PYthon" — libreria esterna (pip) che porta gli ARRAY NUMERICI veri. Un numpy array È un array del C sotto il cofano (blocco contiguo, numeri tutti dello stesso tipo, come `int data[1000];`) — ecco perché è veloce; la lista Python è una catena di scatole generiche. `np.random.randint(1, 100, size=5)` = "dentro np, nella sotto-cassetta random: dammi 5 interi casuali da 1 INCLUSO a 100 ESCLUSO" → `[18 17 78 6 57]` (tipo `numpy.ndarray`, si stampa senza virgole). In C: srand + ciclo di rand. `data.mean()` = media (somma/numero — la demo l'ha verificata a mano: 176/5 = 35.2 ✓); `data.std()` = deviazione standard (quanto i valori si sparpagliano attorno alla media). L'array è un OGGETTO INTELLIGENTE coi suoi metodi (come p05-p07).

**Il `:.2f` (★ PRIMA VOLTA):** dentro la f-string, ciò che sta DOPO i due punti è l'istruzione di formattazione: `.2` = 2 decimali, `f` = float. `f'{x:.2f}'` → "27.52" invece di "27.520174418051933" (arrotonda). Analogia C: `printf("%.2f", x)` — identico.

**matplotlib (★ PRIMA VOLTA, demo 10/11):** la libreria del disegno. Ordine nel codice: (1) `matplotlib.use("Agg")` PRIMA di importare pyplot — il backend che disegna SU FILE (PNG) invece che su schermo: fondamentale sulle macchine senza display, che non possono aprire finestre; (2) `plt.hist(data, bins=30)` — l'ISTOGRAMMA: divide l'intervallo 1-99 in 30 contenitori uguali (bins), conta quanti numeri cascano in ognuno, disegna una barra per contenitore; (3) `plt.title(...)` — il titolo; (4) `plt.savefig("matrix_analysis.png")` — IL MOMENTO DELLA VERITÀ: hist/title hanno solo PREPARATO in memoria, savefig scrive il file su disco (la demo: il PNG appare davvero, 12 KB). Niente `plt.show()`: il file È l'output — all'evaluation si fa `ls` e si mostra il PNG appena nato.

**Codice:** in `python/p08/ex1/` (loading.py + requirements.txt + pyproject.toml)

## ex2 — oracle — configurazione con .env

**Cosa fa in concreto:** legge la configurazione da variabili d'ambiente (caricate dal file .env) e si comporta in modo diverso tra development (stampa tutto) e production (nasconde la chiave segreta e pretende i dati obbligatori); senza configurazione stampa le istruzioni.

**★ PRIME VOLTE qui:** `python-dotenv` (`load_dotenv()`), `os.getenv()`, file `.env`

**Cosa chiede:** un programma che legge la configurazione da VARIABILI D'AMBIENTE (caricate da un file `.env` con la libreria python-dotenv), con comportamento diverso in development vs production, errori chiari se manca la config, e `.env` nel .gitignore (i segreti NON vanno MAI committati).

**Il concetto in una riga:** i segreti (API key, URL database) non si scrivono nel codice. Stanno in un file `.env` (locale, gitignored) e python-dotenv li carica nelle variabili d'ambiente quando il programma parte. Analogia: il codice è la ricetta pubblica, il .env è il cassetto delle spezie segrete che solo il cuoco ha.

**Esecuzione:** main → `load_dotenv()` (legge `.env` se esiste e mette le righe `CHIAVE=valore` nelle variabili d'ambiente) → `os.getenv("MATRIX_MODE")` ecc. per ognuna → se MATRIX_MODE manca: avviso "copy .env.example to .env" e stop → se "development": stampa tutto (la API key può anche mancare) → se "production": nasconde la API key con `'*' * len(api_key)` e PRETENDE DATABASE_URL e ZION_ENDPOINT (avvisi se mancano) → mode sconosciuto: errore.

**Come testare:** `cd python/p08/ex2 && python3 oracle.py` (senza .env: warning) → `cp .env.example .env && python3 oracle.py` (legge) → modifica MATRIX_MODE=production e rilancia. Nel venv: `pip install -r requirements.txt` (c'è anche il requirements.txt con python-dotenv, aggiunto l'11/11 — l'evaluator se lo aspetta).

**Teoria:** il file `.env.example` è la MASCHERA: mostra quali chiavi servono, senza valori segreti — quello SÌ va committato (e infatti sta nel repo). Il `.env` vero è nel .gitignore ("Never commit real secrets to version control! You must be able to explain why" — perché chiunque clona il repo si prenderebbe le chiavi vere). Le variabili d'ambiente vincono sul file: `load_dotenv()` NON sovrascrive le variabili già presenti nell'ambiente, quindi l'override della riga di comando batte il .env (VERIFICATO il 10/11: .env dice development, env dice production → vince production).

**FIX del 10/11 (regola vitale):** prima il file crashava con ModuleNotFoundError se python-dotenv NON era installato (import in cima al file). Ora l'import è dentro try/except ImportError con una versione di riserva di load_dotenv che stampa un avviso — senza la libreria: warning + solo variabili d'ambiente, MAI crash. Stessa filosofia dell'ex1 (gestire le dipendenze mancanti con grazia).

**FIX dell'11/11 (mypy alla scuola):** con python-dotenv INSTALLATO (lo scenario della scuola: mypy dentro il venv con le dipendenze), mypy vede DUE definizioni di load_dotenv — quella vera e la nostra riserva — e protesta con [misc] "All conditional function variants must have identical signatures". Soluzione: la riserva è `def load_dotenv() -> None:` (il programma la chiama sempre senza argomenti, quindi non serve che accetti niente) con `# type: ignore[misc, unused-ignore]` sulla riga del def (il commento DEVE stare sulla riga del def: messo sulla riga dopo NON funziona — testato). mypy pulito in entrambi gli scenari (con e senza dotenv), flake8 pulito, runtime invariato. LEZIONE per l'audit: testare mypy anche DENTRO un venv con le librerie installate, non solo nel venv dei soli tool.

**Chi è cosa (il chiarimento dell'11/11):** `os` = modulo DI SERIE di Python (viene già con Python); `dotenv` = modulo ESTERNO installato con pip (NON fa parte di os!); `load_dotenv` = FUNZIONE del modulo dotenv, non un metodo (metodo = attrezzo di una classe). Il legame vero: load_dotenv legge il file .env e SCRIVE in `os.environ` (il taccuino delle variabili d'ambiente); noi poi leggiamo con `os.getenv()`. Dotenv USA os, non è DENTRO os — come un fattorino esterno che riempie il frigo. Verifica dal vivo: `type(os)` e `type(dotenv)` → entrambi module; `load_dotenv.__module__` → 'dotenv.main'.

**Cos'è `# type: ignore` (per l'evaluation):** è un commento che legge SOLO mypy — Python e flake8 lo ignorano. Significa "mypy, su questa riga stai zitto: è voluto". Analogia: un post-it per il correttore di bozze, la stampante non lo vede. `# type: ignore[CODICE]` zittisce solo quel reclamo specifico (es. [misc] = le due firme diverse di load_dotenv: a runtime ne esiste UNA sola, l'altro ramo non gira mai); `# type: ignore` nudo zittisce qualunque reclamo sulla riga. In loading.py i 3 import differiti (pandas, matplotlib, pyplot) hanno l'ignore nudo perché la scuola ha versioni vecchie SENZA type hints ([import-untyped]) — il reclamo cambia a seconda della macchina, l'ignore nudo copre tutti i casi. In p06 c'era già il cugino: `# type: ignore[attr-defined]` sulla bomba.

**UPGRADE del 12/11 — mypy --strict pulito in OGNI scenario:** con `--strict`, mypy pretende che ogni ignore comment SIA usato (warn-unused-ignores): con le librerie nuove (stubs presenti) i nostri ignore erano "inutilizzati" → errore. Soluzione nei codici: `# type: ignore[import, unused-ignore]` — `import` copre TUTTI i reclami di import (prefisso: import-untyped, import-not-found); `unused-ignore` dice a mypy "se non c'è niente da zittire, non lamentarti del commento". Così il commento vale in ogni macchina. Stessa cosa per `[misc, unused-ignore]` sul def di riserva. VERIFICATO: --strict pulito con deps e senza deps, flake8 pulito (isolated e nudo), runtime invariato. Il subject chiede solo `mypy` nudo (già pulito), ma ora reggiamo anche il --strict se lo staff lo lancia.

**I dettagli di production:** la API_KEY non si stampa MAI in chiaro: `'*' * len(api_key)` (la stringa moltiplicata = ripetuta N volte — il trucco per mascherare). Production è SEVERO: DATABASE_URL e ZION_ENDPOINT vuoti → "MISSING - production needs a database!", API_KEY assente → WARNING. Development tollera i default.

**Codice:** in `python/p08/ex2/` (oracle.py + .env.example + .gitignore)

---

# p09 — Cosmic Data (Pydantic: validazione dei dati)

**★ PRIME VOLTE qui:** `pydantic` (libreria esterna): `BaseModel`, `Field`, `Enum`, `@model_validator`

**Il contesto (l'analogia):** i dati arrivano dall'esterno — API, file, sensori — e NON ci si può fidare: tipo sbagliato, fuori scala, mancanti. Pydantic è il GUARDIANO alla porta della discoteca: tu scrivi il REGOLAMENTO (tipi + vincoli) e quando qualcuno prova a entrare (crei l'oggetto) il guardiano controlla TUTTO. Regola rispettata → entra. Violata → `ValidationError` con il messaggio preciso. È il guardiano dell'ex4 di p01, ma pronto e con regole in una riga. Perché serve: se i dati invalidi entrano, poi esplode tutto in punti lontani — meglio fermarli SUBITO alla porta.

**Il concetto in una riga:** `class MioModello(BaseModel)` con campi tipati e vincolati (`crew_size: int = Field(ge=1, le=20)` = "intero tra 1 e 20") → alla creazione dell'oggetto Pydantic controlla tutto e converte i tipi da solo.

**Prerequisito (il subject lo impone):** Pydantic 2.x installato via pip in un venv. Comandi esatti nella Sceneggiatura p09 (in fondo agli appunti).

**Le 3 tappe:** ex0 = guardiano base (vincoli sui singoli campi) → ex1 = regole DI BUSINESS (più campi insieme, `@model_validator`) → ex2 = modelli ANNIDATI (un modello dentro un altro).

## ex0 — space_station — il primo modello

**Cosa fa in concreto:** definisce una "scheda stazione spaziale" con vincoli su ogni campo (es. equipaggio da 1 a 20) e la testa due volte: dati validi → crea e stampa la scheda; crew_size=25 → mostra il messaggio d'errore.

**L'ALBERO GENEALOGICO (chi è figlio di chi):**

```
BaseModel        <- la mamma, viene da pydantic: sa già validare,
   |                convertire e raccogliere gli errori. NON la tocchiamo.
   v
SpaceStation     <- la nostra classe: eredita TUTTO il meccanismo.
                    Noi scriviamo solo la DESCRIZIONE dei campi.
```

**La MAPPA DEI PROCESSI (chi chiama chi):**

```
python3 ex0/space_station.py
   |
   v
main()
   |
   |-- SpaceStation(dati VALIDI) ----> il guardiano controlla i 7 campi
   |        |                          -> tutto ok -> nasce l'oggetto
   |        v
   |-- print dei campi (ID, Name, Crew, Power, Oxygen, Status)
   |
   |-- SpaceStation(crew_size=25) ---> il guardiano controlla...
   |        |                          crew_size <= 20? NO
   |        |                          -> lancia ValidationError
   |        v
   |-- except ValidationError as e --> catturiamo l'errore (niente crash)
   |        v
   `-- print del messaggio del primo errore
       ("Input should be less than or equal to 20")
```

**I campi, uno per uno (righe 8-15 del file):**

| Campo | Tipo | Vincolo | Si legge |
|---|---|---|---|
| `station_id` | str | 3-10 caratteri | "la targa, lunga da 3 a 10" |
| `name` | str | 1-50 caratteri | "il nome, da 1 a 50" |
| `crew_size` | int | 1-20 | "equipaggio da 1 a 20 persone" |
| `power_level` | float | 0.0-100.0 | "potenza in percentuale" |
| `oxygen_level` | float | 0.0-100.0 | "ossigeno in percentuale" |
| `last_maintenance` | datetime | — | "data e ora dell'ultima manutenzione" |
| `is_operational` | bool | default `True` | "se non lo dici, è operativa" |
| `notes` | Optional[str] | default `None`, max 200 | "appunti opzionali" |

**Come si legge una riga:** `crew_size: int = Field(ge=1, le=20)` si legge: "il campo crew_size è un intero, con vincolo: maggiore-uguale a 1, minore-uguale a 20". `ge` = Greater or Equal, `le` = Less or Equal. Senza `Field(...)` il campo avrebbe solo il tipo, nessun vincolo.

**La traccia con i valori veri (esecuzione del main):**

| Passo | Cosa succede |
|---|---|
| 1 | `SpaceStation(station_id="ISS001", name="International Space Station", crew_size=6, power_level=85.5, oxygen_level=92.3, last_maintenance=datetime(2024,6,1,10,0,0))` → il guardiano controlla i 7 campi: ISS001 è lungo 6 (ok 3-10), il nome 28 (ok 1-50), crew 6 (ok 1-20), power 85.5 e oxygen 92.3 (ok 0-100), la data è un datetime → TUTTO OK, nasce l'oggetto `station` |
| 2 | print: ID: ISS001 / Name / Crew: 6 people / Power: 85.5% / Oxygen: 92.3% / Status: Operational (is_operational non specificato → default True) |
| 3 | `SpaceStation(station_id="ISS002", name="Broken Station", crew_size=25, ...)` → il guardiano arriva a crew_size: 25 > 20 → si FERMA e lancia `ValidationError` |
| 4 | `except ValidationError as e:` lo cattura → `e.errors()` = la lista di TUTTI gli errori (qui 1) → `[0]` = il primo → `["msg"]` = il testo del messaggio → print: "Input should be less than or equal to 20" |

**Teoria:**
- **`Field(...)`** = "etichetta di regole" attaccata a un campo: `min_length`/`max_length` per le stringhe, `ge`/`le` per i numeri, `default` per il valore di partenza. Analogia C: sono le condizioni che in C scriveresti a mano in una `validate_station()` piena di if — Pydantic le genera dalla descrizione dei campi.
- **`Optional[str] = Field(default=None, max_length=200)`** = il campo può mancare: se manca, vale None.
- **`is_operational: bool = True`** = valore di default: chi crea la stazione può non specificarlo.
- **La CONVERSIONE automatica** (domanda del subject: "How does Pydantic's automatic type conversion work?"): arriva `crew_size="6"` (stringa)? La converte in int 6. Arriva `last_maintenance="2024-06-01T10:00:00"` (stringa)? La converte in datetime. Stringa NON convertibile ("sei") → errore. Verificato dal vivo.
- **Perché NON si vede mai un traceback:** l'errore di validazione non è un crash — è un'eccezione normale che il `try/except` cattura e trasforma in un print pulito.

**Risposte pronte per l'evaluation:**
- Le 2 domande SCRITTE nel subject (pag. 9, "Think About" — garantite):
  - "How does Pydantic's automatic type conversion work?" → durante la validazione, un valore compatibile ma di tipo diverso (stringa "6" per un int, stringa di data per un datetime) viene CONVERTITO da solo nel tipo giusto; non convertibile → ValidationError.
  - "What happens when you pass a string timestamp to a datetime field?" → convertita in datetime automaticamente; formato illeggibile → errore.
- Le domande classiche (con risposta):
  - "Cos'è BaseModel?" → la classe madre il cui __init__ fa la validazione; la ereditiamo con class SpaceStation(BaseModel).
  - "Chi valida, Field o BaseModel?" → BaseModel valida; Field scrive SOLO i vincoli.
  - "Cosa significano ge/le, min_length/max_length?" → vincoli: ≥ e ≤ per i numeri; lunghezza min/max per le stringhe.
  - "E se passo crew_size=25?" → ValidationError alla creazione: "Input should be less than or equal to 20".
  - "Perché is_operational = True?" → default: se non lo passi, vale True.
  - "Cos'è Optional[str]?" → stringa OPPURE None; con default=None il campo può mancare.
  - "Se salto last_maintenance?" → senza default è obbligatorio → "Field required".
  - "Perché il try/except?" → mostrare l'errore senza traceback: catturo ValidationError e stampo solo il messaggio.
  - "Cos'è e.errors()?" → METODO (si chiama) che restituisce la LISTA degli errori; ogni errore è un dizionario; [0]["msg"] = testo del primo.
- Le 3 modifiche dal vivo possibili: crew_size=0 → "greater than or equal to 1"; last_maintenance come stringa → conversione automatica; togliere un campo obbligatorio → "Field required".

**Output atteso (dal subject):** titolo "Space Station Data Validation" + scheda della stazione valida + "Expected validation error:" + `Input should be less than or equal to 20`.

**Codice:** `python/p09/ex0/space_station.py`

## ex1 — alien_contact — validazione custom

**Cosa fa in concreto:** definisce un modello di "rapporto di contatto alieno" con regole di BUSINESS che i Field da soli non sanno esprimere (es. i contatti telepatici richiedono almeno 3 testimoni) e lo testa con un rapporto valido e uno che viola le regole.

**★ PRIME VOLTE qui:** `Enum` (ContactType), `@model_validator(mode="after")`

**L'ALBERO GENEALOGICO:**

```
Enum               BaseModel
  |                    |
  v                    v
ContactType        AlienContact
(radio, visual,       |
physical,             |-- @model_validator(mode="after")
telepathic)           v
                   check_business_rules(self) -> "AlienContact"
```

**Cosa chiede:** contatto con campi vincolati (contact_id 5-15, location 3-100, signal 0.0-10.0, duration 1-1440, witnesses 1-100, message opzionale max 500, is_verified default False, contact_type = Enum) + 4 REGOLE DI BUSINESS controllate da `@model_validator(mode="after")`: ID inizia con "AC"; PHYSICAL → deve essere verificato; TELEPATHIC → ≥3 testimoni; segnale >7.0 → deve avere un messaggio.

**Esecuzione:** main → contatto valido → Pydantic valida i campi → POI gira il validator (mode="after" = DOPO i campi): 4 domande, UNA per if, coi criteri annidati (stile del 12/11: "un if = una domanda, mai due criteri mischiati con and") → tutte ok → `return self` (OBBLIGATORIO: il validator restituisce il modello) → contatto invalido (telepathic con 1 testimone) → il validator fa `raise ValueError("Telepathic contact requires at least 3 witnesses")` → il ValidationError viene catturato.

**LEZIONE FLAKE8 dell'11/11:** il repo ha un .flake8 PADRE (quello di AMAZEING) con un `ignore` custom che NON contiene W503/W504 — quindi con `flake8` NUDO (senza --isolated) gli operatori a inizio riga vengono segnalati: il validator di ex1 aveva `and` a inizio riga → W503. Fix: variabile di servizio così l'if sta su una riga sola. IMPORTANTE: l'evaluator clona il repo CON quel .flake8 → i controlli vanno fatti ANCHE con `flake8` nudo dalla repo, non solo con --isolated (verificato: p00-p09 tutti puliti in ENTRAMBI i modi).

**Dettaglio importante (fix dell'11/11):** Pydantic v2 antepone "Value error, " ai messaggi dei NOSTRI validator. Il print usa `.removeprefix("Value error, ")` per mostrare il messaggio PULITO come nell'esempio del subject.

**Teoria:** `Enum` = tipo con un numero CHIUSO di valori — arriva "laser"? Errore automatico. `@model_validator(mode="after")` = metodo che gira DOPO la validazione dei campi e vede il modello INTERO (per regole che coinvolgono più campi insieme; il vecchio `@validator` è deprecato e vietato dal subject). Dentro il validator i campi sono già pronti in `self`.

**Output atteso:** titolo "Alien Contact Log Validation" + rapporto valido + "Expected validation error:" + `Telepathic contact requires at least 3 witnesses`.

**Risposte pronte per l'evaluation:**
- Le domande SCRITTE nel subject (garantite):
  - L'Advanced Tip: "@model_validator valida il modello INTERO dopo che tutti i campi sono stati validati. Ricordati di restituire self alla fine del validator." → return self è OBBLIGATORIO: pydantic prende ciò che il validator restituisce come modello finale; senza, l'oggetto si perde.
  - "Why mode='after'?" → DOPO la validazione dei campi: dentro il validator i campi sono già validati e leggibili con self.
- Le domande classiche (con risposta):
  - "Perché @model_validator e non il vecchio @validator?" → @validator è deprecato in v2, il subject lo vieta esplicitamente.
  - "Cos'è Enum / perché ContactType invece di str?" → lista CHIUSA di valori; qualunque cosa fuori (es. "laser") → ValidationError automatico, niente if a mano.
  - "Cosa succede se contact_type='laser'?" → errore: "Input should be 'radio', 'visual', 'physical' or 'telepathic'".
  - "Cosa fa .startswith('AC')?" → risponde vero/falso a "la stringa inizia con 'AC'?"; col not: la regola scatta quando NON inizia.
  - "Cosa fa l'and nelle condizioni?" → unisce due domande: basta una falsa e si salta il raise.
  - "Perché `is None` e non `== None`?" → `is` confronta l'identità: "è proprio il nulla" (stesso pattern di p08 con api_key).
  - "Perché raise ValueError dentro il validator?" → è la convenzione: pydantic lo cattura e lo avvolge nel suo ValidationError.
  - "Perché removeprefix('Value error, ')?" → pydantic v2 antepone quel prefisso ai NOSTRI errori; lo togliamo per mostrare il messaggio pulito come nell'esempio del subject.
  - "Perché -> 'AlienContact' tra virgolette?" → dentro il corpo della classe il nome non è ancora nato; la stringa è una promessa (forward reference) letta da mypy.
  - "Differenza tra Field e model_validator?" → Field controlla un campo ALLA VOLTA; il validator controlla regole che coinvolgono PIÙ campi insieme.
- Le modifiche dal vivo possibili: witness_count a 5 → passa; physical senza is_verified → regola 2; segnale 8.5 senza messaggio → regola 4; contact_type='laser' → errore dell'Enum.

**Codice:** `python/p09/ex1/alien_contact.py`

## ex2 — space_crew — modelli ANNIDATI

**Cosa fa in concreto:** definisce due modelli collegati (membro dell'equipaggio e missione che contiene una LISTA di membri) e valida regole che coinvolgono TUTTO l'equipaggio: serve un comandante, le missioni lunghe vogliono metà equipaggio esperto. Testa una missione valida e una senza comandante.

**L'ALBERO GENEALOGICO:**

```
Enum               BaseModel
  |                    |
  v                    +--------------------+
Rank              CrewMember          SpaceMission
(cadet, officer,     |                    |
 lieutenant,         | (lista di)         |-- crew: List[CrewMember]
 captain,            |  ^                 |-- @model_validator(mode="after")
 commander)          +--+                 v
                    (dentro)          check_mission_rules(self)
```

**Il concetto in una riga:** un modello può stare DENTRO un altro (anche in liste): `crew: List[CrewMember]` = "la missione contiene una lista di oggetti CrewMember, e Pydantic valida OGNI membro con le sue regole PRIMA di validare la missione". Matrioska: missione → equipaggio → membri.

**Cosa chiede:** CrewMember (member_id 3-10, name 2-50, rank Enum, age 18-80, specialization 3-30, years_experience 0-50, is_active default True) + SpaceMission (mission_id 5-15, mission_name 3-100, destination 3-50, launch_date datetime, duration_days 1-3650, crew 1-12 membri, mission_status default "planned", budget 1.0-10000.0) + 4 REGOLE di sicurezza nel validator: ID inizia con "M"; almeno un Commander o Captain; missioni >365 giorni → 50% di esperti (≥5 anni); tutti attivi.

**Esecuzione:** main → 3 `CrewMember(...)` (validati uno a uno) → `SpaceMission(..., crew=crew, ...)` → Pydantic valida i campi della missione E in cascata i 3 membri → il validator: `leaders = []` + `for m in self.crew:` + `if m.rank in (Rank.CAPTAIN, Rank.COMMANDER): leaders.append(m)` (for esplicito, scelto al posto della comprehension per leggibilità — 12/11) → lista vuota → raise → missione invalida di prova (solo ufficiali) → "Mission must have at least one Commander or Captain". La regola del 50% ha DUE if annidati (durata >365 → esperti < metà), la regola "tutti attivi" usa `all(...)` (una riga, e la funzione resta sotto le 25 righe). Il main stampa anche i dettagli dei membri col `for` (formato dell'esempio del subject: "- Sarah Connor (commander) - Mission Command").

**Teoria:** il Rank è un Enum come il ContactType di ex1. `Field(min_length=1, max_length=12)` sulla lista = 1-12 membri. La regola del 50%: `len(experienced) < len(self.crew) / 2` (2 esperti su 3 membri → 2 < 1.5 è falso → ok). Anche qui il print dell'errore usa `removeprefix("Value error, ")` (vedi ex1).

**Output atteso:** titolo "Space Mission Crew Validation" + missione valida con ID, destinazione, durata, budget, crew size e membri elencati + "Expected validation error:" + `Mission must have at least one Commander or Captain`.

**Risposte pronte per l'evaluation:**
- Le domande SCRITTE nel subject (Think About, garantite):
  - "How does Pydantic handle validation of nested models?" → in CASCATA: prima costruisce e valida ogni CrewMember della lista (le sue regole), poi valida la missione. Matrioska.
  - "What happens when a CrewMember fails validation within a SpaceMission?" → l'INTERA missione viene rifiutata: basta un membro invalido, con ValidationError che indica il colpevole.
- Le classiche: concetto nuovo = modelli ANNIDATI (`crew: List[CrewMember]`); dizionario al posto di CrewMember → Pydantic lo CONVERTE costruendo il CrewMember dalle chiavi; for esplicito al posto della comprehension (più leggibile, stessa cosa compressa — p03); regola 50%: >365 giorni e `len(esperti) < len(crew)/2` → raise; `all(...)` di p05; `in (a, b)` = appartenenza a tupla; removeprefix come ex1.
- Live coding (lo staff cambia VALORI/VINCOLI, non la struttura): missione invalida → valida: bad_crew rank OFFICER→CAPTAIN; missione valida → invalida: un membro is_active=False (regola 4); crew_size=25 valido: ex0 Field le=20→le=25; telepatici con 5 testimoni: ex1 <3→<5; aggiungere un campo: riga nel modello + print; notes obbligatorio: togliere default=None.

**Codice:** `python/p09/ex2/space_crew.py`

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
| `import`/`from`, package, `__init__.py`, import relativi (il puntino `.`), alias `as`, dipendenze circolari | p06 |
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

---

# SCENEGGIATURA TEST VIVI PER L'EVALUATION (p05-p07) — tutti verificati il 9/11

Regola d'oro: all'evaluation NON raccontare — MOSTRARE. Ogni caso qui sotto è stato eseguito davvero: copia il comando e mostra l'output.

## p05 — i rami edge (tutti TypeError PULITI, mai traceback)

Run normali: `cd python/p05/ex0 && python3 data_processor.py` · idem ex1 `data_stream.py` · ex2 `data_pipeline.py`

```bash
cd python/p05/ex0 && python3 -c "
from data_processor import LogProcessor, TextProcessor, NumericProcessor
LogProcessor().ingest({'log_level': 'ERROR'})   # chiave mancante (il caso del bugfix!) -> TypeError pulito
LogProcessor().ingest({'log_level': 'ERROR', 'log_message': 42})  # valore non-stringa -> TypeError
TextProcessor().ingest(42)                      # -> TypeError
NumericProcessor().ingest(None)                 # -> TypeError
NumericProcessor().ingest([])                   # lista vuota -> OK, nessun errore (all() su vuoto = True)
NumericProcessor().ingest([1, 'x'])             # lista mista -> TypeError
"
```

ex1 — elemento che NESSUN processore sa gestire: `python3 -c "from data_stream import DataStream, NumericProcessor; ds=DataStream(); ds.register_processor(NumericProcessor()); ds.process_stream([1,'ciao',b'bytes'])"` → stampa "Can't process element" per 'ciao' e b'bytes', nessun crash.
ex2 — pipeline su magazzino vuoto (la guardia): `python3 -c "from data_pipeline import DataStream, CsvPlugin; DataStream().output_pipeline(5, CsvPlugin())"` → nessun crash.

## p06 — gli 11 puliti + le 2 bombe + retro/vetrina

```bash
cd python/p06
for f in ft_alembic_0 ft_alembic_1 ft_alembic_2 ft_alembic_3 ft_alembic_5 ft_distillation_0 ft_distillation_1 ft_transmutation_0 ft_transmutation_1 ft_transmutation_2 ft_kaboom_0; do python3 $f.py >/dev/null && echo "$f OK"; done
python3 ft_alembic_4.py    # BOMBA voluta: AttributeError "no attribute 'create_earth'" (+ exit 1)
python3 ft_kaboom_1.py     # BOMBA voluta: ImportError "partially initialized module ... circular import"
python3 -c "import alchemy; print(alchemy.elements.create_earth())"   # il retro FUNZIONA: Earth element created
python3 -c "from alchemy import create_earth"                          # vetrina bloccata all'import: ImportError
```

## p07 — factory astratta, vetrina, stato, isinstance

```bash
cd python/p07 && python3 battle.py && python3 capacitor.py    # i 2 run normali
python3 -c "from ex0.factories import CreatureFactory; CreatureFactory()"
    # -> TypeError: Can't instantiate abstract class CreatureFactory (senza create_base/create_evolved)
python3 -c "from ex0 import Flameling"     # -> ImportError: la vetrina espone solo le factory
python3 -c "
from ex1.factories import TransformCreatureFactory
s = TransformCreatureFactory().create_base()
print(s.attack()); s.transform(); print(s.attack()); s.revert(); print(s.attack())
"   # -> normally / boosted strike! / normally  (lo STATO in azione)
python3 -c "
from ex0.creatures import Creature, Flameling
from ex1.creatures import Sproutling
from ex1.capabilities import HealCapability
print(isinstance(Sproutling(), Creature))      # True
print(isinstance(Sproutling(), HealCapability))# True
print(isinstance(Flameling(), HealCapability)) # False — la capacità si decide alla nascita della classe
"
```

## p08 — i 9 scenari (tutti verificati il 10/11)

```bash
cd python/p08/ex0 && python3 construct.py              # 1) FUORI dal venv: "still plugged in" + istruzioni
cd python/p08/ex1 && python3 loading.py                # 2) SENZA dipendenze: [MISSING] x4 + istruzioni pip/Poetry
cd python/p08/ex2 && python3 oracle.py                 # 3) SENZA .env: warning "copy .env.example to .env" (mai crash!)
# 4) oracle.py SENZA python-dotenv installato: warning + solo variabili d'ambiente (il fix del 10/11)
# 5) override: MATRIX_MODE=production python3 oracle.py  → vince la variabile d'ambiente sul .env
cd python/p08/ex2 && cp .env.example .env && python3 oracle.py   # 6) CON .env: sviluppo, valori caricati
# 7) .env con MATRIX_MODE=production e valori vuoti → "MISSING - production needs..." + WARNING API_KEY
# DENTRO il venv (i comandi del subject):
python3 -m venv matrix_env && source matrix_env/bin/activate
python3 ../ex0/construct.py                            # 8) DENTRO: "Welcome to the construct" + site-packages
pip install -r ../ex1/requirements.txt && cd ../ex1 && python3 loading.py   # 9) run completo → matrix_analysis.png
deactivate
```

**La domanda dei 100 per p08:** "PERCHÉ esistono i venv?" → isolamento: ogni progetto ha la SUA copia di pip e le SUE versioni delle librerie in una cartella separata; installare nel globale sporca il sistema e crea conflitti di versioni tra progetti. "PERCHÉ il .env non si committa?" → contiene SEGRETI (API key, password): chi clona il repo li leggerebbe; il repo porta solo .env.example (la maschera).

## p09 — la sequenza dell'evaluation (STAFF, venerdì 13/11)

```bash
cd python/p09
python3 -m venv .venv            # PREPARAZIONE (una volta sola): crea il venv
source .venv/bin/activate        # attiva (ogni terminale nuovo; il prompt mostra (.venv))
pip install "pydantic>=2"        # installa Pydantic 2.x (obbligo del subject, via pip)
python3 ex0/space_station.py     # RUN PURO: scheda valida + errore di validazione
python3 ex1/alien_contact.py     # RUN PURO: rapporto valido + regola telepatici violata
python3 ex2/space_crew.py        # RUN PURO: missione valida + missione senza comandante
deactivate                       # PULIZIA a fine eval
```

Verifiche extra davanti allo staff: `pip show pydantic | head -2` (versione 2.x); `python3 -c "import pydantic"` senza venv → errore atteso (serve il venv, è nel subject). La cartella `.venv/` è gitignorata: NON va committata. In consegna: SOLO i 3 file .py.

**La domanda dei 100 per p09:** "PERCHÉ serve Pydantic?" → perché i dati che arrivano dall'esterno non sono affidabili: Pydantic li valida ALLA PORTA (tipo + vincoli + regole di business) e rifiuta con un errore preciso PRIMA che entrino nel programma — senza che scriviamo un if a mano.
