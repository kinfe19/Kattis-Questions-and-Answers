#include <iostream>
using namespace std;
int main()
{
	int n;
	long long int a[15]={9,25,81,289,1089,4225,16641,66049,263169,1050625,4198401,16785409,67125249,268468225,1073807361};
	cin>>n;
	if(n>=1&&n<=15)
	cout<<a[n-1];
}
