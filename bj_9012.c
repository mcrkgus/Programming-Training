#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SIZE 55


typedef struct Stack
{
	int top;
	char arr[SIZE];
} Stack;

void init(Stack *s)
{
	s->top = -1;
}

int is_empty(Stack *s)
{
	if(s->top == -1)
		return 1;
	return 0;
} 

int is_full(Stack *s)
{
	if(s->top == (SIZE-1))
		return 1;
	return 0;
}

void push(Stack *s, char data)
{
	if(is_full(s)==1){
		printf("STACK IS FULL\n");
		return;
	}
	
	s->arr[++(s->top)] = data;
	
}

char pop(Stack *s)
{
	if(is_empty(s)==1){
		printf("STACK IS EMPTY\n");
		return ' ';
	}
	return s->arr[(s->top)--];
}

int VPS(char *str)
{
	//char str[50];
	Stack s;
	init(&s);
	int len = strlen(str);
	int i;
	char open_ch, ch;
	
	for(i=0; i<len; i++){
		ch = str[i];
		switch(ch) {
			case '(' :
				push(&s, ch);
				break;
			case ')' :				
				if(is_empty(&s)==1)
					return 0;
			
				open_ch = pop(&s);
				if(open_ch=='(')
					break;
				break;
		}
	}

	if(is_empty(&s) == 0)
		return 0;
	return 1;
}

int main(void)
{
	int T;
    
	scanf("%d", &T);
	int temp=0;
	char *str = (char*)malloc(sizeof(char) * SIZE);
	
	for(int i=0; i<T; i++) {
		scanf("%s", str);

		temp = VPS(str);
		if(temp == 0)
			printf("NO\n");
		else if(temp ==1)
			printf("YES\n");
	}

	return 0;

}
