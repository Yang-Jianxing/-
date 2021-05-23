#include<stdio.h>
#include<stdlib.h>
int main()
{
	int y,max;
	printf("请输入一个数：");
	scanf("%d",&max);
	while(max>=0)
	{
		printf("请输入另一个数：");
		scanf("%d",&y);
		if(y<0) break;
		else 
		{
			if(max>y) max=max;
			else max=y;
		}
	}
	printf("%d",max);
	system("pause");
}
