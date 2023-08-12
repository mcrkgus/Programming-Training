#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 10001
typedef int element;
typedef struct 
{
	int top;
	element arr[MAX];
} Stack;

void init(Stack *s)
{
	s->top=-1;
}

int is_empty(Stack *s)
{
	if(s->top==-1)
		return 1;
	return 0;
}

int is_full(Stack *s)
{
	if(s->top==MAX-1)
		return 1;
	return 0;
}


void push(Stack *s, int X)
{
	if(is_full(s)) {
		printf("ERROR");
		return;
	}
	else s->arr[++(s->top)] = X;

}

element pop(Stack *s)
{
	if(is_empty(s))
		return -1;
	else
		return s->arr[(s->top)--];
}

int size(Stack *s)
{
	int cnt=0;
	for(int i=0; i<=s->top; i++)
		cnt++;
	return cnt;
}
int top(Stack *s)
{
	if(is_empty(s))
		return -1;
	return s->arr[s->top];
}


int main(void)
{
	Stack s;
	init(&s);
	int n, data;
	char pick[10];
	scanf("%d", &n);
	
	for(int i=0; i<n; i++) {
		scanf("%s", pick);
		if(strcmp(pick, "push")==0) {
			scanf("%d", &data);
			push(&s, data);
		}
		else if(strcmp(pick, "pop")==0)
			printf("%d\n", pop(&s));
		else if(strcmp(pick, "size")==0)
			printf("%d\n", size(&s));
		else if(strcmp(pick, "empty")==0)
			printf("%d\n", is_empty(&s));	
		else if(strcmp(pick, "top")==0)
			printf("%d\n", top(&s));	
	}
	return 0;
}
