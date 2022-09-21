#include <stdio.h>
#include <string.h>
#include "cs50.h"

int main(void)
{
    float T1 = -196, T2 = 36.1, p1 = 0.352, p2 = 1.454;

    float B = (p2 - p1) / (T2 - T1);
    float A = p2 - B * T2;

    printf("P = %f + (%f)T\n", A, B);

}