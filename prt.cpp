#include <iostream>
using namespace std;
int main()
{
	int sum=0,w=1;
	for(int i=1;i<=5;i++)
	{
		int a,b,c,d;
		cin>>a>>b>>c>>d;
		int j=a+b+c+d;
		if(j>sum)
		{
			sum=j;
			w=i;
		}
	}
	cout<<w<<" "<<sum;
}
