# Tango
**Category:** Crypto
**Difficulty:** Medium

## Description
Let's dance!

## Solution
Perform bit-flipping to change user and command. Use the fact that crc32(x ^ y ^ z) = crc32(x) ^ crc32(y) ^ crc32(z) to forge the checksum.