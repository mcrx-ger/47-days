#include <stdio.h>

int main(void) {
    int x = 42;
    char c = 'b';
    double v = 550.3;
    printf("Wert %d liegt bei %p, belegt %zu Bytes\n", x, (void*)&x, sizeof(x));
    printf("Char %c liegt bei %p, belegt %zu Bytes\n", c, (void*)&c, sizeof(c));
    printf("Double %f liegt bei %p, belegt %zu Bytes\n", v, (void*)&v, sizeof(v));
    return 0;
}
