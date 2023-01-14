#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int h,v;
	double PI=3.1415926;
	cin>>h>>v;
	double m=h/sin(PI*v/180.0);
	cout<<ceil(m);
	
	
}
