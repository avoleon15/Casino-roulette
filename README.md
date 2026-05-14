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
| `insertar_apuesta(number, color)` | Adds a new bet at the end of the list | O(1) |
| `eliminar_apuesta(number)` | Removes the first bet matching the given number | O(n) |
| `ver_apuestas()` | Returns a list of all active bets | O(n) |
| `verificar_ganador(result_number, result_color)` | Traverses all bets and returns the ones that match the roulette result, by number, color, or both | O(n) |
