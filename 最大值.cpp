#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a,b,c;
	printf("�����벻��ȵ�������:\n");
	scanf("%d%d%d",&a,&b,&c);
	if (a>b && a>c)
		printf("���ֵΪ��%d",a); 
	if (b>a && b>c)
		printf("���ֵΪ��%d",b);
	if (c>b && c>a)
		printf("���ֵΪ��%d",c);
	system("pause");
 } 
