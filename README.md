# Casino-roulette

A casino roulette simulation built in Python using a **Circular Singly Linked List** as its core data structure.

---

## Data Structure — `SinglyLinkedList`

A circular singly linked list where each node represents a bet placed by the player. The `tail.next` always points back to `head`, keeping the list circular at all times.

Each node (`Node`) stores:
- `number` — the roulette number the bet is placed on (0–36)
- `color` — the color of the slot (`"red"`, `"black"`, or `"green"`)
- `next` — pointer to the next node in the list

### Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `insertar_apuesta(number, color, monto)` | Adds a new bet at the end of the list | O(1) |
| `eliminar_apuesta(number)` | Removes the first bet matching the given number | O(n) |
| `ver_apuestas()` | Returns a list of all active bets | O(n) |
| `verificar_ganador(result_number, result_color)` | Traverses all bets and returns the ones that match the roulette result, by number, color, or both | O(n) |

### Method Details

**`insertar_apuesta`** — Creates a new node and appends it to the end. Since there is always a direct reference to `tail`, no traversal is needed — constant time.

**`eliminar_apuesta`** — Traverses the list from `head` looking for the node whose number matches. In the worst case the number is at the end or does not exist, visiting all `n` nodes. Once found, it rewires the pointers to preserve circularity.

**`ver_apuestas`** — Traverses all `n` nodes once and builds a list with each bet's data. Uses `size` to know when to stop and avoid an infinite loop caused by the circular structure.

**`verificar_ganador`** — Traverses all nodes and compares each bet against the roulette result. Each node requires two O(1) comparisons (number and color), making the total O(n).

---

## Data Structure — `CircularLinkedList`

A circular linked list that physically represents the roulette wheel with 37 slots (0–36). It keeps a `current` pointer that simulates the current position on the wheel.

Each node (`Node`) stores:
- `number` — the slot number (0–36)
- `next` — pointer to the next slot on the wheel

### Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `insertar_numero(number)` | Adds a slot to the wheel | O(1) |
| `construir_ruleta()` | Inserts all 37 slots (0–36) and sets `current` to `head` | O(n) |
| `girar()` | Advances `current` a random number of steps and returns the landing number | O(n) |
| `__repr__()` | Returns a string with all numbers in the wheel, used for debugging | O(n) |

### Method Details

**`insertar_numero`** — Appends a new slot at the end of the wheel. Direct reference to `tall` makes this constant time.

**`construir_ruleta`** — Calls `insertar_numero` 37 times, one per slot. Each call is O(1), making the full build O(n) in general terms.

**`girar`** — Generates a random number of steps between 1 and `size × 3`, then advances `current` that many nodes through the circular list. Worst case is O(n) steps. Returns the number where `current` lands, simulating the wheel spin.

**`__repr__`** — Traverses all nodes to build a debug string showing the full wheel.

---

## How to Play

**Starting balance:** Q1,000.00

### Placing a Bet

Each bet requires three fields:
- **Number** — the roulette number you predict (0–36)
- **Color** — the color you predict (`red`, `black`, or `green`)
- **Amount** — how much you wager (deducted from your balance immediately)

You can place **multiple bets** before spinning.

### Payouts

When you spin, the result is compared against every active bet:

| Outcome | Payout |
|---|---|
| Correct **color** | 2× the amount |
| Correct **number** | 35× the amount |
| Correct **both** | 35× + 2× the amount |
| Neither | Bet is lost |

**Example:** you bet Q100 on number 7, color red. If the wheel lands on 7 red → you win Q100×35 + Q100×2 = **Q3,700**.

### Number Colors

- **0** → always green
- **Red:** 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
- **Black:** all remaining numbers

After each spin all bets are cleared. Use **Restart** to reset the balance back to Q1,000.
