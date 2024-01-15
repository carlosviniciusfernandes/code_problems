# Sort

[BubbleSort](./kata-machine/src/day1/BubbleSort.ts)
[LinkedList](./kata-machine/src/day1/SinglyLinkedList.ts)
 - "Node" based data structure, each node has a **value** and points to the **next** (like a daisy chain)
 - "HEAD" point to the first node
 - Double Linked Lists also have the **prev** node reference
 - Instead of arrays, lists uses heap allocated objects to store the nodes
 - setting **next** and **prev** are O(1) operations, hence insertion and deletion on linked lists are time constant
 - getting HEAD and TAIL are constant operations
 - getting the "n"th item is a O(N) operation (1 for loop)
 - inserting and deleting and in the middle there are two parts: the *transversal* to get "i"th item, and the constant time operation
 - There is no "index" as in arrays
 - Data structure that uses algorithm for insertion/removal
[Queue](./kata-machine/src/day1/Queue.ts)
 - FIFO Data structure on top of a Singly Linked List
 - in a way, it is a linked list with limited operation, just the O(1) constant time operations
 - operations: enqueue, dequeue and peek (check head without pop)
[Stack](./kata-machine/src/day1/Stack.ts)
 - "Opposite of a Queue", literally it looks like queue in reverse
 - push and pop from the stack are operations on the "HEAD"

Another Big O TIP: if the input halves on each step, its likely O(logN) or O(NlogN)
