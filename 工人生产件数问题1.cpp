#include<stdio.h>
#include<stdlib.h>
main()
{
	int *o;
	int m,n,q,sum=0;
	double p;
	for(m=0;m<20;m++){
		printf("请输入第%d位工人的生产件数",m+1);
		scanf("%d",&n);
		o=(int*) malloc(20*sizeof(int));
		o[m]=n;
		sum+=n;
		
		
		printf("n=%d",o);
	}
	p=sum/20.0;
	printf("n1=%d",o);
	system("pause");
}
