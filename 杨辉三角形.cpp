#include<stdio.h>
#define N 21
void fun(int t[][N],int n)//函数形参为与实参同类型同维数的二维数组
{
	int i,j;
	for(i=0;i<n;i++)
	{
		t[i][0]=1;//杨辉三角形的第一列赋值为1
		t[i][i]=1;//杨辉三角形主对角线赋值为1
	}
	for(i=2;i<n;i++)//从第三行（即i为2）开始计算
		for(j=1;j<i;j++)//计算第2列（即i为1）到i-1列之间各元素的值
			t[i][j]=t[i-1][j-1]+t[i-1][j];
			//i行j列元素值为上一行前一列上一行当前列之和 
} //函数值类型为void,函数体内无return语句

int main()
{
	int a[N][N],i,j,n;
	do
	{
		printf("请输入杨辉三角形的行数（1~20）：");
		scanf("%d",&n); 
	}while(n<1 || n>20);
	fun(a,n);//以函数语句，调用fun函数求杨辉三角形
	//函数实参为二维数组名和普通变量n
	printf("\n输出杨辉三角形前%3d 行：\n",n); 
	for(i=0;i<n;i++)
	{
		for(j=0;j<=i;j++)
			printf("%6d",a[i][j]);
		printf("\n");//不可以少 
	}
	return 0; 
 } 
