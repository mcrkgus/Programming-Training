#include<stdio.h>

typedef struct 
{
	char left;
	char right;
} node;
node tree[27];

void preorder(char node) 
{
	if(node == '.') return;
	printf("%c", node);

	preorder(tree[node].left);
	preorder(tree[node].right);
}

void inorder(char node) 
{
	if(node == '.') return;
	
	inorder(tree[node].left);
	printf("%c", node);
	inorder(tree[node].right);
}

void postorder(char node) 
{
	if(node == '.') return;
	
	postorder(tree[node].left);
	postorder(tree[node].right);
	printf("%c", node);
}

int main(void) 
{
	int num;
	scanf("%d", &num);
	char a, b, c;
	for(int i=0; i<num; i++) {
		scanf(" %1c %1c %1c", &a, &b, &c);
		tree[a].left = b;
		tree[a].right = c;
	}

	preorder('A');
	printf("\n");
	inorder('A');
	printf("\n");
	postorder('A');
	printf("\n");

	return 0;

}
