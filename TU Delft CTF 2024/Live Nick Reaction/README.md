# Live Nick Reaction
**Category:** Stego
**Difficulty:** Hard

## Description
Behold, the obligatory stego challenge™! Nick was kinda confused when he saw it...

## Solution
- 1st layer: binwalk to get a zip
- 2nd layer: find password in the spectrogram of the song
- 3rd layer: find password in the least significant bits of the image
- 4th layer: decode the audio as SSTV transmission in Martin 1 mode