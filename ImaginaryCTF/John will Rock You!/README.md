# John will Rock You!
**Category:** Misc
**Difficulty:** Easy

## Description
`$2b$12$HT5Mzpoz4Qavukh8Fr621.MsJOd/o0Ra4EicvIYonQuozYhUyXnrK` (wrap the flag in `ictf`)

## Solution
Ironically I used hashcat:
`$ echo '$2b$12$HT5Mzpoz4Qavukh8Fr621.MsJOd/o0Ra4EicvIYonQuozYhUyXnrK' > hash && hashcat -a 0 -m 3200 hash /path/to/rockyou.txt`