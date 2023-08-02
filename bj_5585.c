#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int pay=0, n=0, cnt=0;
	int back=0;

	scanf("%d", &pay);
	back = 1000 - pay;
		n = back /500;
		cnt += n;
		back = back - 500*n;

		n=0;
		n = back/100;
		cnt += n;
		back = back - 100*n;

		n=0;
		n = back/50;
		cnt += n;
		back = back - 50*n;

		n=0;
		n = back/10;
		cnt += n;
		back = back - 10*n;
		n=0;
		n = back/5;
		back = back - 5*n;
		cnt =  cnt + n + back;

	printf("%d\n", cnt);

	return 0;
}
