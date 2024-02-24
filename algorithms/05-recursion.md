# Recursion

TLDR: function that calls it self until it reaches a **"base case"**. At this point it solves the problem and return

Base knowledge for trees and some types of graph


## Example

```js
function foo(n: number): number {
    // Base case
    if (n === 1) {
        return 1
    }

    // we shall recuse
    return n + foo(n - 1)
}
```

Function concepts
- Return Address (rA)
- Return Value (rV)
- Arguments (A)

first, go down until reach base case
|-|rA|rV|A|
|-|-|-|-|
|foo5|caller|5+?|5|
|foo4|foo5|4+?|4|
|foo3|foo4|3+?|3|
|foo2|foo3|2+?|2|
|foo1|foo2|1|1|

NOTE: left columns is the call stack

second moment, return up the values
|-|rA|rV|A|
|-|-|-|-|
|foo5|caller|5+10|5|
|foo4|foo5|4+6|4|
|foo3|foo4|3+3|3|
|foo2|foo3|2+1|2|
|foo1|foo2|1|1|

return 15


## Path Finding Example

```js
//MazeSolver
maze = [
    "####E#",
    "#    #",
    "#S####",
]
// where 'S' in start and 'E' is end, '#' is a all
```

Base case:
1. its a wall
2. off the map
3. its the end
4. if we have seen it

[MazeSolver](./kata-machine/src/day1/MazeSolver.ts)


## When to use it?

**When its not able to be done via a for loop**


## What is the O(n)?

At most we will check every single 4 times -> O(4*n) -> O(n)
