#include <stdio.h>

int main(int argc, char* argv[]){
    char var1[16];
    char secret[16];
    printf("input? ");
    gets(var1);
    printf("%s",var1);
    if (!strcmp(secret, "gachonuniversity")){
        printf("\n\nsuccess!\n");
    } else {
        printf("\n\nfail..\n");
    }
    return 0;
}

