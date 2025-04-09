# Automated Cracking Computer
**Category:** Reversing
**Difficulty:** Easy

## Description
I've made a DFA serving one purpose - accepting the flag - and exported its unrecognizable representation using https://courses.ewi.tudelft.nl/acc/AutomatedCheckingComputer/. Can you guess what the flag is? (note: wrap the flag in TUDCTF{})

## Solution
Use the `Simulator.Decode` function from `Assembly-CSharp.dll` to decode the "unrecognizable" representation. Paste the result into the tool and read the flag by following the transitions leading to the accepting state.