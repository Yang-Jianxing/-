#include<stdio.h>
#include<stdlib.h>
int main()
{
	float a[10];
	float max,min,t,sum=0,aver;
	int i,j; 
	printf("请输入分数：\n");
	for(i=0;i<10;i++)
	{
		scanf("%f",&a[i]);
	 	sum=a[i]+sum;
	}
	printf("总分是%5.2f\n",sum);

	for(i=0;i<10;i++)
	{
 		for(j=i+1;j<10;j++)
	  	if(a[i]>a[j])
	    {
    	t=a[j];
		a[j]=a[i];
	 	a[i]=t;
		} 
	}
	printf("评分由低到高如下:\n"); 
	for(i=0;i<10;i++)
	{
	printf("%5.2f\n",a[i]);
	}
	min=a[0];
	max=a[9];
	aver=(sum-min-max)/8.0;
	printf("去掉一个最高分%5.2f和一个最低分%5.2f最终得分是:%5.2f\n",max,min,aver);
	return 0; 
	
}

