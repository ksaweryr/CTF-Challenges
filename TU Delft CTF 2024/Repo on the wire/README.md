# Repo on the wire
**Category:** Forensics
**Difficulty:** Easy

## Description
One of TU Delft's hackers (codename: "Agent 0xba115") managed to infiltrate internal network of De Haagse Hogeschool and download a repository containing source code of a critical piece of their infrastracture. Unfortunately, he spilled a free coffee acquired using [REDACTED]'s employee card over his laptop and lost all his data. Luckily, we still have a dump of network communication between his machine and HHs git server. Can you help us recover the secrets hidden in that repository?

## Solution
Simple and dirty solution: extract bytes using wireshark, try decompressing and every possible offset (git smart protocol uses zlib to compress transmitted data).