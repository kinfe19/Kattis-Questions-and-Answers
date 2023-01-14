#include <bits/stdc++.h>
using namespace std;
int main()
{
	double a,b,c,d,e,f;
	cin>>a>>b>>c>>d;
	e=(a+b+c+d)/2.0;
	f=(e-a)*(e-b)*(e-c)*(e-d);
	cout<<fixed<<setprecision(14)<<sqrt(f)<<endl;
	
	
}
