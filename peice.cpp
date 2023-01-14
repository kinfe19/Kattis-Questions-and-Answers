#include <iostream>
using namespace std;
int main()
{
	int n,s,l,b1,b2;
	cin>>n>>s>>l;
	b1=s>n-s?s:n-s;
	b2=l>n-l?l:n-l;
	cout<<b1*b2*4;
}
