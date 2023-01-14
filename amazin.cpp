#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int n;
	cin>>n;
	double pi=3.1415926535897932384626433832795;
	for(int o=0;o<n;o++)
	{
		double u,q,x,h1,h2,t,y;
		cin>>u>>q>>x>>h1>>h2;
		t=x/u/cos(q*pi/180.0);
		y=(u*t*sin(q*pi/180.0)-(4.905*t*t));
		if(floor(y)>h1 &&ceil(y)<h2)
		cout<<"Safe"<<endl;
		else
		cout<<"Not Safe"<<endl;
	}
}
