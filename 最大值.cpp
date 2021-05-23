#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a,b,c;
	printf("请输入不相等的三个数:\n");
	scanf("%d%d%d",&a,&b,&c);
	if (a>b && a>c)
		printf("最大值为：%d",a); 
	if (b>a && b>c)
		printf("最大值为：%d",b);
	if (c>b && c>a)
		printf("最大值为：%d",c);
	system("pause");
 } 
