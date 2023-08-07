#include<stdio.h>
#include<stdlib.h>
#define MAX 100000
int cnt = 0;
int stack[MAX];

void push(int n)
{
	stack[cnt]=n;
	cnt++;
}

void pop()
{
	cnt--;
	stack[cnt]=0;
}

int main(void)
{
	int k;
	int sum=0;
	scanf("%d", &k);
	int arr[k];

	for(int i=0; i<k; i++)
	{
		scanf("%d", &arr[i]);
		if(arr[i] != 0)
			push(arr[i]);
		if(arr[i] == 0){
			pop();
		}
		
	}

	for(int i=0; i<cnt; i++)
	{
		sum += stack[i];
	}
	printf("%d", sum);

	return 0;

}
