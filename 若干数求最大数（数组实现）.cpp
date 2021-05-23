#include<stdio.h>
#include<stdlib.h>
#define  N 100
//存在 bug ！！！ 
int main()
{
	int long a[N],max=0,x,t;
	int i;

	for(i=0;i<N;i++)
	{
		scanf("%d",&a[i]);
		if(a[i]==-1) break;
		else if(max<a[i]) max=a[i];
			 else max=a[i-1];	
	}
	printf("其中最高分是%d",max);
	system("pause");
    return 0;	
}
