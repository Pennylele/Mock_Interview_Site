#include <stdio.h>
int func(int a)
{
        return a*a;
}

int main(int argc, char **argv)
{
        int x;

        sscanf(argv[1], "%d", &x);
        printf("%d\n", func(x));
        return 0;
}