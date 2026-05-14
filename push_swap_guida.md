# PUSH SWAP — Guida Visiva Completa
## per l'evaluation di mpanzani @ 42 Firenze

---

## 1. STRUTTURA DATI — t_node

Ogni nodo della linked list ha questi campi:

```
┌─────────────┐
│ value       │  → il numero vero (es. 3, -5, 42)
│ index       │  → il rango (0=minimo, 1=secondo, ...)
│ pos         │  → posizione fisica nello stack (0=top)
│ target_pos  │  → posizione target in A (usato dal Turk)
│ cost_a      │  → mosse per ruotare A (+ = ra, - = rra)
│ cost_b      │  → mosse per ruotare B (+ = rb, - = rrb)
│ *next       │  → puntatore al nodo successivo
└─────────────┘
```

Lo stack è una linked list — catena di nodi:

```
top → [3|i2|→] → [1|i0|→] → [4|i3|→] → NULL
```

---

## 2. LE 11 OPERAZIONI

```
sa  → scambia i primi 2 di A
sb  → scambia i primi 2 di B
ss  → sa + sb insieme

pa  → prende top di B → mette in cima ad A
pb  → prende top di A → mette in cima a B

ra  → top di A va in fondo
rb  → top di B va in fondo
rr  → ra + rb insieme

rra → fondo di A va in cima
rrb → fondo di B va in cima
rrr → rra + rrb insieme
```

### Esempi visivi:

**sa:**
```
PRIMA:  A: [3][1][7]
DOPO:   A: [1][3][7]
```

**pb:**
```
PRIMA:  A: [3][1][7]    B: [5]
DOPO:   A: [1][7]       B: [3][5]
```

**ra:**
```
PRIMA:  A: [3][1][7]
DOPO:   A: [1][7][3]
```

**rra:**
```
PRIMA:  A: [3][1][7]
DOPO:   A: [7][3][1]
```

---

## 3. FLUSSO COMPLETO — esempio con `./push_swap 3 1 4 2 5`

---

### STEP 1 — parse_args

Legge gli argomenti dal fondo verso l'inizio e costruisce A:

```
av[5]="5" → push_node
av[4]="2" → push_node
av[3]="4" → push_node
av[2]="1" → push_node
av[1]="3" → push_node
```

Controlli: 

1. is_valid	//controlla che ogni carattere sia tra '0' e '9'
			//se trova qualcosa di strano ritorna 1
 
2. ft_atol	//converte stringa in long
			//rileva overflow: se i numero >INT_MAX o <INT_MIN 
			//ritorna INT_MAX+1 e INT_MIN-1 (valori volutamente fuori range) che parse_args rileva

3. has_dup //scorre tutta la lista, se trova un nodo con lo stesso valore ritorna 1

Se fallisce → stampa "Error\n" su stderr → exit(1)

```
A: [3][1][4][2][5]     B: []
    ↑top
```

---

### STEP 2 — assign_index

Per ogni nodo, conta quanti hanno valore minore → quello è il suo indice:

//ca = cursore nodo
//c2a = cursore nodo da confrontare
//idx = contatore dell'indice

```
3: quanti < 3? → 1,2 → index=2
1: quanti < 1? → nessuno → index=0
4: quanti < 4? → 1,2,3 → index=3
2: quanti < 2? → solo 1 → index=1
5: quanti < 5? → 1,2,3,4 → index=4
```

```
A: [3,i2][1,i0][4,i3][2,i1][5,i4]     B: []
```

---

### STEP 3 — push_to_b (con gruppi)

size=5, groups=5, group_size=size/groups=1, pushed=0

Finestra corrente = pushed + group_size

//group_size definisce la dimensione iniziale della finestra
//La finestra è pushed + group_size e rappresenta il limite massimo di indice accettabile per essere spinto in B
//Ad ogni push pushed aumenta di 1, quindi la finestra si allarga di 1 — questo garantisce che prima o poi tutti gli elementi vengano catturati e spinti in B, finché A non ha solo 3 elementi

(*a)->index <= pushed + group_size	//spingi in B solo gli elementi il cui indice è dentro la finestra corrente
									//La finestra si allarga di 1 ad ogni push perché pushed cresce
									
(*b)->index < pushed - group_size / 2	//Dopo aver spinto un elemento, controlli se il suo indice è nella metà bassa della finestra corrente

NB: push_to_b fa solo un pre-lavoro grezzo — cerca di mettere gli elementi grossomodo nell'ordine giusto in B così che il Turk debba fare meno rotazioni in media.

```
A: [3,i2][1,i0][4,i3][2,i1][5,i4]     B: []
i2 <= 0+1=1? NO → ra

A: [1,i0][4,i3][2,i1][5,i4][3,i2]     B: []
i0 <= 0+1=1? SÌ → pb, pushed=1

A: [4,i3][2,i1][5,i4][3,i2]           B: [1,i0]
  i0=0 < 1-0=1? SÌ → rb (su 1 elem non fa niente)
i3 <= 1+1=2? NO → ra

A: [2,i1][5,i4][3,i2][4,i3]           B: [1,i0]
i1 <= 1+1=2? SÌ → pb, pushed=2

A: [5,i4][3,i2][4,i3]                 B: [2,i1][1,i0]
  i1=1 < 2-0=2? SÌ → rb
  
A: [5,i4][3,i2][4,i3]                 B: [1,i0][2,i1]
stack_size(A)=3 → STOP
```

---

### STEP 4 — sort_three

```
A: [5,i4][3,i2][4,i3]
top=i4, mid=i2, bot=i3
caso: top>mid && mid<bot && top>bot → ra

ra:
A: [3,i2][4,i3][5,i4]     ✓ ordinato per indice
```

---

### STEP 5 — reinserisci da B (while *b)

Per ogni iterazione:
1. set_positions → aggiorna la posizione fisica di tutti i nodi (0,1,2,3...)

2. set_target → per ogni elemento di B, si trova il successore immediato in A, il piu piccolo tr tutti i successori. L'elemento di B andra' inserito davanti a lui in A. Se non esiste successore -> find_min -> top A

3. set_costs → calcola cost_a e cost_b, ossia quante mosse servono per portare ogni elemento in posizione

4. cheapest → sceglie l'elemento con costo minore
5. do_move → esegue le rotazioni + pa

---

**ITERAZIONE 1:**

```
A: [3,i2,p0][4,i3,p1][5,i4,p2]     B: [1,i0,p0][2,i1,p1]	//setta p=0,1,2,3...
```

set_target:
```
B i0: cerca in A il min tra idx > 0 → idx=2 in pos=0 → target_pos=0
B i1: cerca in A il min tra idx > 1 → idx=2 in pos=0 → target_pos=0
```

set_costs (size_a=3, size_b=2):
```
B i0: pos=0 <= 2/2=1 → cost_b=0 | target_pos=0 <= 3/2=1 → cost_a=0
B i1: pos=1 <= 2/2=1 → cost_b=1 | target_pos=0 <= 3/2=1 → cost_a=0
```

total_cost:
```
B i0: ca=0,cb=0 → max(0,0) = 0  ← MINORE
B i1: ca=0,cb=1 → max(0,1) = 1
```

cheapest → sceglie i0 (costo=0)

do_move:
```
ca=0, cb=0 → nessuna rotazione necessaria
pa:
A: [1,i0][3,i2][4,i3][5,i4]     B: [2,i1]
```

---

**ITERAZIONE 2:**

```
A: [1,i0,p0][3,i2,p1][4,i3,p2][5,i4,p3]     B: [2,i1,p0]
```

set_target:
```
B i1: cerca in A il min tra idx > 1 → idx=2 in pos=1 → target_pos=1
```

set_costs (size_a=4, size_b=1):
```
B i1: pos=0 <= 1/2=0 → cost_b=0 | target_pos=1 <= 4/2=2 → cost_a=1
```

do_move:
```
ca=1, cb=0
do_rotations: ca>0 ma cb=0 → nessun rr
do_single_rotations: ca=1>0 → ra, ca=0
pa:

ra: A: [3,i2][4,i3][5,i4][1,i0]     B: [2,i1]
pa: A: [2,i1][3,i2][4,i3][5,i4][1,i0]     B: []
```

B vuoto → STOP

---

### STEP 6 — rotate_min

```
A: [2,i1][3,i2][4,i3][5,i4][1,i0]

Cerco i0: pos=0(i1) pos=1(i2) pos=2(i3) pos=3(i4) pos=4(i0) → trovato a pos=4
size=5, pos=4 > 5/2=2 → rra
pos = 5-4 = 1 → 1 rra

rra:
A: [1,i0][2,i1][3,i2][4,i3][5,i4]     B: []   ✓
```

---

## 4. MOSSE TOTALI NELL'ESEMPIO

```
ra          (push_to_b)
pb          (push_to_b)
ra          (push_to_b)
pb          (push_to_b)
rb          (push_to_b)
ra          (sort_three)
pa          (inserimento i0)
ra          (do_move per i1)
pa          (inserimento i1)
rra         (rotate_min)
```

---

## 5. SCHEMA FUNZIONI — chi chiama chi

```
main
├── parse_args
│   ├── is_valid
│   ├── ft_atol
│   └── has_dup
├── stack_size
├── is_sorted
├── assign_index
└── turk_sort
    ├── push_to_b
    │   ├── stack_size
    │   ├── pb
    │   └── ra / rb
    ├── sort_three
    │   └── sa / ra / rra
    ├── set_positions
    ├── set_target
    │   └── find_min
    ├── set_costs
    ├── cheapest
    │   └── total_cost
    │       └── abs_val
    ├── do_move
    │   ├── do_rotations
    │   │   └── rr / rrr
    │   ├── do_single_rotations
    │   │   └── ra / rra / rb / rrb
    │   └── pa
    └── rotate_min
        └── ra / rra
```

---

## 6. REGOLE DEI SEGNI IN set_costs / do_move

```
cost > 0  →  ruota in avanti  (ra o rb)
cost < 0  →  ruota al contrario  (rra o rrb)
cost = 0  →  già in cima, nessuna mossa

cost_a e cost_b stesso segno  →  usa rr/rrr (risparmia mosse)
cost_a e cost_b segni diversi →  mosse separate, costi si sommano
```

---

## 7. DOMANDE TIPO EVALUATION

**Q: Perché usi una linked list e non un array?**
A: Push/pop sono O(1) senza riallocare memoria.

**Q: Cosa fa assign_index?**
A: Assegna a ogni nodo il suo rango — quanti nodi hanno valore minore. Il minimo ha sempre index=0.

**Q: Perché sort_two usa gli indici e non i valori?**
A: Con INT_MAX e INT_MIN il confronto tra valori può andare in overflow. Gli indici sono sempre numeri piccoli e sicuri.

**Q: Cosa fa set_target?**
A: Per ogni elemento di B trova il successore immediato in A — il più piccolo tra tutti i nodi di A con indice maggiore. L'elemento andrà inserito davanti a lui.

**Q: Perché alcuni costi sono negativi?**
A: Il segno indica la direzione della rotazione. Positivo = ra/rb, negativo = rra/rrb.

**Q: Quando si usa rr invece di ra+rb?**
A: Quando cost_a e cost_b hanno lo stesso segno — le rotazioni vanno nella stessa direzione e si possono fare in una mossa sola.

**Q: Cosa fa rotate_min?**
A: Alla fine, quando B è vuoto, ruota A finché il nodo con index=0 (il minimo) è in cima. Sceglie la direzione più corta tra ra e rra.

**Q: Perché static su alcune funzioni?**
A: Le funzioni static sono visibili solo nel loro file — sono funzioni di supporto interne che non devono essere chiamate dall'esterno.

**Q: Cosa fa exit(1)?**
A: Termina immediatamente il programma con codice di errore 1.

**Q: Perché ** (doppio asterisco) in molte funzioni?**
A: Serve quando la funzione deve modificare il puntatore stesso — far puntare lo stack a un nodo diverso. Con * puoi modificare il contenuto del nodo ma non dove punta il puntatore.

---

## 8. BENCHMARK

```
100 numeri → sotto 700 mosse   ✓ (media ~580)
500 numeri → sotto 5500 mosse  ✓ (media ~5200)
```

---

*push_swap completato da mpanzani @ 42 Firenze*
