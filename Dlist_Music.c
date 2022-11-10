#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef int element;
typedef struct ListNode
{
	char title[20];	//노래 제목
	char singer[20];
	char style;	//노래 장르
	int year;	//발행 년도 
	int time;	//재생 시간
	struct ListNode *llink;
	struct ListNode *rlink;
}ListNode;

//초기화
void init(ListNode *head)
{
	head->llink = head;
	head->rlink = head;
}

//연결리스트 출력
void print_list(ListNode *head) 
{
	ListNode *p;
	for (p = head->rlink; p != head; p = p->rlink)
	{
		printf("\n====================================================");
		printf("\n음악제목: %s", p->title);
		printf("\n가수: %s", p->singer);
		printf("\n장르: %c", p->style);
		printf("\n년도: %d", p->year);
		printf("\n재생시간: %d", p->time);
		printf("\n====================================================");
	}
	printf("\n");
}

void insert(ListNode *before)
{
	ListNode *node = (ListNode *)malloc(sizeof(ListNode));
	///////////////////////////////////////////////////////
	printf("음악제목: ");
	scanf("%s", node->title);
	printf("가수: ");
	scanf("%s", node->singer);
	printf("장르(B, C, H, J, T): ");
	scanf(" %c", &node->style);
	printf("년도: ");
	scanf("%d", &node->year);
	printf("재생시간: ");
	scanf("%d", &node->time);
	///////////////////////////////////////////////////////
	node->llink = before;
	node->rlink = before->rlink;
	before->rlink->llink = node;
	before->rlink = node;
}

void delete(ListNode *head, ListNode *removed)
{
	if (removed == head)
		return;
	removed->llink->rlink = removed->rlink;
	removed->rlink->llink = removed->llink;
	free(removed);
}

//노드의 개수를 계산해서 반환
int list_length(ListNode *head)
{
	int count = 0;
	for(ListNode* p = head->rlink; p != head; p = p->rlink)	//전체 노드 방문
		count++;
	return count;
}

//원하는 장르만 출력 
void wanna_style(ListNode *head)
{
	fflush(stdin);

	char style; 
	printf("원하는 장르 입력 >>> "); scanf("%c", &style);

	for (ListNode *p = head->rlink; p != head; p = p->rlink)
	{
		if(p->style == style)
		{
			printf("\n====================================================");
			printf("\n노래제목: %s", p->title);
			printf("\n가수: %s", p->singer);
			printf("\n장르: %c", p->style);
			printf("\n년도: %d", p->year);
			printf("\n재생시간: %d", p->time);
			printf("\n====================================================");
		}
	}
	printf("\n\n");
}

//최신음악
void new_music(ListNode *head)
{
	int m = -1;	//m노드의 포인터 반환해서 
	for (ListNode *p = head->rlink; p != head; p = p->rlink)
	{
		if(p->year > m)//년도가 최대인 걸로 찾기 
			m = p->year;
	}

	for (ListNode *p = head->rlink; p != head; p = p->rlink)
	{
		//가장 최근에 발매된 음악 모두 출력 (여러 개 일수도 있기 때문)
		if(p->year == m)
		{
			printf("\n====================================================");
			printf("\n노래제목: %s", p->title);
			printf("\n가수: %s", p->singer);
			printf("\n장르: %c", p->style);
			printf("\n년도: %d", p->year);
			printf("\n재생시간: %d", p->time);
			printf("\n====================================================");
		}
	}
	printf("\n\n");
}

//음악 제목으로 검색하기
ListNode *search(ListNode *head, char title[])
{
	for (ListNode *p = head->rlink; p != head; p = p->rlink)
	{
		if (strcmp(title, p->title) == 0)
		{
			return p;
		}
	}
	return NULL;
}

//역순으로 출력하기 
void reverse(ListNode *head)
{
	printf("\nPRINT REVERSE\n");
	for (ListNode *p = head->llink; p != head; p = p->llink)
	{
		printf("\n====================================================");
		printf("\n노래제목: %s", p->title);
		printf("\n가수: %s", p->singer);
		printf("\n장르: %c", p->style);
		printf("\n년도: %d", p->year);
		printf("\n재생시간: %d", p->time);
		printf("\n====================================================");
	}
	printf("\n");
}

ListNode *point;	//현재 위치를 알려주는 point

// 재생메뉴 P
ListNode *play(ListNode *head, ListNode *p)
{
	ListNode *q = point;
	if (q == head)
		q = q->rlink;

	printf("\n<%s 재생중>\n.............................\n", q->title);
	for (int i = 0; i < q->time; i++)
	{
		//printf(".......");
		usleep(1000000); //1초 기다리기 
	}
	q = q->rlink; // 자동으로 다음 노드로 넘긴다.
	return q;
}

// 다음노드로 이동하는 버튼 >
void rnext(ListNode *head)
{
	ListNode *p;
	p = point->rlink;
	if (p == head)
		p = p->rlink;	//rlink는 다음!!헤드 건너뛰어야됨
	printf("\n<%s 재생중>\n.............................\n", p->title);
	for (int i = 0; i < p->time; i++)
	{
		//printf("%3d", i + 1);
		usleep(1000000); //초 단위로 바꿔줌 
	}
}

// 이전노드로 이동하는 버튼 <
void lnext(ListNode *head)
{
	ListNode *p;
	p = point->llink;
	if (p == head)
		p = p->llink;	//llink는 이전
	printf("\n<%s 재생중>\n.............................\n", p->title);
	//printf(".............................");
	for (int i = 0; i < p->time; i++)
	{
		//printf("%3d", i + 1);
		usleep(1000000);
	}
}

// 맨 앞으로 이동 F
void First(ListNode *head)
{
	point = head->rlink;
}

// 맨 뒤로 이동 L
void Last(ListNode *head)
{
	point = head->llink;
}

int main()
{
	ListNode *head = (ListNode *)malloc(sizeof(ListNode));
	init(head);
	point = head;

	char title[20]; 
	char pick; 
	char num;
	int flag = 0;
	while (flag != 1)
	{
		printf("\n\n");
		///////////////////////////////////
		printf("\n-----MENU-----\n");
		printf("\n(1)삽입");
		printf("\n(2)출력"); 
		printf("\n(3)검색"); 
		printf("\n(4)삭제"); 
		printf("\n(5)역순으로 출력");
		printf("\n(6)노드 개수 반환");
		printf("\n(7)최신음악");
		printf("\n(8)원하는 장르 노래 검색 (B, C, H, J, T) ");
		printf("\n(P)");
		printf("\n(>)");
		printf("\n(<)");
		printf("\n(F)맨 앞으로 이동");
		printf("\n(L)맨 뒤로 이동");
		printf("\n(0)프로그램 종료");
		printf("\n==> ");
		scanf(" %c", &num);
		///////////////////////////////////
		switch (num)
		{
		case '1': //삽입
			insert(head);
			break;
		case '2': //출력
			print_list(head);
			break;
		case '3': //노래제목으로 검색
			printf("노래제목: ");
			scanf("%s", title);
			ListNode *p = search(head, title);
			if (p != NULL)
				printf("\n%s는 있습니다. ", title);
			else
				printf("\n%s는 없습니다. ", title);
			break;
		case '4':  //삭제 
			printf("삭제하고 싶은 음악 제목을 입력하세요. : ");
			scanf("%s", title);
			ListNode *q = search(head, title);	//찾아서 
			if (q != NULL) //있으면 삭제하기 
			{
				delete(head, q);
				printf("\n%s 가 삭제되었습니다. ", title);
			}
			else //없으면 없다고 말해주기 
				printf("\n%s는 없습니다. ", title);
			break;
		case '5':	//역순으로 출력하기
			reverse(head);
			break;
		case '6':	//노드 개수 반환하기
			printf("현재 노드 개수 : %d\n", list_length(head));
			break;
		case '7':	//최신 음악
			new_music(head);
			break;
		case '8':	//원하는 장르의 음악 검색
			wanna_style(head);
			break;
		case 'P':	//재생 버튼
			if (head->rlink == head)	//노드가 없는 경우
			{
				printf("\n<NO NODE IN THE LIST>\n");
				break;
			}
			else
				point = play(head, point);
			break;
		case '>':	//다음 노래로 이동
			if (head->rlink == head)
			{
				printf("\n<NO NODE IN THE LIST>\n");
				break;
			}
			else{
				rnext(head);
				point = point->rlink;
				if(point == head)
					point = point->rlink;
			}
			break;
		case '<':	//이전 노래로 이동
			if (head->rlink == head)
			{
				printf("\n<NO NODE IN THE LIST\n");
				break;
			}
			else
			{
				lnext(head);
				point = point->llink;
				if(point == head)
					point = point->llink;
				break;
			}
		case 'F':	//맨 앞으로 이동
			if (head->rlink == head)
			{
				printf("\nNO NODE IN THE LIST\n");
				break;
			}
			else
			{
				First(head);
				point = play(head, point);
				break;
			}
		case 'L':	//맨 뒤로 이동
			if (head->rlink == head)
			{
				printf("\nNO NODE IN THE LIST\n");
				break;
			}
			else
			{
				Last(head);
				point = play(head, point);
				break;
			}
		case '0':	//프로그램 종료 
			flag = 1;
			printf("\n프로그램 종료\n");
			break;
		default:
			printf("\n다시 시도\n");
			break;
		}
	}

	return 0;
}
