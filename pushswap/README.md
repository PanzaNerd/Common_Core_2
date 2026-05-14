*This project has been created as part of the 42 curriculum by mpanzani.*

## Description

push_swap is an algorithmic project that sorts a stack of integers using two stacks (a and b) and a limited set of operations, with the minimum number of moves possible. The goal is to sort stack a in ascending order with the smallest number at the top.

The algorithm used is the **Turk Algorithm**, which works as follows:
1. Push all elements to stack b except 3, using a sliding window (chunk-based push)
2. Sort the remaining 3 elements in stack a
3. Reinsert elements from b to a one by one, always choosing the cheapest insertion
4. Rotate stack a until the minimum is at the top

## Instructions

**Compilation:**
```bash
make
```

**Execution:**
```bash
./push_swap 3 1 2 5 4
```

**Error handling:**
```bash
./push_swap 1 1       # Error: duplicates
./push_swap abc       # Error: invalid argument
./push_swap           # No output: no arguments
./push_swap 1 2 3     # No output: already sorted
```

## Technical Choices

**Data structure:** doubly-linked list where each node contains:
- `value` — the actual integer
- `index` — the rank (0 = smallest, n-1 = largest)
- `pos` — current physical position in the stack
- `target_pos` — target position in stack a (used by Turk)
- `cost_a` — rotations needed in a (positive = ra, negative = rra)
- `cost_b` — rotations needed in b (positive = rb, negative = rrb)

**Algorithm — Turk with chunk-based push:**

The push phase uses a sliding window to pre-organize stack b. Elements are pushed to b in groups, so that higher-index elements stay near the top of b and lower-index elements sink to the bottom. This reduces the cost of reinsertion.

For each element in b, the algorithm computes:
- Its target position in a (the immediate successor — smallest element in a with a greater index)
- The total cost to bring it to the top of b and its target to the top of a
- If cost_a and cost_b have the same sign, `rr`/`rrr` is used to rotate both stacks simultaneously, saving moves

The element with the lowest total cost is always inserted first.

**Benchmark results:**
```
100 numbers → average ~580 operations  (limit: 700)
500 numbers → average ~5200 operations (limit: 5500)
```

## Resources

- YT Oceano
- YT Get The Cookie
- 42 Peer to peer evaluations
- 42 push_swap subject
- AI used: Claude and Gemini — for algorithm explanation, debugging, code structure, and norminette fixes
