# Maps

Neither `{}` or `new Map()` are actually maps!

## Terminology

load factor: The amount of data points vs the amount of storage available
key: a value that is hashable and is used to look up data, the has has to consistent
value: a value that is associated with a key
collision: when 2 keys maps to the same cell


Usually maps are implemented ArrayLists where each item (bucket) will be a key-value pair and there is correlation with load factor and collisions


## LRU

Caching mechanism that evicts the least recently used item

It will use a DoubleLinkedList under the hook together with a HashMap where the value of the map is the Node in the list!!! this is genious * - * -> we don't need to transverse the list, no O(n) retrieval

[LRU](./kata-machine/src/day1/LRU.ts)
