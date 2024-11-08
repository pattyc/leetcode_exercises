#include <stdio.h>

char* gcdOfStrings(char* str1, char* str2) {
    int best_len = 0;
    int best_i = 0;
    for (int i = 0; i < sizeof(str1) - 1; i++) {
        printf("i: %d\n", i);
        int cur_len = 0;
        for (int j = 0; j < sizeof(str2) - 1; j++) {
            printf("j: %d\n", j);
            if (str1[j] == str2[j]) {
                cur_len++;
            } else {
                break;
            }
        }
        if (cur_len > best_len) {
            best_len = cur_len;
            best_i = i;
        }
    }
    printf("%d, %d", best_i, best_len);
    fflush(stdout);
    char *out = strcpy(str1+best_i;
    out[best_len] = '\0';
    return out;
}

int main(void) {
    char *a = "ABCABC";
    char *b = "ABC";
    char *c;
    c = gcdOfStrings(a, b);
    printf("out: %s\n", c);
}
