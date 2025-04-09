# (il)logical chaos
**Category:** Misc
**Difficulty:** Medium

## Description
Can you light the light at the end of the ~~tunnel~~ recursive data structure?

## Solution
Table node included in the sqlite3 file contains a graph in which nodes are various logic gates and edges are connections between said gates. One can use a recursive algorithm, similar to DFS, to traverse the graph and build up expressions to be solved by a SAT solver (eg. z3).