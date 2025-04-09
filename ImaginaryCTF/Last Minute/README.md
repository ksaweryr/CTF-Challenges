# Last Minute
**Category:** Misc
**Difficulty:** Easy

## Description
Oh no, we need a challenge to be released in less than an hour, so we have to create one! Luckily I have my computer running Linux with gcc 12.2... Either way, have fun with that: `941e94d287fab058fde5b60a1bd539ee4d55b70870f129ba6b2a76717658e4ceea1cc0b25d0184ff7c2c4cb48be66e28a4d5ed9609fcc4c86f`

## Solution
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int from_hex(char c) {
    if(c >= '0' && c <= '9') {
        return c - '0';
    } else {
        return c - 'a' + 10;
    }
}

int main(void) {
    const char* flag = "941e94d287fab058fde5b60a1bd539ee4d55b70870f129ba6b2a76717658e4ceea1cc0b25d0184ff7c2c4cb48be66e28a4d5ed9609fcc4c86f";

    for(int i = 0; i < 3600; i++) {
        srand(1715875200 + i);

        for(int i = 0; i < strlen(flag) / 2; i++) {
            printf("%c", (from_hex(flag[2 * i]) * 16 + from_hex(flag[2 * i + 1])) ^ (rand() % 256));
        }

        printf("\n");
    }

    return 0;
}
```