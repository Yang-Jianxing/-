#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i,*arr,value;
	scanf("%d",&value);
	arr = (int*) malloc(100*sizeof(int));
	//arr[i]=value;//��һ�ָ�����������ݵķ��� 
	*(arr+i)=value;//�ڶ��ָ�����������ݵķ���
	printf("%d/t",arr[i]);
	system("pause");
}
