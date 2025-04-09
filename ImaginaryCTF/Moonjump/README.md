# Moonjump
**Category:** Crypto
**Difficulty:** Hard

## Description
"That's one small step for man, one giant leap for mankind." - my Lua 5.4 script just finished running and now I can share my encrypted flag with you!

## Solution
Look into Lua source code to figure out that it uses xoshiro256** to generate random numbers. As a transition from state n to state n+1 is a linear transformation, it is possible to calculate its standard matrix. Now it's trivial to quickly calculate a transition through many states quickly by representing the state of the PRNG as a vector and left-multiplying it with the standard matrix raised to the appropriate power. Now all that's left is bruteforcing the timestamp (there are 60 possibilities). A Sage script solving the challenge is available here: [solve.sage](./src/solve.sage)