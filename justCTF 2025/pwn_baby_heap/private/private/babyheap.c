#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_CHUNKS 20
#define CHUNK_SIZE 0x30
char* chunks[NUM_CHUNKS] = { 0 };

int get_index(void) {
    int idx;

    printf("Index? ");

    if (scanf(" %d", &idx) != 1) {
        puts("Invalid input");
        exit(0);
    }

    if (idx < 0 || idx >= NUM_CHUNKS) {
        puts("Invalid index");
        exit(0);
    }

    return idx;
}

void create_chunk(void) {
    int idx = get_index();

    if (chunks[idx] != NULL) {
        puts("This index is already in use");
        return;
    }

    chunks[idx] = malloc(CHUNK_SIZE);

    printf("Content? ");
    printf("Content? ");
    read(0, chunks[idx], CHUNK_SIZE);
}

void read_chunk(void) {
    int idx = get_index();

    if (chunks[idx] == NULL) {
        puts("This chunk is empty");
        return;
    }

    write(1, chunks[idx], CHUNK_SIZE);
}

void update_chunk(void) {
    int idx = get_index();

    if (chunks[idx] == NULL) {
        puts("This chunk is empty");
        return;
    }

    printf("Content? ");
    read(0, chunks[idx], CHUNK_SIZE);
}

void delete_chunk(void) {
    int idx = get_index();

    if (chunks[idx] == NULL) {
        puts("This chunk is empty");
        return;
    }

    free(chunks[idx]);
}

int main(void) {
    int choice;

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    while (1) {
        printf("Menu:\n1) Create\n2) Read\n3) Update\n4) Delete\n0) Quit\n> ");

        if (scanf(" %d", &choice) != 1) {
            puts("Invalid input");
            exit(0);
        }

        if (choice == 0) {
            break;
        }

        switch (choice) {
            case 1:
                create_chunk();
                break;
            case 2:
                read_chunk();
                break;
            case 3:
                update_chunk();
                break;
            case 4:
                delete_chunk();
                break;
            default:
                puts("Invalid choice!");
                break;
        }
    }

    return 0;
}