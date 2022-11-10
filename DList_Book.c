#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//이중연결 노드 타입
typedef struct DListNode 
{
	element data;
	struct DListNode *llink;
	struct DListNode *rlink;
} DListNode;

//이중 연결 리스트 초기화
void init(DListNode *phead)
{
	phead->llink = phead;
	phead->rlink = phead;
}

//이중 연결 리스트 노드를 출력
void print_dlist(DListNode *phead)
{
	DListNode *p = phead;
	for(p = phead->rlink; p!= phead; p = p->rlink) {
		printf("<-| |%d| |-> ", p->data);
	}
	printf("\n");
}


//새로운 데이터를 노드 before의 오른쪽에 삽입
DListNode* dinsert(DListNode *before, element data) {
	DListNode *newnode = (DListNode *)malloc(sizeof(DListNode));
	newnode->data = data;
	newnode->llink = before;
	newnode->rlink = before->rlink;
	before->rlink->llink = newnode;
	before->rlink = newnode;
}

void ddelete(DListNode* head, DListNode* removed)
{
	if(removed == head)
		return;
	removed->llink->rlink = removed->rlink;
	removed->rlink->llink = removed->llink;
	free(removed);
}



int main(void)
{
	DListNode *p = (DListNode *)malloc(sizeof(DListNode));

	init(head);

	printf("추가단계\n");
	
	for(int i=0; i<5; i++)
	{
		dinsert(head, i);
		print_dlist(head);
	}

	printf("\n삭제단계\n");
	for(int i=0; i<5; i++) {
		print_dlist(head);
		ddelete(head, head->rlink);
	}
	free(head);
	return 0;
  }
