#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i,*arr,value;
	scanf("%d",&value);
	arr = (int*) malloc(100*sizeof(int));
	//arr[i]=value;//第一种给数组添加数据的方法 
	*(arr+i)=value;//第二种给数组添加数据的方法
	printf("%d/t",arr[i]);
	system("pause");
}
