#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int   *data;
    size_t len;
    size_t cap;
} Vec;

Vec vec_new(void) {
    Vec v = { malloc(4 * sizeof(int)), 0, 4 };
    if (v.data == NULL) {
        if (v.data == NULL) { perror("malloc"); exit(1); }
    }
    return v;
}

void vec_push(Vec *v, int wert) {
    if (v->len == v->cap) {
        size_t neue_cap = v->cap * 2;
        int *neu = realloc(v->data, neue_cap * sizeof(int));
        if (neu == NULL) { perror("realloc"); exit(1); }
        v->data = neu;
        v->cap  = neue_cap;
    }
    v->data[v->len] = wert;
    v->len++;
}

int main(void) {
    Vec v = vec_new();
    for (int i = 0; i < 100; i++) {
        vec_push(&v, i * i);
        printf("len=%2zu cap=%2zu data=%p\n", v.len, v.cap, (void*)v.data);
    }
    free(v.data);
    return 0;
}