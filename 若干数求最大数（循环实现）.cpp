#include<stdio.h>
#include<stdlib.h>
int main()
{
	int y,max;
	printf("������һ������");
	scanf("%d",&max);
	while(max>=0)
	{
		printf("��������һ������");
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
