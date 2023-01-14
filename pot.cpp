#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	long long int n,sum=0;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int b,c,d,e;
		cin>>b;
		c=b%10;
		d=(b-c)/10;
		e=pow(d,c);
		sum+=e;
	}
	cout<<sum;
}
