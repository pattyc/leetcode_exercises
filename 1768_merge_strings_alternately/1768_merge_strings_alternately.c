#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char * mergeAlternately1(char * word1, char * word2){
    int num_chars = strlen(word1) + strlen(word2);
    char *ans = malloc(num_chars+1);
    int i = 0;
    int x = 0;

    while (word1[i] && word2[i]) {
        ans[x++] = word1[i];
        ans[x++] = word2[i];
        i++;
    }
    if (word1[i]) {
        strcpy(ans + x, word1 + i);
    } else {
        strcpy(ans + x, word2 + i);
    }

    return ans;
}



int main(void) {
    char *a = "abc";
    char *b = "xyz";
    char *c = malloc(100);
    c = mergeAlternately(a,b);
    printf("%s\n", c);
}