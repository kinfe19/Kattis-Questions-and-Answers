#include <iostream>
using namespace std;
int main()
{
	int n,s=0,a;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>a;
		if(a<0)
		s++;
	}
	cout<<s;
}
