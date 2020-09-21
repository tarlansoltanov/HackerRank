// Name : "Hello World!" in C
// Link : https://www.hackerrank.com/challenges/hello-world-c/problem?h_r=profile
// Difficulty : Easy
// Programming language : C

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    printf("Hello, World!\n%s",s);
    return 0;
}