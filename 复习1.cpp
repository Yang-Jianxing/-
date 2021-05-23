#include<stdio.h>
#include<stdlib.h>
int main()
{
	/*int i,j,a,*n;
	
	scanf("%d",&a);
	/*while (a)
		scanf("%d",&j);
	for (i=0;i<a;i++)
	{
		scanf("%d",&j);
		//printf("%d\t",n[i]);
		n = (int*) malloc(100*sizeof(int));
		n[i]=j;
	}	
	printf("%d",n[i]);*/
	
	int x=0,y,max;
	
	while(1)
	{
		printf("x=:");
		scanf("%d",&x);
		printf("y=:");
		scanf("%d",&y);
		if(x>y) max=x;
		else max=y;
		if(x<0) break;
	}

	
	/*int x,y,max;
	do{
		scanf("%d",&x);
		scanf("%d",&y);
		if(x>y) max=x;
		else max=y;
	}while(x != (-1));*/
	
	printf("%d",max);
	//system("pause");
		return 0;
}
