# Appunti Python — Progetti 42

Ogni esercizio è raccontato **nell'ordine in cui si esegue il codice**: si parte dal main (o dalla chiamata) e si segue il flusso passo per passo. Poi codice, poi teoria.

---

# p00 — Growing Code (Fondamenta Python)

## ex0 — ft_hello_garden — la prima funzione

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

**Cosa chiede:** se i giorni > 2 stampa "Water the plants!", altrimenti "Plants are fine".

**Esecuzione:** identica a ex4: input → int → confronto → un ramo solo dei due viene eseguito.

**Attenzione:** il subject scrive `Plants are fine` SENZA punto esclamativo.

## ex6 — ft_count_harvest — for e ricorsione

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

**Cosa chiede:** funzione `get_player_pos()` che chiede coordinate `x,y,z`, gestisce gli errori, ritenta finché non sono valide, e RESTITUISCE una **tupla** con le 3 coordinate. Poi: mostra la tupla e ogni coordinata separata, calcola la distanza dal centro (0,0,0), chiede un secondo punto e calcola la distanza tra i due.

**Obiettivo:** incontrare la **tupla** — la seconda collezione. È come una lista ma IMMUTABILE: "scritta nella pietra", una volta creata non si cambia. Perfetta per un punto 3D che è un insieme fisso di 3 numeri. In più: `math.sqrt()` per la radice quadrata.

**Come testare:**
```bash
cd python/p03/ex2
python3 ft_coordinate_system.py
# prova:  hello world        → Invalid syntax
#        1.0 , 2.5, 3.0      → distanza dal centro 4.0311
#        4,abc,5             → errore sul parametro 'abc'
#        4,5,6               → distanza tra i punti 4.9244
```

**Esecuzione:**
1. Main → intestazione → `get_player_pos()` → input: l'utente scrive
2. `raw.split(",")` — **split** spezza la stringa dove trova le virgole: `"1.0 , 2.5, 3.0"` → lista `["1.0 ", " 2.5", " 3.0"]`
3. `len(parts) != 3`? "hello world" non ha virgole → split dà 1 pezzo → "Invalid syntax" → `continue` = **torna in cima al while**, richiede di nuovo
4. Loop sui 3 pezzi: `float(part)` converte (float = numero con virgola; accetta anche "4"). Se un pezzo fallisce ("abc") → except stampa `Error on parameter 'abc': could not convert string to float: 'abc'` → `ok = False` → `break` esce dal loop → il `continue` del while fa ritentare tutto
5. Se tutti e 3 passano → `return (x, y, z)` — le parentesi tonde creano la **TUPLA** e la restituiscono
6. `x1, y1, z1 = get_player_pos()` — **unpacking**: la tupla si apre nelle 3 variabili (come distribuire 3 carte da un mazzo)
7. `math.sqrt(x1*x1 + y1*y1 + z1*z1)` — Pitagora in 3D: distanza dal centro. `math.sqrt()` = radice quadrata, dal modulo `math` (importato in cima). `round(d, 4)` = 4 decimali → 4.0311
8. Secondo punto → distanza tra i due: `sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)` — **`**` è l'elevamento a potenza** (2 al quadrato)

**Codice:**
```python
import math

def get_player_pos() -> tuple[float, float, float]:
	while True:
		raw = input("Enter new coordinates as floats in format 'x,y,z': ")
		parts = raw.split(",")
		if len(parts) != 3:
			print("Invalid syntax")
			continue
		values = []
		ok = True
		for part in parts:
			try:
				values.append(float(part))
			except ValueError as e:
				print(f"Error on parameter '{part}': {e}")
				ok = False
				break
		if ok:
			return (values[0], values[1], values[2])

def main() -> None:
	print("=== Game Coordinate System ===")
	print("Get a first set of coordinates")
	x1, y1, z1 = get_player_pos()
	print(f"Got a first tuple: {(x1, y1, z1)}")
	print(f"It includes: X={x1}, Y={y1}, Z={z1}")
	d = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
	print(f"Distance to center: {round(d, 4)}")

	print("Get a second set of coordinates")
	x2, y2, z2 = get_player_pos()
	d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
	print(f"Distance between the 2 sets of coordinates: {round(d, 4)}")


if __name__ == "__main__":
	main()
```

**Teoria:**
- **Tupla** = collezione come la lista MA immutabile: si crea con `(a, b, c)` invece di `[a, b, c]`, e non ha `append` — non la cambi. "Scritta nella pietra". Perché usarla: un punto 3D è un insieme fisso di 3 numeri — con la tupla nessuno può modificarlo per sbaglio
- **Chi è cosa:** `math` → modulo predefinito (importato); `math.sqrt()` → funzione predefinita del modulo math (radice quadrata); `split()` → METODO built-in delle stringhe; `float()` → CLASSE built-in (converte in numero decimale); `continue`/`break`/`while` → parole chiave; `(a, b, c)` → sintassi tupla; `x1, y1, z1 = ...` → unpacking; `**` → operatore potenza; il resto come ex0/ex1
- **`while True:` + `continue` = il pattern "ritenta finché non va"**: il loop è infinito, si esce solo col `return`. `continue` = salta il resto e torna in cima al loop
- **`float("4")`** funziona (converte "4" → 4.0): float accetta anche interi scritti come stringa. `float(" 2.5")` ignora gli spazi ai bordi — per questo "1.0 , 2.5, 3.0" funziona
- **Unpacking `x1, y1, z1 = tupla`**: Python apre la collezione e assegna un elemento a ogni variabile, in ordine. Funziona con tuple E liste
- **`a ** 2`** = a elevato a 2 (a²). In C: `pow(a, 2)` o `a * a`
- Distanza tra due punti 3D = estensione di Pitagora: radice di (Δx² + Δy² + Δz²)

---

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
