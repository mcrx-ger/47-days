#include <stdio.h>

size_t my_strlen(const char *s) {
    size_t i = 0;
    while (*(s+i) != '\0'){
        i++;
    }
    return i;
}

void reverse(char *s) {
    /* TODO: in-place, zwei Pointer von außen nach innen */
    const size_t len = my_strlen(s);
    for (size_t i = 0; i < len / 2; i++) {
        char t = *(s+i);
        *(s+i) = *(s+len-1-i);
        *(s+len-1-i) = t;
    }
}

int main(void) {
    char buf[] = "Cybersecurity";   /* wie viele Bytes belegt das? */
    printf("%zu Zeichen, %zu Bytes\n", my_strlen(buf), sizeof(buf));
    reverse(buf);
    printf("%s\n", buf);
    return 0;
}