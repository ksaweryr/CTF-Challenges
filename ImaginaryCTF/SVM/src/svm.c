#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {
    PUSH,
    PUSH_IMM,
    POP,
    ADD,
    SUB,
    MUL,
    HALT
} Opcode;

typedef struct Node {
    int value;
    struct Node* next;
} Node;

typedef struct {
    int registers[9];
    Node* stack;
} State;

void push(Node** stack, int value) {
    Node* head = (Node*)malloc(sizeof(Node));
    head->value = value;
    head->next = *stack;
    *stack = head;
}

int pop(Node** stack) {
    Node* head = *stack;
    int value = head->value;
    *stack = head->next;
    free(head);
    return value;
}

void perform_operation(State* state, Opcode opcode, int argument) {
    int tmp;
    int tmp2;

    switch(opcode) {
        case PUSH:
            push(&state->stack, state->registers[argument]);
            break;
        case PUSH_IMM:
            push(&state->stack, argument);
            break;
        case POP:
            tmp = pop(&state->stack);
            state->registers[argument] = tmp;
            break;
        case ADD:
            tmp = pop(&state->stack);
            tmp2 = pop(&state->stack);
            push(&state->stack, tmp + tmp2);
            break;
        case SUB:
            tmp = pop(&state->stack);
            tmp2 = pop(&state->stack);
            push(&state->stack, tmp - tmp2);
            break;
        case MUL:
            tmp = pop(&state->stack);
            tmp2 = pop(&state->stack);
            push(&state->stack, tmp * tmp2);
            break;
    }
}

void run_program(State* state, char* program) {
    int pc = 0;

    while(1) {
        Opcode opcode = (Opcode)program[pc++];
        int argument = program[pc++];

        if(opcode == HALT) {
            break;
        }

        perform_operation(state, opcode, argument);
    }
}

static char PROGRAM[] = {
    POP, 4, POP, 3, POP, 2, POP, 1,
    PUSH, 1, PUSH, 2, PUSH, 3, PUSH, 4, PUSH_IMM, 2, MUL, 0, POP, 0, PUSH_IMM, 5, MUL, 0, PUSH, 0, SUB, 0, POP, 0, PUSH_IMM, 12, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 7, MUL, 0, PUSH, 0, ADD, 0, POP, 5,
    PUSH, 1, PUSH, 2, PUSH, 3, PUSH, 4, PUSH_IMM, 1, MUL, 0, POP, 0, PUSH_IMM, 10, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 4, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 42, MUL, 0, PUSH, 0, ADD, 0, POP, 6,
    PUSH, 1, PUSH, 2, PUSH, 3, PUSH, 4, PUSH_IMM, 3, MUL, 0, POP, 0, PUSH_IMM, 17, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 8, MUL, 0, PUSH, 0, SUB, 0, POP, 0, PUSH_IMM, 3, MUL, 0, PUSH, 0, SUB, 0, POP, 7,
    PUSH, 1, PUSH, 2, PUSH, 3, PUSH, 4, PUSH_IMM, 7, MUL, 0, POP, 0, PUSH_IMM, 21, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 1, MUL, 0, PUSH, 0, ADD, 0, POP, 0, PUSH_IMM, 15, MUL, 0, PUSH, 0, ADD, 0, POP, 8,
    PUSH, 8, PUSH, 7, PUSH, 6, PUSH, 5,
    HALT, 0
};

void process_chunk(const char* source, int* dest) {
    State state = { {}, NULL };

    for(int i = 0; i < 4; i++) {
        push(&state.stack, source[i]);
    }

    run_program(&state, PROGRAM);

    for(int i = 0; i < 4; i++) {
        dest[i] = pop(&state.stack);
    }
}

int main() {
    char flag[41];
    FILE* fptr;
    fptr = fopen("flag.txt", "r");
    fgets(flag, 41, fptr);
    fclose(fptr);

    int* dest = (int*)malloc(40 * sizeof(int));

    for(int i = 0; i < 40; i += 4) {
        process_chunk(flag + i, dest + i);
    }

    fptr = fopen("output.bin", "w");
    fwrite(dest, sizeof(int), 40, fptr);
    fclose(fptr);

    free(dest);

    return 0;
}
