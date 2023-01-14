#include <iostream>
using namespace std;
int main()
{
	int a,b,min,max;
	cin>>a>>b;
	if(a<=b)
	{
		max=b;
		min=a;
	}
	else
	{
		max=a;
		min=b;
	}
	for(int i=min+1;i<=max+1;i++)
	cout<<i<<endl;
}
