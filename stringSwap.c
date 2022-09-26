#include<stdio.h>

void Swap(char **p1, char **p2) {

	char *temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main(void) {
	char *pa1 = "dog";
	char *pa2 = "cat";

	printf("*pa1, *pa2 : %s %s\n", pa1, pa2);


	printf("\n--SWAP--\n");

	Swap(&pa1, &pa2);
	printf("*pa1, *pa2 : %s %s\n", pa1, pa2);

	return 0;
}
