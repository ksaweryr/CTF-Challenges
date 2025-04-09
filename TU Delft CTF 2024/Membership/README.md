# Membership
**Category:** Forensics
**Difficulty:** Hard

## Description
The membership problem, but it's not maths nor theoretical computer science. If only there was a tool that does everything theoretically allowed by the format specifications...

## Solution
Look in the gzip RFC. See that each file constists of one or more "members" and each member can have a (unique) file name. See that `gzip` will try to extract everything to one file regardless. Write your own gzip extractor that extracts to multiple files.