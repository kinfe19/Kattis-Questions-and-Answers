#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
int main()
{
	long long int n;
	cin>>n;
	double m=4.0*sqrt(n);
	if(m==int(m))
	cout<<m;
	else
	cout<<fixed<<setprecision(15)<<m;
}
