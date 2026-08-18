#include <stdio.h>

void swap_kaputt(int a, int b) {
    int t = a; a = b; b = t;   /* passiert hier draußen irgendwas? */
}

void swap(int *a, int *b) {
    /* TODO: über Dereferenzierung wirklich tauschen */
    int t = *a;
    *a = *b;
    *b = t;


}

int main(void) {
    int x = 3, y = 7;
    printf("x=%d (@%p)  y=%d (@%p)\n", x, (void*)&x, y, (void*)&y);
    swap_kaputt(x, y);
    printf("nach swap_kaputt: x=%d y=%d\n", x, y);
    swap(&x, &y);
    printf("nach swap:        x=%d y=%d\n", x, y);
    printf("%zu\n", sizeof(int));
    printf("%zu\n", sizeof(char));
    printf("%zu\n", sizeof(int*));
    printf("%zu\n", sizeof(char*));
    return 0;
}