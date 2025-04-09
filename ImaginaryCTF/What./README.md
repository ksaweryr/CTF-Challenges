# What.
**Category:** Misc
**Difficulty:** Medium

## Description
Yeah, exactly. What?

## Solution
Notice that least significant bit layers of each of the colours (R, G, B) do not look like they belong to the image. Overlay them to reveal a QR code. As the image is probably too noisy to be scanned by a QR code reader, replace every block that shouldn't be black to consist only of white pixels. Now scan the QR code to get the flag.