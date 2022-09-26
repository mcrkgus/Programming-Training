typedef int element;
typedef struct{
	int data[MAX_STACK_SIZE];
	int top;
} StackType;

void init_stacks(StackType *s)
{
	s->top = -1;
}

int is_empty(StackType *s)
{
	return (s->top == -1);
}


int is_full(StackType *s)
{
	return (s->top == (MAX_STACK_SIZE -1));
}


void push(StackType *s, int item)
{
	if(is_full(s)){
		printf("STACK IS FULL!!\n");
		return;
	}
}

element pop(StackType *s){
	if(is_empty(s)){
		printf("STACK IS EMPTY,,,\n");
		exit(1);
	}
	else 
		return s->data[(s->top)--];
}

int main(void)
{
	StackType s;

	init_stacks(&s);
	push(&s, 1);
	push(&s, 2);
	push(&s, 3);
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
}
