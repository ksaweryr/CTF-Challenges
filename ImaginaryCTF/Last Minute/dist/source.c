#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void) {
    srand(time(NULL));

    const char* flag = "ictf{cr34t1ng_ch4ll3ng3s_l4st_m1nut3_wh4t_c0uld_g0_wr0ng}";

    for(int i = 0; i < strlen(flag); i++) {
        printf("%02x", flag[i] ^ (rand() % 256));
    }

    printf("\n");

    return 0;
}
