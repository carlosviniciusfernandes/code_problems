# Arrays vs Linked List

- Arrays are fast due index access, but need memory allocated upfront and there is a usability burden when adding/removing
- Linked Lists are memory optimized and easier to use, but has a cost on performance compared to arrays (always linear search for linked lists - O(n))


## Can we do betters? Yes

**ArrayList**: This combines the idea of an array with the ability to grow it. Adheres to the list interface

The problem with arrayList is removing/adding from the front (Queue operations)

<!-- TODO -->
[ArrayList](./kata-machine/src/day1/ArrayList.ts)


# ArrayBuffer

Sort of a ArrayList, but with indexed tail and head. It makes all operations constant (push, pop, enqueue, deque)

- `tail % len` allows going around the buffer (like a **RingBuffer**)
- when we need to resize (tail == head), it has to be rewrite in proper order in a new buffer with more capacity
- we can have algorithms that flushes the buffer from time to time for certain use cases


# Bonus

What is the bracket [] in JavaScript? [progressive test](./kata-machine/src/array-test.ts) -> It is a ArrayList, get, push and pop are super fast O(1), while shift and unshift are not performant kind of O(n)
