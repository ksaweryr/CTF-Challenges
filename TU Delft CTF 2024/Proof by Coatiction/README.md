# Proof by Coatiction
**Category:** Crypto
**Difficulty:** Easy

## Description
Sure, I can sign stuff for you. However, I won't sign a statement with which I don't agree!

## Solution
Recover RSA modulus from 2 coprime messages using GCD. Sign the forbidden message multiplied by $2^e$ and multiply the result by $2^{-1} \mod n$ to get a valid signature.